from datetime import datetime, UTC
from typing import Any

from .todo_repository import TodoRepository

from ..databases.sqlite_db import SQLiteDB

from ..models.todo import Todo


class TodoSQLiteRepository(TodoRepository):
    def __init__(self, db: SQLiteDB):
        self._db = db
        self._connection = self._db.create_connection()

    async def get_all(self) -> list[Any]:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM todos ORDER BY id")
        todos = cursor.fetchall()
        return todos

    async def get_one(self, id: str) -> Any:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
        todo = cursor.fetchone()
        return todo

    async def insert_one(self, todo: Todo) -> Any:
        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute(
                """
                INSERT INTO todos (title, description, is_active)
                VALUES (?, ?, ?)
                RETURNING *
                """,
                (
                    str(todo.title),
                    str(todo.description),
                    int(todo.is_active),
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

        columns = [f"{column} = ?" for column in data.keys()]

        temp_parameter_list = list(data.values())
        temp_parameter_list.append(id)

        sql = f"""
            UPDATE todos SET {", ".join(columns)}
            WHERE id = ?
            RETURNING *
        """

        with self._connection:
            cursor = self._connection.cursor()
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

    async def upsert_one(self, id: str, todo: Todo):
        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute(
                """
                INSERT INTO todos (id, title, description, is_active, updated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(id)
                DO UPDATE SET
                    title = excluded.title,
                    description = excluded.description,
                    is_active = excluded.is_active,
                    updated_at = excluded.updated_at
                RETURNING *
                """,
                (
                    id,
                    str(todo.title),
                    str(todo.description),
                    int(todo.is_active),
                    datetime.now(UTC).isoformat(),
                ),
            )
            upserted_todo = cursor.fetchone()
            return upserted_todo

    async def upsert_many(self, todos: list[Todo]) -> list[Any]:
        upserted_todos = []
        for todo in todos:
            upserted_todo = await self.upsert_one(todo.id, todo)
            upserted_todos.append(upserted_todo)
        return upserted_todos

    async def delete_one(self, id: str):
        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (id,))

    async def delete_many(self, ids: list[str]):
        for id in ids:
            self.delete_one(id)
