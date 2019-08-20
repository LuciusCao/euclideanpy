from .base_element import BaseElement
from .point import Point
from .segment import Segment
from ..validations import angle_validation


class Angle(BaseElement):
    def __init__(self, symbol, measure=None, hook=None):
        _ = angle_validation(symbol)

        super().__init__(symbol, hook=hook)

        if len(symbol) == 1:
            if symbol.isnumeric():
                self.name = self.symbol = symbol
            else:
                self.name = self.symbol = symbol.upper()
        elif len(symbol) == 3:
            self.name = self.symbol = symbol.upper()
            self.reversed_name = self.name[::-1]

        self.measure = measure
        self.points = []
        self.segments = []

    def append_point(self, point):
        if not isinstance(point, Point):
            raise Exception('point must be an instance of Point')

        self.points.append(point)

    def append_segment(self, segment):
        if not isinstance(segment, Segment):
            raise Exception('segment must be an instance of Segment')

        self.segments.append(segment)
