from .base_element import BaseElement


class Segment(BaseElement):
    def __init__(self, tuple_of_points, explicit=True, alias=None, length=None, hook=None):
        if len(tuple_of_points) != 2:
            raise Exception("A Segment must be represented by two points")
        self.points = tuple_of_points
        name = self.points[0].name + self.points[1].name

        super().__init__(name, explicit=explicit, alias=alias, hook=hook)

        self.reversed_name = self.name[::-1]
