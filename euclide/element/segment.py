from .base_element import BaseElement
from ..utils import segment_validation


class Segment(BaseElement):
    def __init__(self, symbol, explicit=True, alias=None, length=None, hook=None):
        _ =  segment_validation(symbol)

        super().__init__(symbol, explicit=explicit, alias=None, hook=hook)

        if len(symbol) == 1:
            self.name = symbol.lower()
        if len(symbol) == 2:
            self.name = symbol.upper()
            self.reversed_name = self.name[::-1]
