"""Testy jednostkowe dla modułu infinite_sequences."""

import unittest
from infinite_sequences import Squares, Fib


class TestSquares(unittest.TestCase):
    """Testy jednostkowe dla klasy Squares."""

    def test_squares(self):
        """Testy metody next klasy Squares."""
        squares = Squares()
        self.assertEqual(squares.nxt(), 0)
        self.assertEqual(squares.nxt(), 1)
        self.assertEqual(squares.nxt(), 4)
        self.assertEqual([squares.nxt() for _ in range(5)], [9, 16, 25, 36, 49])


class TestFib(unittest.TestCase):
    """Testy jednostkowe dla klasy Fib."""

    def test_fib(self):
        """Testy metody idx klasy Fib."""
        fib = Fib()
        self.assertEqual([fib.idx(n) for n in range(6)], [0, 1, 1, 2, 3, 5])

    def test_fib_large(self):
        """Test dla wartości fib.idx(100).

        Źródło: https://www.wolframalpha.com/input/?i=fibonacci(100)
        """
        fib = Fib()
        self.assertEqual(fib.idx(100), 354224848179261915075)

    def test_fib_custom(self):
        """Testy metody idx klasy Fib z innymi wartościami początkowymi."""
        fib = Fib(a=2, b=1)
        self.assertEqual([fib.idx(n) for n in range(6)], [2, 1, 3, 4, 7, 11])

        fib = Fib(a=-1, b=1)
        self.assertEqual([fib.idx(n) for n in range(6)], [-1, 1, 0, 1, 1, 2])

    def test_if_recursive(self):
        """Test czy metoda idx klasy Fib jest rekurencyjna."""
        fib = Fib()
        with self.assertRaises(RecursionError):
            fib.idx(5000)


if __name__ == "__main__":
    unittest.main()
