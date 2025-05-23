"""Testy jednostkowe dla klasy OpenInterval z modułu open_interval"""

import unittest

from open_interval import OpenInterval


class TestOpenInterval(unittest.TestCase):
    """Testy jednostkowe dla klasy OpenInterval"""

    def test_len(self):
        """Testy dla metody __len__() klasy OpenInterval"""
        self.assertEqual(len(OpenInterval(1, 5)), 4)
        self.assertEqual(len(OpenInterval(1, 1)), 0)
        self.assertEqual(len(OpenInterval(5, 1)), 0)

    def test_bool(self):
        """Testy dla metody __bool__() klasy OpenInterval"""
        self.assertTrue(OpenInterval(1, 5))
        self.assertFalse(OpenInterval(1, 1))
        self.assertFalse(OpenInterval(5, 1))

    def test_repr(self):
        """Testy dla metody __repr__() klasy OpenInterval"""
        self.assertEqual(repr(OpenInterval(1, 5)), "OpenInterval(1, 5)")
        self.assertEqual(repr(OpenInterval(1, 1)), "OpenInterval(0, 0)")
        self.assertEqual(repr(OpenInterval(5, 1)), "OpenInterval(0, 0)")

    def test_str(self):
        """Testy dla metody __str__() klasy OpenInterval"""
        self.assertEqual(str(OpenInterval(1, 5)), "(1, 5)")
        self.assertEqual(str(OpenInterval(1, 1)), "\u2205")
        self.assertEqual(str(OpenInterval(5, 1)), "\u2205")

    def test_contains(self):
        """Testy dla metody __contains__() klasy OpenInterval"""
        self.assertTrue(3 in OpenInterval(1, 5))
        self.assertFalse(5 in OpenInterval(1, 5))
        self.assertFalse(1 in OpenInterval(1, 5))

    def test_eq(self):
        """Testy dla metody __eq__() klasy OpenInterval"""
        self.assertEqual(OpenInterval(1, 5), OpenInterval(1, 5))
        self.assertEqual(OpenInterval(10, 7), OpenInterval(4, -3))
        self.assertNotEqual(OpenInterval(1, 5), OpenInterval(1, 6))
        self.assertNotEqual(OpenInterval(1, 5), OpenInterval(0, 5))

    def test_and(self):
        """Testy dla metody __and__() klasy OpenInterval"""
        self.assertEqual(OpenInterval(1, 5) & OpenInterval(3, 7), OpenInterval(3, 5))
        self.assertEqual(OpenInterval(1, 5) & OpenInterval(6, 7), OpenInterval(0, 0))

    def test_or(self):
        """Testy dla metody __or__() klasy OpenInterval"""
        self.assertEqual(OpenInterval(1, 5) | OpenInterval(3, 7), OpenInterval(1, 7))

    def test_nonoverlapping_or(self):
        """Test dla metody __or__() klasy OpenInterval dla niezachodzących przedziałów"""
        with self.assertRaises(NotImplementedError) as context:
            OpenInterval(1, 5) | OpenInterval(6, 7)
        self.assertEqual(str(context.exception), "Przedziały nie zachodzą na siebie")


if __name__ == "__main__":
    unittest.main()
