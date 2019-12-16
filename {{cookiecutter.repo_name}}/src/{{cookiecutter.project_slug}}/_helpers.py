import logging
from enum import Enum
from typing import Any, Iterable, Tuple


_LOGGER = logging.getLogger(__name__)


class ExtendedEnum(Enum):
    """ Add helper methods to Enums """

    @classmethod
    def values(cls) -> Iterable[Any]:
        """ Returns iterator of all values """
        return map(lambda member: member.value, cls)

    @classmethod
    def key_values(cls) -> Iterable[Tuple[str, Any]]:
        """ Returns an iterator """
        return map(lambda member: (member.name, member.value), cls)
