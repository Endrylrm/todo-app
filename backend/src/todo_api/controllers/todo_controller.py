from fastapi import APIRouter, status

from ..models.todo import Todo, TodoList

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
            self.update_todo_completely,
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

    async def get_todos(self) -> TodoList:
        return self._service.get_todos()

    async def get_todo(self, id: int) -> Todo | dict[str, str]:
        return self._service.get_todo(id)

    async def insert_todo(self, todo: Todo):
        await self._service.insert_todo(todo)

        return {"success": "todo created!"}

    async def update_todo(self, id: int, todo: Todo):
        await self._service.update_todo(id, todo)

        return {"success": f"todo {id} updated!"}

    async def update_todo_completely(self, id: int, todo: Todo):
        await self._service.update_todo_completely(id, todo)

        return {"success": f"todo {id} completely updated!"}

    async def delete_todo(self, id: int):
        await self._service.delete_todo(id)

        return {"success": f"todo {id} deleted!"}
