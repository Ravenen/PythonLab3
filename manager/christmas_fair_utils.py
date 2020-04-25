from typing import List

from model.abstract_decor import AbstractDecor
from model.garland import Garland
from model.light import Light
from model.sort_type import SortType
from model.tree_toy import TreeToy


class ChristmasFairUtils(object):

    @staticmethod
    def sort_decorations_by_price(decorations: List[AbstractDecor], sort_type: SortType = SortType.ASCENDING) -> List[AbstractDecor]:
        """
        Returns a list of AbtstractDecors, sorted by price with order, set in SortType (Ascending by default)

        >>> decor_list = [Light(color="Red", price_in_uah=225.50),
        ...                 Light(color="Rainbow", price_in_uah=300.0),
        ...                 Garland(color="Green", price_in_uah=50.0),
        ...                 Garland(color="Blue", price_in_uah=75.0),
        ...                 TreeToy(color="Yellow", price_in_uah=25.50),
        ...                 TreeToy(color="Multicolor", price_in_uah=50.50)]

        >>> sorted_by_price_asc = ChristmasFairUtils.sort_decorations_by_price(decor_list)
        >>> [decor.price_in_uah for decor in sorted_by_price_asc]
        [25.5, 50.0, 50.5, 75.0, 225.5, 300.0]
        >>> sorted_by_price_desc = ChristmasFairUtils.sort_decorations_by_price(decor_list, SortType.DESCENDING)
        >>> [decor.price_in_uah for decor in sorted_by_price_desc]
        [300.0, 225.5, 75.0, 50.5, 50.0, 25.5]
        """
        return ChristmasFairUtils.sort_decorations_by(decorations, sort_type, lambda decor: decor.price_in_uah)

    @staticmethod
    def sort_decorations_by_color(decorations: List[AbstractDecor], sort_type: SortType = SortType.ASCENDING) -> List[AbstractDecor]:
        """
        Returns a list of AbtstractDecors, sorted by color with order, set in SortType (Ascending by default)

        >>> decor_list = [Light(color="Red", price_in_uah=225.50),
        ...                 Light(color="Rainbow", price_in_uah=300.0),
        ...                 Garland(color="Green", price_in_uah=50.0),
        ...                 Garland(color="Blue", price_in_uah=75.0),
        ...                 TreeToy(color="Yellow", price_in_uah=25.50),
        ...                 TreeToy(color="Multicolor", price_in_uah=50.50)]

        >>> sorted_by_color_asc = ChristmasFairUtils.sort_decorations_by_color(decor_list)
        >>> [decor.color for decor in sorted_by_color_asc]
        ['Blue', 'Green', 'Multicolor', 'Rainbow', 'Red', 'Yellow']
        >>> sorted_by_color_desc = ChristmasFairUtils.sort_decorations_by_color(decor_list, SortType.DESCENDING)
        >>> [decor.color for decor in sorted_by_color_desc]
        ['Yellow', 'Red', 'Rainbow', 'Multicolor', 'Green', 'Blue']
        """
        return ChristmasFairUtils.sort_decorations_by(decorations, sort_type, lambda decor: decor.color)

    @staticmethod
    def sort_decorations_by(decorations: List[AbstractDecor], sort_type: SortType, key) -> List[AbstractDecor]:
        return sorted(decorations, key=key, reverse=(sort_type == SortType.DESCENDING))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
