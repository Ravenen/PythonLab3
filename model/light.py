from typing import Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class Light(AbstractDecor):

    def __init__(self, color: str, price_in_uah: float, decor_type: Set[DecorType], max_voltage: float,
                 number_of_bulbs: int):
        super(Light, self).__init__(color, price_in_uah, decor_type)
        self.max_voltage = max_voltage
        self.number_of_bulbs = number_of_bulbs
