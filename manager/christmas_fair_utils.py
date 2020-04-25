from typing import List

from model.abstract_decor import AbstractDecor
from model.sort_type import SortType


class ChristmasFairUtils(object):

    @staticmethod
    def sort_decorations_by_price(decorations: List[AbstractDecor], sort_type: SortType = SortType.ASCENDING) -> List[AbstractDecor]:
        return ChristmasFairUtils.sort_decorations_by(decorations, sort_type, lambda decor: decor.price_in_uah)

    @staticmethod
    def sort_decorations_by_color(decorations: List[AbstractDecor], sort_type: SortType = SortType.ASCENDING) -> List[AbstractDecor]:
        return ChristmasFairUtils.sort_decorations_by(decorations, sort_type, lambda decor: decor.color)

    @staticmethod
    def sort_decorations_by(decorations: List[AbstractDecor], sort_type: SortType, key) -> List[AbstractDecor]:
        return sorted(decorations, key=key, reverse=(sort_type == SortType.DESCENDING))
