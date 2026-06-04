from ..models.todo import Todo, TodoList
from ..repositories.todo_repository import TodoRepository

from ..exceptions.errors import TodoNotFoundError


class TodoService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    async def get_todos(self) -> TodoList:
        result = await self._repository.get_all()

        todo_list = TodoList()

        for todo in result:
            todo_list.todos.append(
                Todo(
                    id=str(todo[0]),
                    title=todo[1],
                    description=todo[2],
                    is_active=bool(todo[3]),
                )
            )

        return todo_list

    async def get_todo(self, id: str) -> Todo:
        result = await self._repository.get_one(id)

        if not result:
            raise TodoNotFoundError(id)

        todo = Todo(
            id=str(result[0]),
            title=result[1],
            description=result[2],
            is_active=bool(result[3]),
        )

        return todo

    async def insert_todo(self, todo: Todo):
        await self._repository.insert_one(todo)

    async def update_todo(self, id: str, todo: Todo):
        await self._repository.update_one(id, todo)

    async def update_todo_completely(self, id: str, todo: Todo):
        await self._repository.update_everything(id, todo)

    async def delete_todo(self, id: str):
        await self._repository.delete_one(id)
