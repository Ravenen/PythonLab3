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

        >>> first_light = Light("Red", 225.50, {DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE, DecorType.DOOR}, 220.0, 25)
        >>> second_light = Light("Rainbow", 300.0, {DecorType.HOUSE_INTERIOR, DecorType.HOUSE_EXTERIOR, DecorType.OUTDOOR_TREE}, 250.0, 30)
        >>> first_garland = Garland("Green", 50.0, {DecorType.WORKING_PLACE, DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE}, 3.0, True)
        >>> second_garland = Garland("Blue", 75.0, {DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE, DecorType.OUTDOOR_TREE}, 5.0, False)
        >>> first_treetoy = TreeToy("Yellow", 25.50, {DecorType.INDOOR_TREE}, "sphere", 4)
        >>> second_treetoy = TreeToy("Multicolor", 50.50, {DecorType.INDOOR_TREE, DecorType.HOUSE_INTERIOR}, "Santa Clause", 5)
        >>> decor_list = [first_light, second_light, first_garland, second_garland, first_treetoy, second_treetoy]
        >>> manager = ChristmasFairManager(decor_list)

        >>> manager.find_decorations_by_decor_type({DecorType.HOUSE_INTERIOR, DecorType.INDOOR_TREE})
        [Light[color: Red, price: 225.5, decor_type: [<DecorType.INDOOR_TREE: 1>, <DecorType.HOUSE_INTERIOR: 3>, <DecorType.DOOR: 6>], max_voltage: 220.0, number_of_bulbs: 25, Garland[color: Green, price: 50.0, decor_type: [<DecorType.INDOOR_TREE: 1>, <DecorType.HOUSE_INTERIOR: 3>, <DecorType.WORKING_PLACE: 5>], length: 3.0, is_natural: True, Garland[color: Blue, price: 75.0, decor_type: [<DecorType.INDOOR_TREE: 1>, <DecorType.OUTDOOR_TREE: 2>, <DecorType.HOUSE_INTERIOR: 3>], length: 5.0, is_natural: False, TreeToy[color: Multicolor, price: 50.5, decor_type: [<DecorType.INDOOR_TREE: 1>, <DecorType.HOUSE_INTERIOR: 3>], form: Santa Clause, volume_in_cm_cube: 5]
        >>> manager.find_decorations_by_decor_type({DecorType.OUTDOOR_TREE})
        [Light[color: Rainbow, price: 300.0, decor_type: [<DecorType.OUTDOOR_TREE: 2>, <DecorType.HOUSE_INTERIOR: 3>, <DecorType.HOUSE_EXTERIOR: 4>], max_voltage: 250.0, number_of_bulbs: 30, Garland[color: Blue, price: 75.0, decor_type: [<DecorType.INDOOR_TREE: 1>, <DecorType.OUTDOOR_TREE: 2>, <DecorType.HOUSE_INTERIOR: 3>], length: 5.0, is_natural: False]
        >>> manager.find_decorations_by_decor_type({DecorType.WORKING_PLACE, DecorType.DOOR})
        []
        """
        found_decorations = [decor for decor in self.decorations if decor.check_criterion(criterion)]
        return found_decorations


if __name__ == '__main__':
    import doctest
    doctest.testmod()
