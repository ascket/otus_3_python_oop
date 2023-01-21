import pytest
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle
from src.rectangle import Rectangle


class TestCircle:
    @pytest.mark.parametrize(
        "radius_value, expect_value",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4)
        ]
    )
    def test_circle_right_radius(self, radius_value, expect_value):
        c = Circle(radius=radius_value)
        assert c.radius == expect_value

    @pytest.mark.parametrize(
        "_radius",
        [0, -1]
    )
    def test_circle_wrong_radius(self, _radius):
        match_regex = r"Value must be a positive integer or float. .* is wrong."
        with pytest.raises(ValueError, match=match_regex):
            Circle(_radius)

    def test_circle_repr(self, default_circle):
        assert repr(default_circle) == "Circle(radius=2)"

    def test_circle_name(self, default_circle):
        assert default_circle.name == "Circle"

    @pytest.mark.parametrize(
        "_radius, _area",
        [
            (1, 3.14),
            (5, 78.54),
            (20, 1256.64)
        ]
    )
    def test_circle_area(self, _radius, _area):
        c = Circle(_radius)
        assert c.area == _area

    def test_circle_wrong_area(self, default_circle):
        assert default_circle.area != 12

    @pytest.mark.parametrize(
        "_radius, _perimeter",
        [
            (1, 6.28),
            (5, 31.42),
            (20, 125.66)
        ]
    )
    def test_circle_right_perimeter(self, _radius, _perimeter):
        c = Circle(_radius)
        assert c.perimeter == _perimeter

    def test_circle_wrong_perimeter(self, default_circle):
        assert default_circle.perimeter != 2

    def test_circle_add_area(self, default_triangle, default_circle, default_rectangle, default_square):
        assert default_circle.add_area(default_triangle) == 13.54
        assert default_circle.add_area(default_rectangle) == 18.57
        assert default_circle.add_area(default_square) == 16.57

    def test_circle_add_area_error(self, default_circle):
        with pytest.raises(ValueError) as err:
            default_circle.add_area(3)
        assert "Variable must be a type 'Figure'" == str(err.value)


class TestTriangle:
    def test_triangle_values(self, triangle_values, default_triangle):
        for attr in triangle_values:
            assert getattr(default_triangle, attr) == triangle_values.get(attr)

    def test_triangle_repr(self, default_triangle):
        assert repr(default_triangle) == "Triangle(side_a=1, side_b=2, side_c=2)"

    def test_triangle_name(self, default_triangle):
        assert default_triangle.name == "Triangle"

    @pytest.mark.parametrize(
        "_side_a, _side_b, _side_c",
        [
            (10, 2, 3),
            (2, 10, 3),
            (2, 3, 10),
            (10, 5, 5)
        ]
    )
    def test_wrong_triangle(self, _side_a, _side_b, _side_c):
        with pytest.raises(ValueError) as err:
            Triangle(_side_a, _side_b, _side_c)
        assert "(sum of another two sides)" in str(err.value)

    @pytest.mark.parametrize(
        "_side_a, _side_b, _side_c",
        [
            (0, 2, 3),
            (2, 0, 3),
            (2, 3, 0),
            (-1, 2, 3),
            (2, -1, 3),
            (2, 3, -1)
        ]
    )
    def test_triange_wrong_values(self, _side_a, _side_b, _side_c):
        match_regex = r"Value must be a positive integer or float. .* is wrong."
        with pytest.raises(ValueError, match=match_regex):
            Triangle(_side_a, _side_b, _side_c)

    def test_triangle_error_values(self):
        with pytest.raises(ValueError) as err:
            Triangle(10, 2, 3)
        assert "side a (10) must be less than 5 (sum of another two sides)" == str(err.value)

    @pytest.mark.parametrize(
        "_side_a, _side_b, _side_c, _area",
        [
            (1, 2, 2, 0.97),
            (5, 3, 4, 6),
            (20, 10, 20, 96.82),

        ]
    )
    def test_triangle_right_area(self, _side_a, _side_b, _side_c, _area):
        tr = Triangle(_side_a, _side_b, _side_c)
        assert tr.area == _area

    @pytest.mark.parametrize(
        "_side_a, _side_b, _side_c, _area",
        [
            (1, 2, 2, 2),
            (5, 3, 4, 7),
            (20, 10, 20, 95),

        ]
    )
    def test_triangle_wrong_area(self, _side_a, _side_b, _side_c, _area):
        tr = Triangle(_side_a, _side_b, _side_c)
        assert tr.area != _area

    @pytest.mark.parametrize(
        "_side_a, _side_b, _side_c, _perimeter",
        [
            (1, 2, 2, 5),
            (5, 3, 4, 12),
            (20, 10, 20, 50),

        ]
    )
    def test_triangle_right_perimeter(self, _side_a, _side_b, _side_c, _perimeter):
        tr = Triangle(_side_a, _side_b, _side_c)
        assert tr.perimeter == _perimeter

    @pytest.mark.parametrize(
        "_side_a, _side_b, _side_c, _perimeter",
        [
            (1, 2, 2, 25),
            (5, 3, 4, 2),
            (20, 10, 20, 5),

        ]
    )
    def test_triangle_wrong_perimeter(self, _side_a, _side_b, _side_c, _perimeter):
        tr = Triangle(_side_a, _side_b, _side_c)
        assert tr.perimeter != _perimeter

    def test_triangle_add_area(self, default_triangle, default_circle, default_rectangle, default_square):
        assert default_triangle.add_area(default_circle) == 13.54
        assert default_triangle.add_area(default_rectangle) == 6.97
        assert default_triangle.add_area(default_square) == 4.97

    def test_triangle_add_area_error(self, default_triangle):
        with pytest.raises(ValueError) as err:
            default_triangle.add_area(3)
        assert "Variable must be a type 'Figure'" == str(err.value)


class TestRectangle:
    @pytest.mark.parametrize(
        "_side_a, _side_b",
        [
            (1, 2),
            (20, 30),
            (3, 8),
            (10, 15),
            (7, 7)
        ]
    )
    def test_rectangle_right_value(self, _side_a, _side_b):
        c = Rectangle(_side_a, _side_b)
        assert c.side_b == _side_b
        assert c.side_a == _side_a

    @pytest.mark.parametrize(
        "_side_a, _side_b",
        [
            (-1, 3),
            (3, -1),
            (0, 3),
            (3, 0)
        ]
    )
    def test_rectangle_wrong_values(self, _side_a, _side_b):
        match_regex = r"Value must be a positive integer or float. .* is wrong."
        with pytest.raises(ValueError, match=match_regex):
            Rectangle(_side_a, _side_b)

    def test_rectangle_repr(self, default_rectangle):
        assert repr(default_rectangle) == "Rectangle(side_a=2, side_b=3)"

    def test_rectangle_name(self, default_rectangle):
        assert default_rectangle.name == "Rectangle"

    @pytest.mark.parametrize(
        "_side_a, _side_b, _area",
        [
            (1, 2, 2),
            (5, 10, 50),
            (20, 20, 400),
            (2.998, 3, 8.99),
            (2.5, 1.5, 3.75),
            (3, 2.998, 8.99)
        ]
    )
    def test_rectangle_area(self, _side_a, _side_b, _area):
        rc = Rectangle(_side_a, _side_b)
        assert rc.area == _area

    def test_rectangle_wrong_area(self, default_rectangle):
        assert default_rectangle.area != 12

    @pytest.mark.parametrize(
        "_side_a, _side_b, _perimeter",
        [
            (1, 2, 6),
            (5, 10, 30),
            (20, 20, 80),
            (2.43, 3, 10.86),
            (2.5, 1.5, 8),
            (3, 2.43, 10.86)
        ]
    )
    def test_rectangle_right_perimeter(self, _side_a, _side_b, _perimeter):
        rc = Rectangle(_side_a, _side_b)
        assert rc.perimeter == _perimeter

    def test_rectangle_wrong_perimeter(self, default_rectangle):
        assert default_rectangle.perimeter != 2

    def test_rectangle_add_area(self, default_triangle, default_circle, default_rectangle, default_square):
        assert default_rectangle.add_area(default_triangle) == 6.97
        assert default_rectangle.add_area(default_circle) == 18.57
        assert default_rectangle.add_area(default_square) == 10

    def test_rectangle_add_area_error(self, default_rectangle):
        with pytest.raises(ValueError) as err:
            default_rectangle.add_area(3)
        assert "Variable must be a type 'Figure'" == str(err.value)


class TestSquare:
    @pytest.mark.parametrize(
        "_sides, expect_value",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4)
        ]
    )
    def test_square_right_value(self, _sides, expect_value):
        sq = Square(_sides)
        assert sq.sides == expect_value

    @pytest.mark.parametrize(
        "_sides",
        [0, -1]
    )
    def test_square_wrong_value(self, _sides):
        match_regex = r"Value must be a positive integer or float. .* is wrong."
        with pytest.raises(ValueError, match=match_regex):
            Square(_sides)

    def test_square_repr(self, default_square):
        assert repr(default_square) == "Square(sides=2)"

    def test_square_name(self, default_square):
        assert default_square.name == "Square"

    @pytest.mark.parametrize(
        "_sides, _area",
        [
            (1, 1),
            (5, 25),
            (20, 400)
        ]
    )
    def test_square_area(self, _sides, _area):
        sq = Square(_sides)
        assert sq.area == _area

    def test_square_wrong_area(self, default_square):
        assert default_square.area != 12

    @pytest.mark.parametrize(
        "_sides, _perimeter",
        [
            (1, 4),
            (5, 20),
            (20, 80)
        ]
    )
    def test_square_right_perimeter(self, _sides, _perimeter):
        sq = Square(_sides)
        assert sq.perimeter == _perimeter

    def test_square_wrong_perimeter(self, default_square):
        assert default_square.perimeter != 20

    def test_square_add_area(self, default_triangle, default_circle, default_rectangle, default_square):
        assert default_square.add_area(default_triangle) == 4.97
        assert default_square.add_area(default_rectangle) == 10
        assert default_square.add_area(default_circle) == 16.57

    def test_square_add_area_error(self, default_square):
        with pytest.raises(ValueError) as err:
            default_square.add_area(3)
        assert "Variable must be a type 'Figure'" == str(err.value)
