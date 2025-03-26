import unittest

from continued_fractions import to_float, euclid, continued_fraction, gcd, to_fraction


class TestToFloat(unittest.TestCase):
    """Testy funkcji to_float() z modułu continued_fractions.py"""

    def test_to_float(self):
        """Testy dla funkcji to_float()"""
        self.assertAlmostEqual(to_float([-3]), -3)
        self.assertAlmostEqual(to_float([0]), 0)
        self.assertAlmostEqual(to_float([23]), 23)
        self.assertAlmostEqual(to_float([1, 2]), 1 + 1 / 2)
        self.assertAlmostEqual(to_float([0, 1, 2]), 0 + 1 / (1 + 1 / 2))
        self.assertAlmostEqual(to_float([1, 2, 3]), 1 + 1 / (2 + 1 / 3))
        self.assertAlmostEqual(to_float([1, 2, 3, 4]), 1 + 1 / (2 + 1 / (3 + 1 / 4)))
        self.assertAlmostEqual(to_float([-2, 3, 4, 1]), -2 + 1 / (3 + 1 / (4 + 1 / 1)))
        self.assertAlmostEqual(
            to_float([1, 1, 1, 1, 1]), 1 + 1 / (1 + 1 / (1 + 1 / (1 + 1 / 1)))
        )

    def test_to_float_empty(self):
        """Testy dla funkcji to_float() z pustą sekwencją"""
        with self.assertRaises(ValueError) as context:
            to_float([])
        self.assertEqual(
            str(context.exception), "sekwencja współczynników nie może być pusta"
        )


class TestToFraction(unittest.TestCase):
    """Testy funkcji to_fraction() z modułu continued_fractions.py"""

    def test_to_fraction(self):
        """Testy dla funkcji to_fraction()"""
        self.assertEqual(to_fraction([-3]), (-3, 1))
        self.assertEqual(to_fraction([0]), (0, 1))
        self.assertEqual(to_fraction([23]), (23, 1))
        self.assertEqual(to_fraction([1, 2]), (3, 2))
        self.assertEqual(to_fraction([0, 1, 2]), (2, 3))
        self.assertEqual(to_fraction([1, 2, 3]), (10, 7))
        self.assertEqual(to_fraction([-1, 2, 2, 2]), (-7, 12))
        # https://www.wolframalpha.com/input?i=continued+fraction+2839%2F617
        self.assertEqual(to_fraction([4, 1, 1, 1, 1, 30, 4]), (2839, 617))

    def test_to_fraction_empty(self):
        """Testy dla funkcji to_fraction() z pustą sekwencją"""
        with self.assertRaises(ValueError) as context:
            to_fraction([])
        self.assertEqual(
            str(context.exception), "sekwencja współczynników nie może być pusta"
        )


class TestEuclid(unittest.TestCase):
    """Testy funkcji euclid() z modułu continued_fractions.py"""

    def test_euclid_simple(self):
        """Testy dla funkcji euclid(), gdy a i b są małe, przypadki brzegowe"""
        self.assertEqual(euclid(0, 1), ([0, 1, 0], [0]))
        self.assertEqual(euclid(1, 1), ([1, 1, 0], [1]))
        self.assertEqual(euclid(1, 2), ([1, 2, 1, 0], [0, 2]))
        self.assertEqual(euclid(2, 1), ([2, 1, 0], [2]))
        self.assertEqual(euclid(-5, 3), ([-5, 3, 1, 0], [-2, 3]))

    def test_euclid_nonpositive_b(self):
        """Testy dla funkcji euclid(), gdy b <= 0"""
        with self.assertRaises(ValueError) as context:
            euclid(1, 0)
        self.assertEqual(str(context.exception), "argument b musi być dodatni")


class TestContinuedFraction(unittest.TestCase):
    """Testy funkcji continued_fraction() z modułu continued_fractions.py"""

    def test_continued_fraction_simple(self):
        """Testy dla funkcji continued_fraction(), gdy a i b są małe, przypadki brzegowe"""
        self.assertEqual(continued_fraction(0, 1), [0])
        self.assertEqual(continued_fraction(1, 1), [1])
        self.assertEqual(continued_fraction(1, 2), [0, 2])
        self.assertEqual(continued_fraction(2, 1), [2])
        self.assertEqual(continued_fraction(2, 3), [0, 1, 2])
        self.assertEqual(continued_fraction(3, 2), [1, 2])
        self.assertEqual(continued_fraction(3, 4), [0, 1, 3])
        self.assertEqual(continued_fraction(4, 3), [1, 3])
        self.assertEqual(continued_fraction(4, 5), [0, 1, 4])
        self.assertEqual(continued_fraction(5, 4), [1, 4])
        self.assertEqual(continued_fraction(4, 7), [0, 1, 1, 3])

    def test_continued_fraction_negative(self):
        """Testy dla funkcji continued_fraction(), gdy licznik lub mianownik jest ujemny"""
        # https://www.wolframalpha.com/input?i=continued+fraction+5678%2F1234
        self.assertEqual(continued_fraction(5678, 1234), [4, 1, 1, 1, 1, 30, 4])
        self.assertEqual(continued_fraction(-5678, -1234), [4, 1, 1, 1, 1, 30, 4])
        # -5678/1234 = -5 + 246/617
        self.assertEqual(continued_fraction(246, 617), [0, 2, 1, 1, 30, 4])
        # Zatem -5678/1234 = [-5, 2, 1, 1, 30, 4]
        self.assertEqual(continued_fraction(-5678, 1234), [-5, 2, 1, 1, 30, 4])
        self.assertEqual(continued_fraction(5678, -1234), [-5, 2, 1, 1, 30, 4])

    def test_continued_fraction_nonpositive_denominator(self):
        """Testy dla funkcji continued_fraction(), gdy mianownik == 0"""
        with self.assertRaises(ZeroDivisionError) as context:
            continued_fraction(1, 0)
        self.assertEqual(str(context.exception), "mianownik nie może być równy 0")
        with self.assertRaises(ZeroDivisionError) as context:
            continued_fraction(-1, 0)
        self.assertEqual(str(context.exception), "mianownik nie może być równy 0")


class TestGcd(unittest.TestCase):
    """Testy funkcji gcd() z modułu continued_fractions.py"""

    def test_gcd_simple(self):
        """Testy dla funkcji gcd(), gdy a i b są małe, przypadki brzegowe"""
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(1, 2), 1)
        self.assertEqual(gcd(2, 1), 1)
        self.assertEqual(gcd(2, 3), 1)
        self.assertEqual(gcd(3, 2), 1)
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(-12, 15), 3)
        self.assertEqual(gcd(12, -15), 3)
        self.assertEqual(gcd(-12, -15), 3)

    def test_gcd_large(self):
        """Testy dla funkcji gcd(), gdy a i b są duże"""
        self.assertEqual(gcd(2**100, 3**100), 1)
        self.assertEqual(gcd(2**100 * 5**20, 3**100 * 5**20), 5**20)

    def test_gcd_against_long_time_execution(self):
        """Testy dla funkcji gcd() w celu sprawdzenia czy działa szybko"""
        self.assertEqual(gcd(10**9, 1), 1)
        self.assertEqual(gcd(1, 10**9), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
