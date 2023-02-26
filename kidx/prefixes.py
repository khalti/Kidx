from enum import Enum, unique
from .exceptions import KIDXPrefixNotFound


@unique
class KIDXPrefixes(Enum):
    """KIDX Prefixes for different tables."""

    @classmethod
    def get(cls, key):
        enum_obj = getattr(cls, key, None)

        if enum_obj is None:
            raise KIDXPrefixNotFound(key)

        return enum_obj.value
