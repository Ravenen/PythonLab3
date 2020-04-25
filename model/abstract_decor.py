from abc import ABC
from typing import Set

from model.decor_type import DecorType


class AbstractDecor(ABC):

    def __init__(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None):
        self.color = color
        self.price_in_uah = price_in_uah
        self.decor_type = sorted(decor_type)

    def check_criterion(self, criterion: Set[DecorType]) -> bool:
        return set(self.decor_type).issuperset(criterion)

    def __repr__(self) -> str:
        return f"color: {self.color}, price: {self.price_in_uah}, decor_type: {self.decor_type}"
