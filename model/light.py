from typing import Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class Light(AbstractDecor):

    def __init__(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None, max_voltage: float = None,
                 number_of_bulbs: int = None):
        super(Light, self).__init__(color, price_in_uah, decor_type)
        self.max_voltage = max_voltage
        self.number_of_bulbs = number_of_bulbs

    def __repr__(self) -> str:
        return f"Light[{super().__repr__()}, max_voltage: {self.max_voltage}, number_of_bulbs: {self.number_of_bulbs}"
