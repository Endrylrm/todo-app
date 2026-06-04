from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: int | None = None
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None
    updated_at: datetime | None = None
    created_at: datetime | None = None

    @classmethod
    def from_api(cls, request: dict):
        return cls(
            id=request["id"],
            title=request["title"],
            description=request["description"],
            is_active=request["is_active"],
            updated_at=datetime.fromisoformat(request["updated_at"]),
            created_at=datetime.fromisoformat(request["created_at"]),
        )
