from typing import Any

from fastapi import APIRouter, status

from ..dto.requests import CreateTodoRequest, UpdateTodoRequest, ReplaceTodoRequest

from ..services.todo_service import TodoService


class TodoController:
    def __init__(self, service: TodoService):
        self.router = APIRouter(prefix="/api/todos")
        self._service = service

        self.router.add_api_route(
            "/", self.get_todos, methods=["GET"], status_code=status.HTTP_200_OK
        )
        self.router.add_api_route(
            "/{id}", self.get_todo, methods=["GET"], status_code=status.HTTP_200_OK
        )
        self.router.add_api_route(
            "/", self.insert_todo, methods=["POST"], status_code=status.HTTP_201_CREATED
        )
        self.router.add_api_route(
            "/{id}",
            self.replace_todo,
            methods=["PUT"],
            status_code=status.HTTP_200_OK,
        )
        self.router.add_api_route(
            "/{id}", self.update_todo, methods=["PATCH"], status_code=status.HTTP_200_OK
        )
        self.router.add_api_route(
            "/{id}",
            self.delete_todo,
            methods=["DELETE"],
            status_code=status.HTTP_200_OK,
        )

    async def get_todos(self) -> dict[str, Any]:
        todos = await self._service.get_todos()
        return {"success": "Todos found!", "data": todos}

    async def get_todo(self, id: int) -> dict[str, Any]:
        todo = await self._service.get_todo(id)
        return {"success": f"Todo with id: {todo.id} found!", "data": todo}

    async def insert_todo(self, request: CreateTodoRequest) -> dict[str, Any]:
        new_todo = await self._service.insert_todo(request)

        return {"success": f"Todo with id: {new_todo.id} created!", "data": new_todo}

    async def update_todo(self, id: int, request: UpdateTodoRequest) -> dict[str, Any]:
        updated_todo = await self._service.update_todo(id, request)

        return {"success": f"Todo with id: {id} updated!", "data": updated_todo}

    async def replace_todo(
        self, id: int, request: ReplaceTodoRequest
    ) -> dict[str, Any]:
        replaced_todo = await self._service.replace_todo(id, request)

        return {"success": f"Todo with id: {id} replaced!", "data": replaced_todo}

    async def delete_todo(self, id: int) -> dict[str, str]:
        await self._service.delete_todo(id)

        return {"success": f"Todo with id: {id} deleted!"}
