from datetime import datetime

from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: str
    title: str
    description: str
    is_active: bool
    updated_at: datetime
    created_at: datetime
