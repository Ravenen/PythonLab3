from abc import ABC
from typing import Set

from model.decor_type import DecorType


class AbstractDecor(ABC):

    def __init__(self, color: str, price_in_uah: float, decor_type: Set[DecorType]):
        self.color = color
        self.price_in_uah = price_in_uah
        self.decor_type = decor_type

    def check_criterion(self, criterion: Set[DecorType]) -> bool:
        return self.decor_type.issuperset(criterion)
