"""Testy jednostkowe dla modułu basic_arithmetic_ops.py"""

import unittest

from basic_arithmetic_ops import add, sub, mul, int_div


class Test1BasicArithmeticOpsSmallValues(unittest.TestCase):
    """Testy jednostkowe dla modułu basic_arithmetic_ops.py, małe liczby całkowite"""

    def test_add(self):
        """Testy funkcji add(), małe liczby całkowite"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        """Testy funkcji sub(), małe liczby całkowite"""
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(-2, 3), -5)
        self.assertEqual(sub(-2, -3), 1)
        self.assertEqual(sub(0, 3), -3)
        self.assertEqual(sub(2, 0), 2)
        self.assertEqual(sub(0, 0), 0)

    def test_mul(self):
        """Testy funkcji mul(), małe liczby całkowite"""
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(-2, -3), 6)
        self.assertEqual(mul(0, 3), 0)
        self.assertEqual(mul(2, 0), 0)
        self.assertEqual(mul(0, 0), 0)

    def test_int_div(self):
        """Testy funkcji int_div(), małe liczby całkowite"""
        self.assertEqual(int_div(2, 3), 0)
        self.assertEqual(int_div(-2, 3), -1)
        self.assertEqual(int_div(-2, -3), 0)
        self.assertEqual(int_div(0, 3), 0)
        self.assertEqual(int_div(2, 1), 2)
        self.assertEqual(int_div(0, 1), 0)
        self.assertEqual(int_div(1, 1), 1)


class Test2BasicArithmeticOpsZeroDivision(unittest.TestCase):
    """Testy jednostkowe dla modułu basic_arithmetic_ops.py, dzielenie przez zero"""

    def test_int_div(self):
        """Testy funkcji int_div(), dzielenie przez zero"""
        with self.assertRaises(ValueError) as context:
            int_div(2, 0)
        self.assertEqual(str(context.exception), "Dzielenie przez zero")
        with self.assertRaises(ValueError) as context:
            int_div(-2, 0)
        self.assertEqual(str(context.exception), "Dzielenie przez zero")
        with self.assertRaises(ValueError) as context:
            int_div(0, 0)
        self.assertEqual(str(context.exception), "Dzielenie przez zero")


class Test3BasicArithmeticOpsLargeValues(unittest.TestCase):
    """Testy jednostkowe dla modułu basic_arithmetic_ops.py, duże liczby całkowite"""

    def test_add(self):
        """Testy funkcji add(), duże liczby całkowite"""
        self.assertEqual(add(10**8, 1), 10**8 + 1)
        self.assertEqual(add(-(10**8), 1), -(10**8) + 1)
        self.assertEqual(add(-(10**8), -1), -(10**8) - 1)
        self.assertEqual(add(10**8, -1), 10**8 - 1)
        self.assertEqual(add(2, 10**8), 2 + 10**8)
        self.assertEqual(add(-2, 10**8), -2 + 10**8)
        self.assertEqual(add(-2, -(10**8)), -2 - 10**8)
        self.assertEqual(add(2, -(10**8)), 2 - 10**8)

    def test_sub(self):
        """Testy funkcji sub(), duże liczby całkowite"""
        self.assertEqual(sub(10**8, 1), 10**8 - 1)
        self.assertEqual(sub(-(10**8), 1), -(10**8) - 1)
        self.assertEqual(sub(-(10**8), -1), -(10**8) + 1)
        self.assertEqual(sub(10**8, -1), 10**8 + 1)
        self.assertEqual(sub(2, 10**8), 2 - 10**8)
        self.assertEqual(sub(-2, 10**8), -2 - 10**8)
        self.assertEqual(sub(-2, -(10**8)), -2 + 10**8)
        self.assertEqual(sub(2, -(10**8)), 2 + 10**8)

    def test_mul_times_1(self):
        """Testy funkcji mul(), duże liczby całkowite, mnożenie przez 1"""
        self.assertEqual(mul(10**8, 1), 10**8)
        self.assertEqual(mul(-(10**8), 1), -(10**8))
        self.assertEqual(mul(-(10**8), -1), 10**8)
        self.assertEqual(mul(10**8, -1), -(10**8))
        self.assertEqual(mul(1, 10**8), 10**8)
        self.assertEqual(mul(-1, 10**8), -(10**8))
        self.assertEqual(mul(-1, -(10**8)), 10**8)
        self.assertEqual(mul(1, -(10**8)), -(10**8))

    def test_mul_times_2(self):
        """Testy funkcji mul(), duże liczby całkowite, mnożenie przez 2"""
        self.assertEqual(mul(10**6, 2), 10**6 * 2)
        self.assertEqual(mul(-(10**6), 2), -(10**6 * 2))
        self.assertEqual(mul(-(10**6), -2), 10**6 * 2)
        self.assertEqual(mul(10**6, -2), -(10**6 * 2))
        self.assertEqual(mul(2, 10**6), 10**6 * 2)
        self.assertEqual(mul(-2, 10**6), -(10**6 * 2))
        self.assertEqual(mul(-2, -(10**6)), 10**6 * 2)
        self.assertEqual(mul(2, -(10**6)), -(10**6 * 2))


if __name__ == "__main__":
    unittest.main()
