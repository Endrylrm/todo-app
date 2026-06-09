from pydantic import BaseModel


class BaseTodoRequest(BaseModel):
    title: str
    description: str
    is_active: bool


class CreateTodoRequest(BaseTodoRequest): ...


class UpdateTodoRequest(BaseTodoRequest):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None


class ReplaceTodoRequest(BaseTodoRequest): ...
