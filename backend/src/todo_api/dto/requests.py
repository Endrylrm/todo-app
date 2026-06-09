from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    title: str
    description: str
    is_active: bool


class UpdateTodoRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None


class ReplaceTodoRequest(BaseModel):
    title: str
    description: str
    is_active: bool
