from typing import Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class Garland(AbstractDecor):

    def __init__(self, color: str, price_in_uah: float, decor_type: Set[DecorType], length_in_metres: float,
                 is_natural: bool):
        super(Garland, self).__init__(color, price_in_uah, decor_type)
        self.length_in_metres = length_in_metres
        self.is_natural = is_natural
