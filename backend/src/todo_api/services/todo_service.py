from datetime import datetime

from ..dto.requests import CreateTodoRequest, UpdateTodoRequest, ReplaceTodoRequest
from ..dto.responses import TodoResponse

from ..models.todo import Todo

from ..repositories.todo_repository import TodoRepository

from ..exceptions.errors import TodoNotFoundError, TodoNotCreatedError


class TodoService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    async def get_todos(self) -> list[TodoResponse]:
        result = await self._repository.get_all()

        todo_list = []

        for todo in result:
            todo_list.append(
                TodoResponse(
                    id=str(todo[0]),
                    title=todo[1],
                    description=todo[2],
                    is_active=bool(todo[3]),
                    updated_at=datetime.fromisoformat(str(todo[4])),
                    created_at=datetime.fromisoformat(str(todo[5])),
                )
            )

        return todo_list

    async def get_todo(self, id: str) -> TodoResponse:
        result = await self._repository.get_one(id)

        if not result:
            raise TodoNotFoundError(id)

        todo = TodoResponse(
            id=str(result[0]),
            title=result[1],
            description=result[2],
            is_active=bool(result[3]),
            updated_at=datetime.fromisoformat(str(result[4])),
            created_at=datetime.fromisoformat(str(result[5])),
        )

        return todo

    async def insert_todo(self, request: CreateTodoRequest) -> TodoResponse:
        todo = Todo(
            title=request.title,
            description=request.description,
            is_active=request.is_active,
        )

        result = await self._repository.insert_one(todo)

        if not result:
            raise TodoNotCreatedError()

        new_todo = TodoResponse(
            id=str(result[0]),
            title=result[1],
            description=result[2],
            is_active=bool(result[3]),
            updated_at=datetime.fromisoformat(str(result[4])),
            created_at=datetime.fromisoformat(str(result[5])),
        )

        return new_todo

    async def update_todo(self, id: str, request: UpdateTodoRequest) -> TodoResponse:
        await self._check_todo_exists(id)

        todo = Todo(
            title=request.title,
            description=request.description,
            is_active=request.is_active,
        )

        result = await self._repository.update_one(id, todo)
        print(result)

        updated_todo = TodoResponse(
            id=str(result[0]),
            title=result[1],
            description=result[2],
            is_active=bool(result[3]),
            updated_at=datetime.fromisoformat(str(result[4])),
            created_at=datetime.fromisoformat(str(result[5])),
        )

        return updated_todo

    async def upsert_todo(self, id: str, request: ReplaceTodoRequest) -> TodoResponse:
        await self._check_todo_exists(id)

        todo = Todo(
            title=request.title,
            description=request.description,
            is_active=request.is_active,
        )

        result = await self._repository.upsert_one(id, todo)

        upserted_todo = TodoResponse(
            id=str(result[0]),
            title=result[1],
            description=result[2],
            is_active=bool(result[3]),
            updated_at=datetime.fromisoformat(str(result[4])),
            created_at=datetime.fromisoformat(str(result[5])),
        )

        return upserted_todo

    async def delete_todo(self, id: str):
        await self._check_todo_exists(id)

        await self._repository.delete_one(id)

    async def _check_todo_exists(self, id: str):
        todo_exists = await self._repository.get_one(id)

        if todo_exists is None:
            raise TodoNotFoundError(id)
