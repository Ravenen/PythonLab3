from typing import Set

from model.decor_type import DecorType


class AbstractDecor(object):

    def __init__(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None):
        self.color = color
        self.price_in_uah = price_in_uah
        self.decor_type = decor_type

    def set_fields(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None):
        self.color = color
        self.price_in_uah = price_in_uah
        self.decor_type = decor_type

    def check_criterion(self, criterion: Set[DecorType]) -> bool:
        return self.decor_type.issuperset(criterion)

    def __repr__(self) -> str:
        return f"color: {self.color}, price: {self.price_in_uah}, decor_type: {self.decor_type}"
