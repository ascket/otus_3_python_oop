from src.figure import Figure
from typing import Union
import math


class Circle(Figure):
    def __init__(self, radius: Union[int, float]):
        super().__init__(radius)
        self.radius = radius


    @property
    def area(self):
        s = math.pi * pow(self.radius, 2)
        return round(s, 2)

    @property
    def perimeter(self):
        return self.__class__.perimeter_calculation(self.radius, circle=True)

    def __repr__(self):
        return super().__repr__() + f"(radius={self.radius})"
