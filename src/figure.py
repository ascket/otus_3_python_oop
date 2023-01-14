from typing import Union
import math


class Figure():
    def __init__(self, *values: Union[int, float]):
        for value in values:
            self.__class__.valid_value(value)

    @staticmethod
    def valid_value(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Value must be a positive integer or float. {value} is wrong.")

    @staticmethod
    def perimeter_calculation(sides_or_radius: int = 1, *values: Union[int, float], circle=False):
        if circle:
            s = 2 * math.pi * sides_or_radius
            return round(s, 2)
        else:
            s = sides_or_radius * sum(values)
            return round(s, 2)

    @property
    def area(self):
        pass

    @property
    def perimeter(self):
        return self.__class__.perimeter_calculation()

    @property
    def name(self):
        return f"{self.__class__.__name__}"

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"Figure must be a type 'Figure'")
        return figure.area + self.area

    def __repr__(self):
        return self.name
