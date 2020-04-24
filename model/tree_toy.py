from typing import Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class TreeToy(AbstractDecor):

    def __init__(self, color: str, price_in_uah: float, decor_type: Set[DecorType], form: str, volume_in_cm_cume: int):
        super(TreeToy, self).__init__(color, price_in_uah, decor_type)
        self.form = form
        self.volume_in_cm_cume = volume_in_cm_cume
