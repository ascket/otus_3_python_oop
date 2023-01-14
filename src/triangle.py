from figure import Figure
from typing import Union


class Triangle(Figure):
    def __init__(self, side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]):
        super().__init__(side_a, side_c, side_b)

        sides = {"side a": side_a, "side b": side_b, "side c": side_c} #этот словарь сделан для вывода названия строны в ошибке при проверке существования треугольника

        sum_sides = sum(sides.values())
        for key, value in sides.items():
            sum_sides_minus = sum_sides - value
            if value >= sum_sides_minus:
                raise ValueError(f"{key} ({value}) must be less than {sum_sides_minus} (sum of another two sides)")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        p = self.perimeter / 2
        s = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return round(s, 2)

    @property
    def perimeter(self):
        return self.__class__.perimeter_calculation(1, self.side_a, self.side_b, self.side_c)

    def __repr__(self):
        return super().__repr__() + f"(side_a={self.side_a}, side_b={self.side_b}, side_c={self.side_c})"


if __name__ == "__main__":
    tr = Triangle(5, 5, 2)
    print(tr)
    print(tr.perimeter)
    print(tr.area)
    print(tr.name)
