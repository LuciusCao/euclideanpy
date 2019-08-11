import pytest

from euclide.element.point import Point
from euclide.element.segment import Segment


@pytest.mark.parametrize("tuple_of_points, expected", [
    ((Point("A"), Point("B")), "AB")
])
def test_initialization(tuple_of_points, expected):
    segment = Segment(tuple_of_points)
    assert segment.name == expected


@pytest.mark.parametrize("tuple_of_points", [
    ((Point("A"),)),
    ((Point("B"), Point("A"), Point("C")))
])
def test_initialization_failure(tuple_of_points):
    with pytest.raises(Exception):
        point = Segment(tuple_of_points)
