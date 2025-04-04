"""Testy jednostkowe dla funkcji z modułu polygons"""

import unittest
from fractions import Fraction as F
from math import sqrt

from polygons import polygon, regular_polygon
from logo_turtle import create_turtle


class TestPolygon(unittest.TestCase):
    """Testy jednostkowe dla funkcji polygon()"""

    def test_polygon_nsides(self):
        """Test liczby wierzchołków wielokąta"""
        turtle = create_turtle()
        n = polygon(turtle, 90, 1)
        self.assertEqual(n, 4, "kwadrat")
        turtle = create_turtle()
        n = polygon(turtle, 144, 1)
        self.assertEqual(n, 5, "gwieździsty pięciokąt")
        turtle = create_turtle()
        n = polygon(turtle, 72, 1)
        self.assertEqual(n, 5, "pięciokąt")
        turtle = create_turtle()
        n = polygon(turtle, F(360, 7), 1)
        self.assertEqual(n, 7, "siedmiokąt")

    def test_polygon_position(self):
        """Test pozycji dla kąta 90 stopni"""
        turtle = create_turtle()
        polygon(turtle, 90, 1)
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        for (x1, y1), (x2, y2) in zip(turtle["position"], vertices):
            self.assertAlmostEqual(x1, x2)
            self.assertAlmostEqual(y1, y2)

    def test_polygon_angle_type(self):
        """Test typu parametru kąt"""
        turtle = create_turtle()
        with self.assertRaises(TypeError) as cm:
            polygon(turtle, 45.0, 1)
        self.assertEqual(
            str(cm.exception), "kąt musi być liczbą całkowitą lub wymierną"
        )

    def test_polygon_full_angle(self):
        """Test zgłaszania wyjątku dla kąta pełnego"""
        turtle = create_turtle()
        with self.assertRaises(ValueError) as cm:
            polygon(turtle, 0, 1)
        self.assertEqual(
            str(cm.exception),
            "kąt musi być liczba wymierną nie będącą wielokrotnością 360",
        )
        with self.assertRaises(ValueError) as cm:
            polygon(turtle, 360, 1)
        self.assertEqual(
            str(cm.exception),
            "kąt musi być liczba wymierną nie będącą wielokrotnością 360",
        )
        with self.assertRaises(ValueError) as cm:
            polygon(turtle, -720, 1)
        self.assertEqual(
            str(cm.exception),
            "kąt musi być liczba wymierną nie będącą wielokrotnością 360",
        )
        with self.assertRaises(ValueError) as cm:
            polygon(turtle, F(360, 1), 1)
        self.assertEqual(
            str(cm.exception),
            "kąt musi być liczba wymierną nie będącą wielokrotnością 360",
        )


class TestRegularPolygon(unittest.TestCase):
    """Testy jednostkowe dla funkcji regular_polygon()"""

    def test_regular_polygon(self):
        """Test wielokąta foremnego"""
        turtle = create_turtle()
        regular_polygon(turtle, 3, 1)
        vertices = [(0, 0), (1, 0), (0.5, sqrt(3) / 2), (0, 0)]
        for (x1, y1), (x2, y2) in zip(turtle["position"], vertices):
            self.assertAlmostEqual(x1, x2)
            self.assertAlmostEqual(y1, y2)


if __name__ == "__main__":
    unittest.main()
