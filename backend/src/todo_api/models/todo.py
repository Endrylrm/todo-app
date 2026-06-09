from datetime import datetime
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: str | None = Field(default=None, title="The title of the Todo.")
    title: str | None = Field(default=None, title="The title of the Todo.")
    description: str | None = Field(default=None, title="The description of the Todo.")
    is_active: bool | None = Field(default=None, title="Is the Todo Active?")
    updated_at: datetime | None = Field(
        default=None, title="Todo updated datetime - ISO Format"
    )
    created_at: datetime | None = Field(
        default=None, title="Todo created datetime - ISO Format"
    )
