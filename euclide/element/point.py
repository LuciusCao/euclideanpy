from .base_element import BaseElement
from ..validations import point_validation


class Point(BaseElement):
    def __init__(self, symbol, explicit=True, coordinates=None, hook=None):
        _ = point_validation(symbol)

        super().__init__(symbol, explicit=explicit, hook=hook)

        self.name = symbol.upper()
        self.symbol = symbol.upper()
        self.coordinates = coordinates
