from .base_element import BaseElement
from ..utils import point_validation


class Point(BaseElement):
    def __init__(self, symbol, explicit=True, alias=None, coordinates=None, hook=None):
        _ = point_validation(symbol)

        super().__init__(symbol, explicit=explicit, alias=alias, hook=hook)

        self.name = symbol.upper()
        self.coordinates = coordinates
