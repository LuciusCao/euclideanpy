import pytest

from euclide.element.point import Point


@pytest.mark.parametrize("symbol, expected", [
    ("A", "A"),
    ("a", "A"),
])
def test_initialization(symbol, expected):
    point = Point(symbol)
    assert point.name == expected


@pytest.mark.parametrize("symbol", [
    ("1",),
    ("abc"),
    ("ABC"),
    ("AbC"),
])
def test_initialization_failure(symbol):
    with pytest.raises(Exception):
        point = Point(symbol)
