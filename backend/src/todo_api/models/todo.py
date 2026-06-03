from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: str | None = Field(default=None, title="The title of the Todo.")
    title: str | None = Field(default=None, title="The title of the Todo.")
    description: str | None = Field(default=None, title="The description of the Todo.")
    is_active: bool | None = Field(default=None, title="Is the Todo Active?")


class TodoList(BaseModel):
    todos: list[Todo] = Field(default=[], title="List of Todos.")
