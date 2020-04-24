from typing import List, Set

from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class ChristmasFairManager(object):

    def __init__(self, decorations: List[AbstractDecor]):
        self.decorations = decorations

    def find_decorations_by_decor_type(self, criterion: Set[DecorType]) -> List[AbstractDecor]:
        found_decorations = [decor for decor in self.decorations if decor.check_criterion(criterion)]
        return found_decorations
