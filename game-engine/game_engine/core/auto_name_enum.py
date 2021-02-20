from typing import Any, List, Optional
from enum import Enum, auto, unique

class AutoNameEnum(str, Enum):
    # Type ignored due to special case, should not be staticmethod decorated,
    # but also shouldn't have a self instance reference.
    # This is a specail case for Enums which type-checkers don't quite handle.
    # https://github.com/python/mypy/issues/7591
    # https://github.com/microsoft/pyright/issues/800
    def _generate_next_value_(  # type: ignore
        name: str,
        start: int,
        count: int,
        last_values: Optional[List[Any]],
    ) -> str:
        "Automatically generates ENUM value from propery name"
        return name

