from .base_element import BaseElement
from .point import Point
from ..validations import segment_validation


class Segment(BaseElement):
    def __init__(self, symbol, explicit=True, length=None, hook=None):
        _ = segment_validation(symbol)

        super().__init__(symbol, explicit=explicit, hook=hook)

        if len(symbol) == 1:
            self.name = symbol.lower()
            self.symbol = symbol.lower()
        elif len(symbol) == 2:
            self.name = symbol.upper()
            self.symbol = symbol.upper()
            self.reversed_name = self.name[::-1]

        self.points = []

    def append_point(self, point):
        if not isinstance(point, Point):
            raise Exception('point must be an instance of Point')

        self.points.append(point)
        return self.points
