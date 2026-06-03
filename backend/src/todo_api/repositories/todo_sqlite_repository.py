import sqlite3

from typing import Any

from .todo_repository import TodoRepository

from ..models.todo import Todo

from ..validations.results import SQLValidationResult, SQLError


class TodoSQLiteRepository(TodoRepository):
    def __init__(self, connection: sqlite3.Connection):
        self._conn = connection

    def get_all(self) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute("SELECT * FROM todos")
            todos = cursor.fetchall()
            return SQLValidationResult(todos, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            return SQLValidationResult(None, SQLError(error, True))

    def get_one(self, id: str) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
            todo = cursor.fetchone()
            return SQLValidationResult(todo, SQLError("", False))
        except sqlite3.Error as error:
            print(f"Error: {error}")
            return SQLValidationResult(None, SQLError(error, True))

    def insert_one(self, todo: Todo) -> SQLValidationResult:
        try:
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
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))

    def insert_many(self, todos: list[Todo]) -> SQLValidationResult:
        try:
            for todo in todos:
                self.insert_one(todo)

            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))

    def update_one(self, id: str, todo: Todo) -> SQLValidationResult:
        try:
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
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))

    def update_many(self, todos: list[Todo]) -> SQLValidationResult:
        try:
            for todo in todos:
                self.update_one(1, todo)
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))

    def update_everything(self, id: str, todo: Todo) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute(
                "UPDATE todos SET title = ?, description = ?, is_active = ? WHERE id = ?",
                (todo.title, todo.description, int(todo.is_active), id),
            )
            self._conn.commit()
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))

    def delete_one(self, id: str) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
            self._conn.commit()
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))

    def delete_many(self, ids: str) -> SQLValidationResult:
        try:
            for id in ids:
                self.delete_one(id)
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))
