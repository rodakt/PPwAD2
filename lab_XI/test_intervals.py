"""Testy jednostkowe dla klasy Intervals z modułu intervals"""

import unittest

from intervals import Intervals


class TestIntervals(unittest.TestCase):
    """Testy jednostkowe dla klasy Intervals"""

    def setUp(self):
        try:
            self.i1 = Intervals((1, 5))
            self.i2 = Intervals((3, 7))
            self.i3 = Intervals((5, 9))
            self.i4 = Intervals((6, 7))
            self.i5 = Intervals((8, 9))
            self.i6 = Intervals((10, 20))
        except Exception as e:
            self.fail(f"Nie udało się utworzyć obiektu klasy Intervals: {e}")

    def test_1_eq(self):
        """Testy dla metody __eq__() klasy Intervals"""
        self.assertEqual(Intervals(), Intervals((0, 0)))
        self.assertEqual(Intervals((1, 5), (3, 7)), Intervals((1, 7)))
        self.assertEqual(Intervals((1, 5), (6, 7)), Intervals((6, 7), (1, 5)))

    def test_2_and(self):
        """Testy dla metody __and__() klasy Intervals"""
        self.assertEqual(self.i1 & self.i2, Intervals((3, 5)))
        self.assertEqual(self.i1 & self.i3, Intervals())
        self.assertEqual(self.i2 & self.i4, self.i4)
        self.assertEqual(self.i2 & self.i4 & self.i4, self.i4)

    def test_3_or(self):
        """Testy dla metody __or__() klasy Intervals"""
        # self.i1 = Intervals((1, 5))
        # self.i2 = Intervals((3, 7))
        # self.i3 = Intervals((5, 9))
        # self.i4 = Intervals((6, 7))
        # self.i5 = Intervals((8, 9))
        # self.i6 = Intervals((10, 20))
        self.assertEqual(self.i1 | self.i2, Intervals((1, 7)))
        self.assertEqual(self.i1 | self.i3, Intervals((1, 5), (5, 9)))
        self.assertEqual(self.i2 | self.i4 | self.i5, Intervals((3, 7), (8, 9)))
        self.assertEqual(
            self.i1 | self.i2 | self.i3 | self.i4 | self.i5 | self.i6,
            Intervals((1, 9), (10, 20)),
        )

    def test_4_bool(self):
        """Testy dla metody __bool__() klasy Intervals"""
        self.assertFalse(Intervals())
        self.assertFalse(Intervals((5, 1), (7, 3)))
        self.assertTrue(Intervals((1, 5), (3, 7)))
        self.assertTrue(Intervals((1, 5), (6, 7)))

    def test_5_contains(self):
        """Testy dla metody __contains__() klasy Intervals"""
        intervals = self.i1 | self.i3  # (1, 5) u (5, 9)
        self.assertTrue(4 in intervals)
        self.assertFalse(5 in intervals)
        self.assertFalse(1 in intervals)
        self.assertTrue(6 in intervals)

    def test_6_repr(self):
        """Testy dla metody __repr__() klasy Intervals"""
        self.assertEqual(repr(Intervals()), "Intervals(OpenInterval(0, 0))")
        self.assertEqual(
            repr(Intervals((1, 5), (3, 7))),
            "Intervals(OpenInterval(1, 7))",
        )
        self.assertEqual(
            repr(Intervals((1, 5), (6, 7))),
            "Intervals(OpenInterval(1, 5), OpenInterval(6, 7))",
        )

    def test_7_str(self):
        """Testy dla metody __str__() klasy Intervals"""
        self.assertEqual(str(Intervals()), "\u2205")
        self.assertEqual(
            str(
                Intervals((1, 5), (3, 7)),
            ),
            "(1, 7)",
        )
        self.assertEqual(
            str(
                Intervals((1, 5), (6, 7)),
            ),
            "(1, 5) \u222A (6, 7)",
        )

    def test_8_len(self):
        """Testy dla metody __len__() klasy Intervals"""
        self.assertEqual(len(Intervals()), 0)
        self.assertEqual(len(Intervals((1, 5), (3, 7))), 6)
        self.assertEqual(len(Intervals((1, 5), (6, 7))), 5)


class TestIntegrationTests(unittest.TestCase):
    """Testy integracyjne dla klasy Intervals"""

    def setUp(self):
        try:
            self.i1 = Intervals((1, 5))
            self.i2 = Intervals((3, 7))
            self.i3 = Intervals((5, 9))
            self.i4 = Intervals((6, 7))
            self.i5 = Intervals((8, 9))
            self.i6 = Intervals((10, 20))
        except Exception as e:
            self.fail(f"Nie udało się utworzyć obiektu klasy Intervals: {e}")

    def test_1(self):
        """Testy dla wyrażeń łaczących sumy i przecięcia"""
        self.assertEqual(self.i1 & self.i2 | self.i3, Intervals((3, 5), (5, 9)))
        self.assertEqual(
            (self.i1 | self.i5) & (self.i2 | self.i4),
            (self.i1 & self.i2)
            | (self.i1 & self.i4)
            | (self.i5 & self.i2)
            | (self.i5 & self.i4),
        )


if __name__ == "__main__":
    unittest.main()
