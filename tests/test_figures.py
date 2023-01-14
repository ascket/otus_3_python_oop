from src.circle import Circle

class TestCircle:
    def test_circle(self):
        c = Circle(2)
        assert c.radius == 2
