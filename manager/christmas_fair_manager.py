from typing import List, Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType
from model.garland import Garland
from model.light import Light
from model.tree_toy import TreeToy


class ChristmasFairManager(object):

    def __init__(self, decorations: List[AbstractDecor]):
        self.decorations = decorations

    def find_decorations_by_decor_type(self, criterion: Set[DecorType]) -> List[AbstractDecor]:
        """
        Returns a List of decorations that correspond to criteria - Set of DecorType`s

        >>> decor_list = [Light(color="Red light", decor_type={DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE, DecorType.DOOR}),
        ...                 Light(color="Blue light", decor_type={DecorType.HOUSE_INTERIOR, DecorType.HOUSE_EXTERIOR, DecorType.OUTDOOR_TREE}),
        ...                 Garland(color="Red garland", decor_type={DecorType.WORKING_PLACE, DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE}),
        ...                 Garland(color="Blue garland", decor_type={DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE, DecorType.OUTDOOR_TREE}),
        ...                 TreeToy(color="Red toy", decor_type={DecorType.INDOOR_TREE}),
        ...                 TreeToy(color="Blue toy", decor_type={DecorType.INDOOR_TREE, DecorType.HOUSE_INTERIOR})]
        >>> manager = ChristmasFairManager(decor_list)

        >>> found_decor_list = manager.find_decorations_by_decor_type({DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE})
        >>> [decor.color for decor in found_decor_list]
        ['Red light', 'Red garland', 'Blue garland', 'Blue toy']
        >>> found_decor_list = manager.find_decorations_by_decor_type({DecorType.OUTDOOR_TREE})
        >>> [decor.color for decor in found_decor_list]
        ['Blue light', 'Blue garland']
        >>> found_decor_list = manager.find_decorations_by_decor_type({DecorType.WORKING_PLACE, DecorType.DOOR})
        >>> [decor.color for decor in found_decor_list]
        []
        """
        found_decorations = [decor for decor in self.decorations if decor.check_criterion(criterion)]
        return found_decorations


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
