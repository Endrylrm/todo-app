from typing import Any

from ..models.todo import Todo
from ..repositories.todo_sqlite_repository import TodoSQLiteRepository
from ..validations.results import SQLError


class TodoService:
    def __init__(self, repository: TodoSQLiteRepository):
        self._repository = repository

    def get_todos(self) -> dict[str, Any]:
        result = self._repository.get_todos()

        if result.error.value:
            return {"failed": "SQL Error", "error": result.error.message}

        todos_rows = result.value
        todos = {}

        for todo in todos_rows:
            todos[str(todo[0])] = Todo(
                title=todo[1], description=todo[2], is_active=bool(todo[3])
            )

        return todos

    def get_todo(self, id: int) -> dict[str, Any]:
        result = self._repository.get_todo(id)

        if result.error.value:
            return {"failed": "SQL Error", "error": result.error.message}

        todo_row = result.value
        todo: dict[str, Todo] = {
            str(todo_row[0]): Todo(
                title=todo_row[1], description=todo_row[2], is_active=bool(todo_row[3])
            )
        }

        return todo

    def insert_todo(self, todo: Todo) -> SQLError:
        result = self._repository.insert_todo(todo)
        return result.error

    def update_todo_completely(self, id: int, todo: Todo) -> SQLError:
        result = self._repository.update_todo_completely(id, todo)
        return result.error

    def update_todo(self, id: int, todo: Todo) -> SQLError:
        result = self._repository.update_todo(id, todo)
        return result.error

    def delete_todo(self, id: int) -> SQLError:
        result = self._repository.delete_todo(id)
        return result.error
