from .base_element import BaseElement


class Point(BaseElement):
    def __init__(self, symbol, explicit=True, coordinates=None, hook=None):
        if len(symbol) != 1:
            raise Exception("A Point must be represented by a single letter")
        super().__init__(symbol, explicit=explicit, alias=None, hook=hook)

        self.name = symbol.upper()
