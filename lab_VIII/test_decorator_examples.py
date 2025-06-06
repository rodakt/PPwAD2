"""Testy dla dekoratorów z pliku decorator_examples.py"""

import unittest
from decorator_examples import register, register_in, pre_test, post_test, REGISTRY


class TestRegister(unittest.TestCase):
    """Testy dla dekoratora register."""

    def setUp(self):
        REGISTRY.clear()

    def test_register(self):
        """Test dekoratora register."""

        @register
        def f():
            """Funkcja f."""
            return "foo"

        @register
        def g():
            """Funkcja g."""
            return "bar"

        self.assertEqual(REGISTRY, {"f": f, "g": g})
        self.assertIs(f, REGISTRY["f"])
        self.assertIs(g, REGISTRY["g"])
        self.assertEqual(f.__doc__, "Funkcja f.")
        self.assertEqual(g.__doc__, "Funkcja g.")


class TestRegisterIn(unittest.TestCase):
    """Testy dla dekoratora register_in."""

    def setUp(self):
        self.dictionary = {}

    def test_register_in(self):
        """Test dekoratora register_in."""

        @register_in(self.dictionary)
        def f():
            """Funkcja f."""
            return "foo"

        @register_in(self.dictionary)
        def g():
            """Funkcja g."""
            return "bar"

        self.assertEqual(self.dictionary, {"f": f, "g": g})
        self.assertIs(f, self.dictionary["f"])
        self.assertIs(g, self.dictionary["g"])
        self.assertEqual(f.__doc__, "Funkcja f.")
        self.assertEqual(g.__doc__, "Funkcja g.")


class TestPreTest(unittest.TestCase):
    """Testy dla dekoratora pre_test."""

    def test_pre_test_is_positive(self):
        """Test dekoratora pre_test dla predykatu is_positive."""

        def positive(x):
            assert x > 0, f"{x} <= 0"

        @pre_test(positive)
        def u(a):
            """Pierwiastek kwadratowy."""
            return a**0.5

        self.assertAlmostEqual(u(9), 3.0)
        self.assertAlmostEqual(u(100), 10.0)
        self.assertEqual(u.__name__, "u")
        self.assertEqual(u.__doc__, "Pierwiastek kwadratowy.")
        with self.assertRaises(AssertionError) as cm:
            u(-9)
        self.assertEqual(str(cm.exception), "-9 <= 0")

    def test_pre_test_is_variable_name(self):
        """Test dekoratora pre_test dla predykatu is_variable_name."""

        def is_variable_name(s):
            """Sprawdza, czy łańcuch jest nazwą zmiennej."""
            assert s.isidentifier(), "łańcuch nie jest nazwą zmiennej."

        @pre_test(is_variable_name)
        def g(s):
            """Zwraca łańcuch s zapisany wielkimi literami."""
            return s.upper()

        self.assertEqual(g("a"), "A")
        self.assertEqual(g("x"), "X")
        self.assertEqual(g("x_2"), "X_2")
        self.assertEqual(g.__name__, "g")
        self.assertEqual(g.__doc__, "Zwraca łańcuch s zapisany wielkimi literami.")
        with self.assertRaises(AssertionError) as cm:
            g("2a")
        self.assertEqual(str(cm.exception), "łańcuch nie jest nazwą zmiennej.")

    def test_pre_test_at_least_3(self):
        """Test dekoratora pre_test dla predykatu at_least_3."""

        def at_least_3(*c):
            """Sprawdza, czy liczba argumentów jest większa niż 2."""
            assert len(c) > 2, "mniej niż 3 argumenty"

        @pre_test(at_least_3)
        def h(*c):
            """Zwraca największą wartość z argumentów."""
            return max(c)

        self.assertEqual(h(3, 1, 5, 2), 5)
        self.assertEqual(h.__name__, "h")
        self.assertEqual(h.__doc__, "Zwraca największą wartość z argumentów.")
        with self.assertRaises(AssertionError) as cm:
            h(3, 1)
        self.assertEqual(str(cm.exception), "mniej niż 3 argumenty")


class TestPostTest(unittest.TestCase):
    """Testy dla dekoratora post_test."""

    def test_post_test_is_positive(self):
        """Test dekoratora post_test dla predykatu is_positive."""

        def positive(x):
            assert x > 0, f"{x} <= 0"

        @post_test(positive)
        def multiply(a, b):
            """Iloczyn dwóch liczb."""
            return a * b

        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, -5), 10)
        self.assertEqual(multiply.__name__, "multiply")
        self.assertEqual(multiply.__doc__, "Iloczyn dwóch liczb.")
        # Funkcja zwróci wartość ujemną, co powinno wywołać AssertionError
        with self.assertRaises(AssertionError) as cm:
            multiply(-3, 2)
        self.assertEqual(str(cm.exception), "-6 <= 0")

    def test_post_test_is_even(self):
        """Test dekoratora post_test dla predykatu is_even."""

        def is_even(x):
            assert x % 2 == 0, f"{x} nie jest liczbą parzystą"

        @post_test(is_even)
        def multiply(a, b):
            """Iloczyn dwóch liczb."""
            return a * b
        self.assertEqual(multiply(2, 7), 14)
        self.assertEqual(multiply(-10, 3), -30)
        self.assertEqual(multiply.__name__, "multiply")
        self.assertEqual(multiply.__doc__, "Iloczyn dwóch liczb.")
        # Funkcja zwróci liczbę nieparzystą, co powinno wywołać AssertionError
        with self.assertRaises(AssertionError) as cm:
            multiply(3, 5)
        self.assertEqual(str(cm.exception), "15 nie jest liczbą parzystą")

    def test_post_test_length(self):
        """Test dekoratora post_test dla predykatu sprawdzającego długość."""

        def length_is_3(result):
            assert len(result) == 3, f"Długość wyniku {len(result)} nie jest równa 3"

        @post_test(length_is_3)
        def get_first_three(seq):
            """Zwraca pierwsze trzy elementy sekwencji."""
            return seq[:3]

        self.assertEqual(get_first_three([1, 2, 3, 4, 5]), [1, 2, 3])
        self.assertEqual(get_first_three("abcde"), "abc")
        self.assertEqual(get_first_three.__name__, "get_first_three")
        self.assertEqual(get_first_three.__doc__, "Zwraca pierwsze trzy elementy sekwencji.")
        # Sekwencja jest zbyt krótka, co powinno wywołać AssertionError
        with self.assertRaises(AssertionError) as cm:
            get_first_three([1, 2])
        self.assertEqual(str(cm.exception), "Długość wyniku 2 nie jest równa 3")


if __name__ == "__main__":
    unittest.main()
