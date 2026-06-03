from ..models.todo import Todo, TodoList
from ..repositories.todo_repository import TodoRepository
from ..validations.results import SQLError


class TodoService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    def get_todos(self) -> TodoList:
        result = self._repository.get_all()

        if result.error.value:
            return {"failed": "SQL Error", "error": result.error.message}

        todos_rows = result.value
        todo_list = TodoList()

        for todo in todos_rows:
            todo_list.todos.append(
                Todo(
                    id=str(todo[0]),
                    title=todo[1],
                    description=todo[2],
                    is_active=bool(todo[3]),
                ).model_dump()
            )

        return todo_list

    def get_todo(self, id: str) -> Todo:
        result = self._repository.get_one(id)

        if result.error.value:
            return {"failed": "SQL Error", "error": result.error.message}

        todo_row = result.value
        todo = Todo(
            id=str(todo_row[0]),
            title=todo_row[1],
            description=todo_row[2],
            is_active=bool(todo_row[3]),
        ).model_dump()

        return todo

    def insert_todo(self, todo: Todo) -> SQLError:
        result = self._repository.insert_one(todo)
        return result.error

    def update_todo(self, id: str, todo: Todo) -> SQLError:
        result = self._repository.update_one(id, todo)
        return result.error

    def update_todo_completely(self, id: str, todo: Todo) -> SQLError:
        result = self._repository.update_everything(id, todo)
        return result.error

    def delete_todo(self, id: str) -> SQLError:
        result = self._repository.delete_one(id)
        return result.error
