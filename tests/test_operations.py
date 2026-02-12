import pytest
from app.operation.operations import Operations


# ADD
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected


# SUBTRACT
@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (10, 4, 6),
])
def test_subtract(a, b, expected):
    assert Operations.subtract(a, b) == expected


# MULTIPLY
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (4, 5, 20),
])
def test_multiply(a, b, expected):
    assert Operations.multiply(a, b) == expected


# DIVIDE SUCCESS
def test_divide_success():
    assert Operations.divide(9, 3) == 3


# DIVIDE BY ZERO
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(5, 0)