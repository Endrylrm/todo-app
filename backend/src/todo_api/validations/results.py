from dataclasses import dataclass

from typing import NamedTuple, Any


@dataclass(frozen=True)
class SQLError:
    message: str = ""
    value: bool = False


class SQLValidationResult(NamedTuple):
    value: Any | None = None
    error: SQLError | None = None
