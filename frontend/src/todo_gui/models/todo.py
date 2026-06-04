from dataclasses import dataclass, field


@dataclass
class Todo:
    id: int | None = field(default_factory=None)
    title: str | None = field(default_factory=None)
    description: str | None = field(default_factory=None)
    is_active: bool | None = field(default_factory=None)
