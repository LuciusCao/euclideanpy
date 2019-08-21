from .base_element import BaseElement
from .point import Point


class Line(BaseElement):
    def __init__(self, tuple_of_points, explicit=True, hook=None):
        if len(tuple_of_points) != 2:
            raise Exception("A Line must be represented by two letters")
        self.points = tuple_of_points
        name = self.points[0].name + self.points[1].name

        super().__init__(name, explicit=explicit, hook=hook)

        self.reversed_name = self.name[::-1]
