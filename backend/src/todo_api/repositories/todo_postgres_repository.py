from datetime import datetime, UTC
from typing import Any

from .todo_repository import TodoRepository

from ..databases.postgres_db import PostgreSQLDB

from ..models.todo import Todo


class TodoPostgresRepository(TodoRepository):
    def __init__(self, db: PostgreSQLDB):
        self._db = db

    async def get_all(self) -> list[Any]:
        with self._db.create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM todos")
                todos = cursor.fetchall()
                return todos

    async def get_one(self, id: str) -> Any:
        with self._db.create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM todos WHERE id = %s", (id,))
                todo = cursor.fetchone()
                return todo

    async def insert_one(self, todo: Todo) -> Any:
        with self._db.create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO todos (title, description, is_active)
                    VALUES (%s, %s, %s)
                    RETURNING *
                    """,
                    (
                        str(todo.title),
                        str(todo.description),
                        todo.is_active,
                    ),
                )
                new_todo = cursor.fetchone()
                return new_todo

    async def insert_many(self, todos: list[Todo]) -> list[Any]:
        inserted_todos = []
        for todo in todos:
            new_todo = await self.insert_one(todo)
            inserted_todos.append(new_todo)
        return inserted_todos

    async def update_one(self, id: str, todo: Todo) -> Any:
        data = todo.model_dump(exclude_none=True)
        data["updated_at"] = datetime.now(UTC).isoformat()

        columns = [f"{column} = %s" for column in data.keys()]

        temp_parameter_list = list(data.values())
        temp_parameter_list.append(id)

        sql = f"""
            UPDATE todos SET {", ".join(columns)}
            WHERE id = %s
            RETURNING *
        """

        with self._db.create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    sql,
                    tuple(temp_parameter_list),
                )
                updated_todo = cursor.fetchone()
                return updated_todo

    async def update_many(self, todos: list[Todo]) -> list[Any]:
        updated_todos = []
        for todo in todos:
            updated_todo = await self.update_one(todo.id, todo)
            updated_todos.append(updated_todo)
        return updated_todos

    async def replace_one(self, id: str, todo: Todo):
        with self._db.create_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO todos (id, title, description, is_active, updated_at)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT(id)
                    DO UPDATE SET
                        title = EXCLUDED.title,
                        description = EXCLUDED.description,
                        is_active = EXCLUDED.is_active,
                        updated_at = NOW()
                    RETURNING *
                    """,
                    (
                        id,
                        str(todo.title),
                        str(todo.description),
                        todo.is_active,
                        datetime.now(UTC).isoformat(),
                    ),
                )
                replaced_todo = cursor.fetchone()
                return replaced_todo

    async def replace_many(self, todos: list[Todo]) -> list[Any]:
        replaced_todos = []
        for todo in todos:
            replaced_todo = await self.replace_todo(todo.id, todo)
            replaced_todos.append(replaced_todo)
        return replaced_todos

    async def delete_one(self, id: str):
        with self._db.create_connection() as conn:
            with conn.cursor() as cursor:
                cursor = self._connection.cursor()
                cursor.execute("DELETE FROM todos WHERE id = %s", (id,))

    async def delete_many(self, ids: list[str]):
        for id in ids:
            self.delete_one(id)
