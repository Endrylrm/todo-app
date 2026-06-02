import sqlite3

from typing import Any

from ..models.todo import Todo

from ..validations.results import SQLValidationResult, SQLError


class TodoRepository:
    def __init__(self, path: str):
        self._path = path
        self._conn = self.create_connection()
        self.create_table()

    def create_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._path)
        return conn

    def create_table(self):
        cursor = self._conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                is_active BOOLEAN
            )
        """)

    def get_todos(self) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute("SELECT * FROM todos")
            todos = cursor.fetchall()
            return SQLValidationResult(todos, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            return SQLValidationResult(None, SQLError(error, True))

    def get_todo(self, id: int) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
            todo = cursor.fetchone()
            return SQLValidationResult(todo, SQLError("", False))
        except sqlite3.Error as error:
            print(f"Error: {error}")
            return SQLValidationResult(None, SQLError(error, True))

    def insert_todo(self, todo: Todo) -> SQLValidationResult:
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

    def update_todo_completely(self, id: int, todo: Todo) -> SQLValidationResult:
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

    def update_todo(self, id: int, todo: Todo) -> SQLValidationResult:
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

    def delete_todo(self, id: int) -> SQLValidationResult:
        try:
            cursor = self._conn.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
            self._conn.commit()
            return SQLValidationResult(None, SQLError("", False))

        except sqlite3.Error as error:
            print(f"Error: {error}")
            self._conn.rollback()
            return SQLValidationResult(None, SQLError(error, True))
