"""Testy jednostkowe dla funkcji z modułu fib_gen."""

import unittest
from fib_gen import fib, trib, tetra, fib_general


class TestFib(unittest.TestCase):
    """Testy dla funkcji fib()."""

    def test_fib(self):
        """Test dla funkcji fib() z domyślnymi argumentami."""
        f = fib()
        self.assertEqual(next(f), 0)
        self.assertEqual(next(f), 1)
        self.assertEqual(
            [next(f) for _ in range(10)], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        )

    def test_fib_custom(self):
        """Test dla funkcji fib() z niestandardowymi argumentami."""
        f = fib(2, 3)
        self.assertEqual(next(f), 2)
        self.assertEqual(next(f), 3)
        self.assertEqual(
            [next(f) for _ in range(10)], [5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        )


class TestTetra(unittest.TestCase):
    """Testy dla funkcji tetra()."""

    def test_tetra(self):
        """Test dla funkcji tetra() z domyślnymi argumentami."""
        t = tetra()
        self.assertEqual(next(t), 0)
        self.assertEqual(next(t), 0)
        self.assertEqual(next(t), 0)
        self.assertEqual(next(t), 1)
        self.assertEqual(
            [next(t) for _ in range(10)], [1, 2, 4, 8, 15, 29, 56, 108, 208, 401]
        )

    def test_tetra_custom(self):
        """Test dla funkcji tetra() z niestandardowymi argumentami."""
        t = tetra(1, 0, -1, 1)
        self.assertEqual(next(t), 1)
        self.assertEqual(next(t), 0)
        self.assertEqual(next(t), -1)
        self.assertEqual(next(t), 1)
        self.assertEqual(
            [next(t) for _ in range(10)], [1, 1, 2, 5, 9, 17, 33, 64, 123, 237]
        )


class TestTrib(unittest.TestCase):
    """Testy dla funkcji trib()."""

    def test_trib(self):
        """Test dla funkcji trib() z domyślnymi argumentami."""
        t = trib()
        self.assertEqual(next(t), 0)
        self.assertEqual(next(t), 0)
        self.assertEqual(next(t), 1)
        self.assertEqual(
            [next(t) for _ in range(10)], [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
        )

    def test_trib_custom(self):
        """Test dla funkcji trib() z niestandardowymi argumentami."""
        t = trib(1, 2, -1)
        self.assertEqual(next(t), 1)
        self.assertEqual(next(t), 2)
        self.assertEqual(next(t), -1)
        self.assertEqual(
            [next(t) for _ in range(10)], [2, 3, 4, 9, 16, 29, 54, 99, 182, 335]
        )

class TestFibGeneral(unittest.TestCase):
    """Testy dla funkcji fib_general()."""

    def test_fib_general(self):
        """Test dla funkcji fib_general() z domyślnymi argumentami."""
        f = fib_general(0, 1)
        self.assertEqual(next(f), 0)
        self.assertEqual(next(f), 1)
        self.assertEqual(
            [next(f) for _ in range(10)], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        )

    def test_fib_general_custom(self):
        """Test dla funkcji fib_general() z niestandardowymi argumentami."""
        f = fib_general(2, 3)
        self.assertEqual(next(f), 2)
        self.assertEqual(next(f), 3)
        self.assertEqual(
            [next(f) for _ in range(10)], [5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        )
    
    def test_fib_general_higher_order(self):
        """Test dla funkcji fib_general() z większą liczbą argumentów."""
        f = fib_general(*range(100))
        # Wyczerpujemy pierwsze 100 argumentów
        for _ in range(100):
            next(f)
        self.assertEqual(next(f), sum(range(100)))
        self.assertEqual(next(f), sum(range(1, 100)) + sum(range(100))) 


if __name__ == "__main__":
    unittest.main()
