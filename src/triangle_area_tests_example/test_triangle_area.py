"""Testy jednostkowe dla modułu triangle_area"""

import unittest
from math import sqrt

from triangle_area import is_triangle, triangle_area


class TestTriangleArea(unittest.TestCase):
    """Testy jednostkowe dla funkcji is_triangle() i triangle_area()."""

    def test_is_triangle(self):
        """Testy pozytywne dla funkcji is_triangle()."""
        self.assertTrue(is_triangle(3, 4, 5), msg="3, 4, 5 jest trójkątem prostokątnym")
        self.assertTrue(is_triangle(1, 1, 1), msg="Trójkąt równoboczny")
        self.assertTrue(
            is_triangle(5, 2, 3), msg="5, 2, 3 jest trójkątem zdegenerowanym"
        )
        self.assertTrue(
            is_triangle(100, 100, sqrt(2) * 100),
            msg="100, 100, 100√2 jest trójkątem prostokątnym",
        )

    def test_is_not_triangle(self):
        """Testy negatywne dla funkcji is_triangle()."""
        self.assertFalse(is_triangle(1, 1, 3), msg="1, 1, 3 nie jest trójkątem")
        self.assertFalse(is_triangle(-5, 2, 3), msg="-5, 2, 3 nie jest trójkątem")
        self.assertFalse(is_triangle(1, -1, -3), msg="1, -1, -3 nie jest trójkątem")

    def test_triangle_area(self):
        """Testy funkcji triangle_area()."""
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6, msg="Pole trójkąta 3, 4, 5")
        self.assertAlmostEqual(
            triangle_area(1, 1, 1), sqrt(3) / 4, msg="Pole trójkąta 1, 1, 1"
        )
        self.assertAlmostEqual(triangle_area(5, 2, 3), 0, msg="Pole trójkąta 5, 2, 3")
        self.assertAlmostEqual(
            triangle_area(100, 100, sqrt(2) * 100),
            5000,
            msg="Pole trójkąta 100, 100, 100√2",
        )

    def test_triangle_area_exceptions(self):
        """Testy wyjątków dla funkcji triangle_area()."""
        with self.assertRaises(ValueError) as e:
            triangle_area(1, 1, 3)
        self.assertEqual(
            str(e.exception), "Nie można zbudować trójkąta o bokach 1, 1, 3"
        )

        with self.assertRaises(ValueError) as e:
            triangle_area(-5, 2, 3)
        self.assertEqual(
            str(e.exception), "Nie można zbudować trójkąta o bokach -5, 2, 3"
        )


if __name__ == "__main__":
    unittest.main()
