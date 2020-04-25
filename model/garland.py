from typing import Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class Garland(AbstractDecor):

    def __init__(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None,
                 length_in_metres: float = None, is_natural: bool = None):
        super(Garland, self).__init__(color, price_in_uah, decor_type)
        self.length_in_metres = length_in_metres
        self.is_natural = is_natural

    def __repr__(self) -> str:
        return f"Garland[{super().__repr__()}, length: {self.length_in_metres}, is_natural: {self.is_natural}"
