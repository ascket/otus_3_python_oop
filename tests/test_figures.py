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
    def test_circle_radius(self, radius_value, expect_value):
        c = Circle(radius=radius_value)
        assert c.radius == expect_value


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
    def test_false_triangle(self, _side_a, _side_b, _side_c):
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
    def test_triange_false_values(self, _side_a, _side_b, _side_c):
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
    def test_triangle_false_area(self, _side_a, _side_b, _side_c, _area):
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
    def test_triangle_false_perimeter(self, _side_a, _side_b, _side_c, _perimeter):
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
