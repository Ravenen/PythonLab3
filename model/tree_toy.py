from typing import Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class TreeToy(AbstractDecor):

    def __init__(self, color: str, price_in_uah: float, decor_type: Set[DecorType], form: str, volume_in_cm_cube: int):
        super(TreeToy, self).__init__(color, price_in_uah, decor_type)
        self.form = form
        self.volume_in_cm_cube = volume_in_cm_cube

    def __repr__(self) -> str:
        return f"TreeToy[{super().__repr__()}, form: {self.form}, volume_in_cm_cube: {self.volume_in_cm_cube}"
