"""Testy jednostkowe dla funkcji maximum_rec i maximum_tail z modułu maximum."""

import unittest
from maximum import maximum_rec, maximum_tail


class TestMaximum(unittest.TestCase):

    def test_maximum_rec(self):
        """Test dla funkcji maximum_rec()."""
        seq = [1, 2, 3, 4, 5]
        self.assertEqual(maximum_rec(seq), 5)
        seq = [5, 4, 3, 2, 1]
        self.assertEqual(maximum_rec(seq), 5)
        seq = [1, 2, 3, 5, 4]
        self.assertEqual(maximum_rec(seq), 5)
        seq = [1]
        self.assertEqual(maximum_rec(seq), 1)
        with self.assertRaises(ValueError):
            maximum_rec([])

    def test_maximum_rec_isrecursive(self):
        """Test czy funkcja maximum_rec() jest rekurencyjna."""
        with self.assertRaises(
            RecursionError, msg="maximum_rec() nie jest rekurencyjna"
        ):
            maximum_rec(list(range(10000)))

    def test_maximum_tail(self):
        """Test dla funkcji maximum_tail()."""
        seq = [1, 2, 3, 4, 5]
        self.assertEqual(maximum_tail(seq), 5)
        seq = [5, 4, 3, 2, 1]
        self.assertEqual(maximum_tail(seq), 5)
        seq = [1, 2, 3, 5, 4]
        self.assertEqual(maximum_tail(seq), 5)
        seq = [1]
        self.assertEqual(maximum_tail(seq), 1)
        with self.assertRaises(ValueError):
            maximum_tail([])

    def test_maximum_tail_isrecursive(self):
        """Test czy funkcja maximum_tail() jest rekurencyjna."""
        with self.assertRaises(
            RecursionError, msg="maximum_tail() nie jest rekurencyjna"
        ):
            maximum_tail(list(range(10000)))


if __name__ == "__main__":
    unittest.main()
