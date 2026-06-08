import sqlite3

from datetime import datetime, UTC

from typing import Any

from .todo_repository import TodoRepository

from ..models.todo import Todo

from ..exceptions.errors import (
    TodoNotFoundError,
    TodoInvalidDataError,
    TodoEmptyDataError,
)


class TodoSQLiteRepository(TodoRepository):
    def __init__(self, connection: sqlite3.Connection):
        self._connection = connection

    async def get_all(self) -> Any:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        return todos

    async def get_one(self, id: str) -> Any:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
        todo = cursor.fetchone()
        return todo

    async def insert_one(self, todo: Todo):
        self._check_empty_todo(todo)
        self._validate_todo(todo)

        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO todos (title, description, is_active) VALUES (?, ?, ?)",
                (
                    str(todo.title),
                    str(todo.description),
                    int(todo.is_active),
                ),
            )

    async def insert_many(self, todos: list[Todo]):
        for todo in todos:
            self.insert_one(todo)

    async def update_one(self, id: str, todo: Todo):
        # we don't accept empty todos.
        self._check_empty_todo(todo)

        # check if todo exist
        todo = await self.get_one(id)

        if todo is None:
            raise TodoNotFoundError(id)

        sql = "UPDATE todos SET "
        temp_parameter_list = []

        if todo.title is not None:
            sql = sql + "title = ?,"
            temp_parameter_list.append(str(todo.title))

        if todo.description is not None:
            sql = sql + "description = ?,"
            temp_parameter_list.append(str(todo.description))

        if todo.is_active is not None:
            sql = sql + "is_active = ?,"
            temp_parameter_list.append(int(todo.is_active))

        sql = sql + f"updated_at = ?"
        temp_parameter_list.append(datetime.now(UTC).isoformat())

        sql = sql + " WHERE id = ?"
        temp_parameter_list.append(id)

        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute(
                sql,
                tuple(temp_parameter_list),
            )

    async def update_many(self, todos: list[Todo]):
        for todo in todos:
            self.update_one(todo.id, todo)

    async def update_everything(self, id: str, todo: Todo):
        self._check_empty_todo(todo)
        self._validate_todo(todo)

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
                    updated_at = excluded.updated_at;
                """,
                (
                    id,
                    str(todo.title),
                    str(todo.description),
                    int(todo.is_active),
                    datetime.now(UTC).isoformat(),
                ),
            )

    async def delete_one(self, id: str):
        # check if todo exist
        todo = await self.get_one(id)

        if todo is None:
            raise TodoNotFoundError(id)

        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (id,))

    async def delete_many(self, ids: list[str]):
        for id in ids:
            self.delete_one(id)

    def _check_empty_todo(self, todo: Todo):
        if todo.title is None and todo.description is None and todo.is_active is None:
            raise TodoEmptyDataError()

    def _validate_todo(self, todo: Todo):
        if todo.title is None:
            raise TodoInvalidDataError("title")

        if todo.description is None:
            raise TodoInvalidDataError("description")

        if todo.is_active is None:
            raise TodoInvalidDataError("is_active")
