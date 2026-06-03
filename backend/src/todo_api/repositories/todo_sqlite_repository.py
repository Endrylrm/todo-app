import sqlite3

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
        self._conn = connection

    def get_all(self) -> Any:
        cursor = self._conn.cursor()
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        return todos

    def get_one(self, id: str) -> Any:
        cursor = self._conn.cursor()
        cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
        todo = cursor.fetchone()

        if todo is None:
            raise TodoNotFoundError(id)
        return todo

    def insert_one(self, todo: Todo):
        self._check_empty_todo(todo)
        self._validate_todo(todo)

        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO todos (title, description, is_active) VALUES (?, ?, ?)",
            (
                todo.title,
                todo.description,
                int(todo.is_active),
            ),
        )
        self._conn.commit()

    def insert_many(self, todos: list[Todo]):
        for todo in todos:
            self.insert_one(todo)

    def update_one(self, id: str, todo: Todo):
        # we don't accept empty todos.
        self._check_empty_todo(todo)

        # check if user exist
        user = self.get_one(id)

        cursor = self._conn.cursor()
        sql = "UPDATE todos SET "
        temp_parameter_list = []

        if todo.title is not None:
            sql = sql + "title = ?,"
            temp_parameter_list.append(todo.title)

        if todo.description is not None:
            sql = sql + "description = ?,"
            temp_parameter_list.append(todo.description)

        if todo.is_active is not None:
            sql = sql + "is_active = ?,"
            temp_parameter_list.append(int(todo.is_active))

        sql = sql.rstrip(",") + " WHERE id = ?"
        temp_parameter_list.append(id)

        cursor.execute(
            sql,
            tuple(temp_parameter_list),
        )
        self._conn.commit()

    def update_many(self, todos: list[Todo]):
        for todo in todos:
            self.update_one(1, todo)

    def update_everything(self, id: str, todo: Todo):
        self._check_empty_todo(todo)
        self._validate_todo(todo)

        if not id:
            self.insert_one(todo)
            return

        cursor = self._conn.cursor()
        cursor.execute(
            "UPDATE todos SET title = ?, description = ?, is_active = ? WHERE id = ?",
            (todo.title, todo.description, int(todo.is_active), id),
        )
        self._conn.commit()

    def delete_one(self, id: str):
        # check if user exist
        user = self.get_one(id)

        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
        self._conn.commit()

    def delete_many(self, ids: list[str]):
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
