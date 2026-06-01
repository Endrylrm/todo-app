from pydantic import BaseModel, Field


class Todo(BaseModel):
    title: str | None = Field(default=None, title="The title of the Todo.")
    description: str | None = Field(default=None, title="The description of the Todo.")
    is_active: bool | None = Field(default=None, title="Is the Todo Active?")
