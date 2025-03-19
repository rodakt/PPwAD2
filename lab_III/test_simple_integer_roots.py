"""
Testy jednostkowe dla funkcji z modułu simple_integer_roots.
"""

import unittest

from simple_integer_roots import (
    integer_square_root,
    integer_cubic_root,
    is_perfect_square,
    is_perfect_cube,
)


class TestIntegerSquareRoot(unittest.TestCase):
    """Testy jednostkowe dla funkcji integer_square_root()"""

    def test_1_integer_square_root_small_values(self):
        """Testy dla wartości n < 100**2

        Jeśli m**2 <= n < (m + 1)**2, to integer_square_root(n) == m
        """
        for m in range(100):
            for n in range(m**2, (m + 1) ** 2):
                self.assertEqual(
                    integer_square_root(n),
                    m,
                    f"integer_square_root({n}) nie zwrócił oczekiwanej wartości {m}",
                )

    def test_2_integer_square_root_against_overflowerror(self):
        """Sprawdza czy funkcja integer_square_root() obsługuje
        wartości całkowite, które nie mieszczą się w zakresie typu float.

        Ponieważ 2**10_000 = (2**5_000)**2, więc oczekujemy, że
        integer_square_root(2**10_000) zwóci 2**5_000.
        """
        n = 2**10_000
        try:
            self.assertEqual(
                integer_square_root(n),
                2**5_000,
                "integer_square_root(2 ** 10_000) nie zwrócił oczekiwanej wartości 2 ** 5_000",
            )
        except OverflowError:
            self.fail("integer_square_root(2 ** 10_000) zgłosił OverflowError")

    def test_3_integer_square_root_large_values(self):
        """Testy dla 2**10_000 - 1 i 2**10_000 + 1

        Jeśli m >= 2, to
        (m - 1)**2 < m**2 - 1 < m**2 < m**2 + 1 < (m + 1)**2.
        Zatem
        * dla n = m**2 - 1, integer_square_root(n) powinno zwrócić m - 1;
        * dla n = m**2 + 1, integer_square_root(n) powinno zwrócić m.
        """
        m = 2**5_000
        self.assertEqual(
            integer_square_root(m**2 - 1),
            m - 1,
            "dla m**2 - 1, integer_square_root(n) nie zwrócił oczekiwanej wartości m - 1",
        )
        self.assertEqual(
            integer_square_root(m**2 + 1),
            m,
            "dla m**2 + 1, integer_square_root(n) nie zwrócił oczekiwanej wartości m",
        )

    def test_4_integer_square_root_negative_argument(self):
        """Testy dla wartości ujemnych

        Dla n < 0, integer_square_root(n) powinno zgłosić ValueError.
        """
        with self.assertRaises(ValueError) as cm:
            integer_square_root(-1)
        self.assertEqual(str(cm.exception), "argument musi być nieujemny")


class TestIntegerCubicRoot(unittest.TestCase):
    """Testy jednostkowe dla funkcji integer_cubic_root()"""

    def test_1_integer_cubic_root_small_values(self):
        """Testy dla wartości n < 50**3

        Jeśli m**3 <= n < (m + 1)**3, to integer_cubic_root(n) == m
        """
        for m in range(50):
            for n in range(m**3, (m + 1) ** 3):
                self.assertEqual(
                    integer_cubic_root(n),
                    m,
                    f"integer_cubic_root({n}) nie zwrócił oczekiwanej wartości {m}",
                )

    def test_2_integer_cubic_root_against_overflowerror(self):
        """Sprawdza czy funkcja integer_cubic_root() obsługuje
        wartości całkowite, które nie mieszczą się w zakresie typu float.

        Ponieważ 2**9000 = (2**3000)**3, więc oczekujemy, że
        integer_cubic_root(2**9000) zwóci 2**3000.
        """
        n = 2**9_000
        try:
            self.assertEqual(
                integer_cubic_root(n),
                2**3_000,
                "integer_cubic_root(2 ** 9_000) nie zwrócił oczekiwanej wartości 2 ** 3_000",
            )
        except OverflowError:
            self.fail("integer_cubic_root(2 ** 9_000) zgłosił OverflowError")

    def test_3_integer_cubic_root_large_values(self):
        """Testy dla 2**9_000 - 1 i 2**9_000 + 1

        Jeśli m >= 2, to
        (m - 1)**3 < m**3 - 1 < m**3 < m**3 + 1 < (m + 1)**3.
        Zatem
        * dla n = m**3 - 1, integer_cubic_root(n) powinno zwrócić m - 1;
        * dla n = m**3 + 1, integer_cubic_root(n) powinno zwrócić m.
        """
        m = 2**3_000
        self.assertEqual(
            integer_cubic_root(m**3 - 1),
            m - 1,
            "dla m**3 - 1, integer_cubic_root(n) nie zwrócił oczekiwanej wartości m - 1",
        )
        self.assertEqual(
            integer_cubic_root(m**3 + 1),
            m,
            "dla m**3 + 1, integer_cubic_root(n) nie zwrócił oczekiwanej wartości m",
        )


class TestIsPerfectSquare(unittest.TestCase):
    """Testy jednostkowe dla funkcji is_perfect_square()"""

    def test_1_is_perfect_square(self):
        """Testy dla wartości n = m**2, gdzie m = 0, 1, 2, ..., 100"""
        for m in range(101):
            n = m**2
            self.assertTrue(
                is_perfect_square(n),
                f"is_perfect_square({n}) nie zwróciło oczekiwanej wartości True",
            )

    def test_2_is_perfect_square_negative_case(self):
        """Testy dla wartości, które nie są kwadratami liczb całkowitych"""
        self.assertEqual(
            is_perfect_square(2), False, "2 nie jest kwadratem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_square(3), False, "3 nie jest kwadratem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_square(5), False, "5 nie jest kwadratem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_square(1001), False, "1001 nie jest kwadratem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_square(-1), False, "-1 nie jest kwadratem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_square(-9), False, "-9 nie jest kwadratem liczby całkowitej"
        )

    def test_3_is_perfect_square_large_values(self):
        """Test dla wartości nie mieszczących się w zakresie typu float"""
        n = 2**10_000
        self.assertTrue(
            is_perfect_square(n),
            "is_perfect_square(2**10_000) nie zwróciło oczekiwanej wartości True",
        )
        n = 2**10_000 + 1
        self.assertFalse(
            is_perfect_square(n),
            "is_perfect_square(2**10_000 + 1) nie zwróciło oczekiwanej wartości False",
        )


class TestIsPerfectCube(unittest.TestCase):
    """Testy jednostkowe dla funkcji is_perfect_cube()"""

    def test_1_is_perfect_cube(self):
        """Testy dla wartości n = m**3, gdzie m = -50, -49, ..., 50"""
        for m in range(-50, 51):
            n = m**3
            self.assertTrue(
                is_perfect_cube(n),
                f"is_perfect_cube({n}) nie zwróciło oczekiwanej wartości True",
            )

    def test_2_is_perfect_cube_negative_case(self):
        """Testy dla wartości, które nie są sześcianami liczb całkowitych"""
        self.assertEqual(
            is_perfect_cube(2), False, "2 nie jest sześcianem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_cube(3), False, "3 nie jest sześcianem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_cube(5), False, "5 nie jest sześcianem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_cube(1001), False, "1001 nie jest sześcianem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_cube(-10), False, "-10 nie jest sześcianem liczby całkowitej"
        )
        self.assertEqual(
            is_perfect_cube(-80), False, "-80 nie jest sześcianem liczby całkowitej"
        )

    def test_3_is_perfect_cube_large_values(self):
        """Test dla wartości nie mieszczących się w zakresie typu float"""
        n = 2**9_000
        self.assertTrue(
            is_perfect_cube(n),
            "is_perfect_cube(2**9_000) nie zwróciło oczekiwanej wartości True",
        )
        n = 2**9_000 + 1
        self.assertFalse(
            is_perfect_cube(n),
            "is_perfect_cube(2**9_000 + 1) nie zwróciło oczekiwanej wartości False",
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
