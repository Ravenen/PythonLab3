import json
from typing import Set

from sqlalchemy.ext.hybrid import hybrid_property

from app import db, ma
from model.abstract_decor import AbstractDecor
from model.decor_type import DecorType


class Garland(AbstractDecor, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(32))
    price_in_uah = db.Column(db.Float)
    _decor_type = db.Column('decor_type', db.String(255), default='[]', server_default='[]')
    length_in_metres = db.Column(db.Float)
    is_natural = db.Column(db.Boolean)

    def __init__(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None,
                 length_in_metres: float = None, is_natural: bool = None):
        super(Garland, self).__init__(color, price_in_uah, decor_type)
        self.length_in_metres = length_in_metres
        self.is_natural = is_natural

    def set_fields(self, color: str = None, price_in_uah: float = None, decor_type: Set[DecorType] = None,
                   length_in_metres: float = None, is_natural: bool = None):
        super(Garland, self).set_fields(color, price_in_uah, decor_type)
        self.length_in_metres = length_in_metres
        self.is_natural = is_natural

    def __repr__(self) -> str:
        return f"Garland[{super().__repr__()}, length: {self.length_in_metres}, is_natural: {self.is_natural}"

    @hybrid_property
    def decor_type(self):
        return json.loads(self._decor_type)

    @decor_type.setter
    def decor_type(self, decor_type):
        self._decor_type = json.dumps(list(decor_type))


class GarlandSchema(ma.Schema):
    class Meta:
        fields = ('id', 'color', 'price_in_uah', 'decor_type', 'length_in_metres', 'is_natural')
