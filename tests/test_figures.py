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
    def test_circle_right_perimeter(self, _perimeter, _radius):
        c = Circle(_radius)
        assert c.perimeter == _perimeter

    def test_circle_wrong_perimeter(self, default_circle):
        assert default_circle.perimeter != 2

    def test_circle_add_area(self, default_triangle, default_circle, default_rectangle, default_square):
        assert default_circle.add_area(default_triangle) == 13.54
        assert default_circle.add_area(default_rectangle) == 18.57
        assert default_circle.add_area(default_square) == 16.57

    def test_circle_add_aredefault_circlea_error(self, default_circle):
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
