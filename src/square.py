from src.figure import Figure
from typing import Union


class Square(Figure):
    def __init__(self, sides: Union[int, float]):
        super().__init__(sides)
        self.sides = sides

    @property
    def area(self):
        return pow(self.sides, 2)

    @property
    def perimeter(self):
        return self.__class__.perimeter_calculation(4, self.sides)

    def __repr__(self):
        return super().__repr__() + f"(sides={self.sides})"
