"""Testy dla dekoratorów z pliku registry.py"""

import unittest
from registry import register, register_in, REGISTRY


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


if __name__ == "__main__":
    unittest.main()
