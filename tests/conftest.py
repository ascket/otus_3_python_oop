import pytest
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle
from src.rectangle import Rectangle


@pytest.fixture(scope="class")
def triangle_values():
    return {
        "side_a": 1,
        "side_b": 2,
        "side_c": 2
    }


@pytest.fixture(scope="class")
def rectanlge_values():
    return {
        "side_a": 2,
        "side_b": 3
    }


@pytest.fixture(scope="class")
def default_rectangle(rectanlge_values):
    return Rectangle(**rectanlge_values)


@pytest.fixture(scope="class")
def default_triangle(triangle_values):
    return Triangle(**triangle_values)


@pytest.fixture(scope="class")
def default_circle():
    return Circle(2)


@pytest.fixture(scope="class")
def default_square():
    return Square(2)
