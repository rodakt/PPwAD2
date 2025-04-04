"""Moduł zawierający testy jednostkowe dla modułu logo_turtle.py"""

import unittest
import math
from logo_turtle import create_turtle, left, right, forward, to_csv


class TestCreateTurtle(unittest.TestCase):
    """Testy jednostkowe dla funkcji create_turtle()"""

    def test_create_turtle(self):
        """Sprawdza wywołanie create_turtle() bez parametrów"""
        turtle = create_turtle()
        self.assertEqual(turtle["position"], [(0, 0)])
        self.assertEqual(turtle["azimuth"], 0)
        self.assertEqual(turtle["name"], "")

    def test_create_turtle_with_params(self):
        """Sprawdza wywołanie create_turtle() z parametrami"""
        turtle = create_turtle(x=1, y=2, azimuth=3, name="Tolek")
        self.assertEqual(turtle["position"], [(1, 2)])
        self.assertEqual(turtle["azimuth"], 3)
        self.assertEqual(turtle["name"], "Tolek")


class TestLeftRight(unittest.TestCase):
    """Testy jednostkowe dla funkcji left() i right()"""

    def test_left(self):
        """Sprawdza wywołanie left()"""
        turtle = create_turtle(azimuth=0)
        left(turtle, 90)
        self.assertEqual(turtle["azimuth"], 90)
        left(turtle, 90)
        self.assertEqual(turtle["azimuth"], 180)

    def test_right(self):
        """Sprawdza wywołanie right()"""
        turtle = create_turtle(azimuth=0)
        right(turtle, 90)
        self.assertEqual(turtle["azimuth"], -90)
        right(turtle, 90)
        self.assertEqual(turtle["azimuth"], -180)


class TestForward(unittest.TestCase):
    """Testy jednostkowe dla funkcji forward()"""

    def test_forward(self):
        """Sprawdza wywołanie forward()"""
        turtle = create_turtle(x=0, y=0, azimuth=0)
        forward(turtle, 1)
        self.assertEqual(turtle["position"], [(0, 0), (1, 0)])
        forward(turtle, 1)
        self.assertEqual(turtle["position"], [(0, 0), (1, 0), (2, 0)])

    def test_forward_with_azimuth(self):
        """Test ruchu po krawędziach trójkąta równobocznego"""
        turtle = create_turtle(x=0, y=0, azimuth=0)
        forward(turtle, 1)
        self.assertEqual(turtle["position"], [(0, 0), (1, 0)])
        left(turtle, 120)
        forward(turtle, 1)
        x, y = turtle["position"][-1]
        self.assertAlmostEqual(x, 0.5)
        self.assertAlmostEqual(y, math.sqrt(3) / 2)
        left(turtle, 120)
        forward(turtle, 1)
        x, y = turtle["position"][-1]
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 0)


if __name__ == "__main__":
    unittest.main()
