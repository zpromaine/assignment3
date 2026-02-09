import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]

# ---------------------------------------------
# Unit Tests for the 'addition' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6),
        (-2.5, 3.5, 1.0),
    ],
    ids=[
        "add_two_positive_inters",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)
def test_addition(a: Number, b:Number, excpected: Number) -> None:
    result = Operations.addition(a, b)

    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {results}"


@pytest.mark.parametrize

# ---------------------------------------------
# Unit Tests for the 'subtraction' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, excpected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ]
    ids=[
        "subtract_two_positive_inters",
        "subtract_two_zeros",
        "subtract_negative_from negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
      result = Operations.subtraction(a, b)

    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {results}"
