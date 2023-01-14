from figure import Figure
from typing import Union


class Rectangle(Figure):
    def __init__(self, side_a: Union[int, float], side_b: Union[int, float]):
        super().__init__(side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return self.__class__.perimeter_calculation(2, self.side_a, self.side_b)

    def __repr__(self):
        return super().__repr__() + f"(side_a={self.side_a}, side_b={self.side_b})"


if __name__ == "__main__":
    r = Rectangle(1, 2)
    print(r)
    print(r.perimeter)
    print(r.area)
