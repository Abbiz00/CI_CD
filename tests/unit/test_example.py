from src.example import square, multiply, add
import pytest


@pytest.mark.unit
def test_square():

    # Arrange
    test_data = 10
    expected = 100

    # Act
    actual = square(test_data)

    # Assert
    assert actual == expected


@pytest.mark.unit
def test_add():

    # Assert
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


@pytest.mark.unit
def test_divide():

    # Assert
    assert multiply(10, 2) == 20
