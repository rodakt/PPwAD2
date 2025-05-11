"""Testy jednostkowe dla funkcji z modułu simple_recurrence."""

import unittest
from simple_recurrence import maximum_rec, maximum_tail, fib_tail


class TestSimpleRecurrence(unittest.TestCase):
    """Testy jednostkowe dla funkcji z modułu simple_recurrence."""

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

    def test_maximum_tail_maxval(self):
        """Test dla funkcji maximum_tail() z podanym max_val."""
        seq = [1, 2, 3, 4, 5]
        self.assertEqual(maximum_tail(seq, 0), 5)
        seq = [5, 4, 3, 2, 1]
        self.assertEqual(maximum_tail(seq, 0), 5)
        seq = [1, 2, 3, 5, 4]
        self.assertEqual(maximum_tail(seq, 100), 100)

    def test_maximum_tail_isrecursive(self):
        """Test czy funkcja maximum_tail() jest rekurencyjna."""
        with self.assertRaises(
            RecursionError, msg="maximum_tail() nie jest rekurencyjna"
        ):
            maximum_tail(list(range(10000)))

    def test_fib_tail(self):
        """Test dla funkcji fib_tail()."""
        self.assertEqual(fib_tail(0), 0)
        self.assertEqual(fib_tail(1), 1)
        self.assertEqual(fib_tail(2), 1)
        self.assertEqual(fib_tail(3), 2)
        self.assertEqual(fib_tail(4), 3)
        self.assertEqual(fib_tail(5), 5)
        self.assertEqual(fib_tail(6), 8)
        self.assertEqual(fib_tail(7), 13)
        self.assertEqual(fib_tail(8), 21)
        self.assertEqual(fib_tail(9), 34)
        self.assertEqual(fib_tail(10), 55)
        self.assertEqual(fib_tail(11), 89)
        self.assertEqual(fib_tail(12), 144)
        self.assertEqual(fib_tail(13), 233)
        self.assertEqual(fib_tail(14), 377)
        self.assertEqual(fib_tail(15), 610)

    def test_fib_tail_large(self):
        """Test dla funkcji fib_tail() z dużą wartością n.

        # https://www.wolframalpha.com/input?i=fib+100
        """
        self.assertEqual(fib_tail(100), 354224848179261915075)

    def test_fib_tail_ab(self):
        """Test dla funkcji fib_tail() z podanymi a i b."""
        self.assertEqual(fib_tail(0, 0, 1), 0)
        self.assertEqual(fib_tail(5, -1, 1), 2)

    def test_fib_tail_isrecursive(self):
        """Test czy funkcja fib_tail() jest rekurencyjna."""
        with self.assertRaises(RecursionError, msg="fib_tail() nie jest rekurencyjna"):
            fib_tail(10000)


if __name__ == "__main__":
    unittest.main()
