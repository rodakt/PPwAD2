"""Testy dla funkcji z modułu connect_alternately."""

import unittest
from connect_alternately import connect_alternately2, connect_alternately

# assert list(connect_alternately("abc", "xyz")) == list("axbycz")
# assert list(connect_alternately("abc", "xy")) == list("axbyc")
# assert list(connect_alternately("ab", "xyz")) == list("axby")
# assert list(connect_alternately("abc", "")) == ["a"]
# assert list(connect_alternately("", "xyz")) == []
# assert list(connect_alternately([1, 2], [3, 4])) == [1, 3, 2, 4]

# it = connect_alternately((1, 2), "a")

# assert next(it) == 1
# assert next(it) == "a"
# assert next(it) == 2

# try:
#     next(it)
# except StopIteration:
#     pass
# else:
#     raise AssertionError("Generator został wyczerpany")
# assert list(connect_alternately()) == []
# assert list(connect_alternately("a", "xy", "uvw")) == list("axu")
# assert list(connect_alternately("abc", "xy", "u")) == list("axuby")
# assert list(connect_alternately("abc", "kl", "", "u")) == list("ak")


class TestConnectAlternately2(unittest.TestCase):
    """Testy dla funkcji connect_alternately2."""

    def test_simple_cases(self):
        """Testy dla różnych przypadków."""
        self.assertEqual(list(connect_alternately2("abc", "xyz")), list("axbycz"))
        self.assertEqual(list(connect_alternately2("abc", "xy")), list("axbyc"))
        self.assertEqual(list(connect_alternately2("ab", "xyz")), list("axby"))
        self.assertEqual(list(connect_alternately2("abc", "")), ["a"])
        self.assertEqual(list(connect_alternately2("", "xyz")), [])
        self.assertEqual(list(connect_alternately2([1, 2], [3, 4])), [1, 3, 2, 4])

    def test_iterables(self):
        """Testy dla obiektów iterowalnych różnych typów."""
        it = connect_alternately2((1, 2), "a")
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), "a")
        self.assertEqual(next(it), 2)
        with self.assertRaises(StopIteration):
            next(it)

    def test_infinite_iterators(self):
        """Testy dla nieskończonych iteratorów."""

        def infinite1():
            while True:
                yield 1

        def infinite2():
            while True:
                yield 2

        it = connect_alternately2(infinite1(), infinite2())
        self.assertEqual([next(it) for _ in range(10)], [1, 2] * 5)


class TestConnectAlternately(unittest.TestCase):
    """Testy dla funkcji connect_alternately."""

    def test_simple_cases(self):
        """Testy dla różnych przypadków."""
        self.assertEqual(list(connect_alternately("abc", "xyz")), list("axbycz"))
        self.assertEqual(list(connect_alternately("abc", "xy")), list("axbyc"))
        self.assertEqual(list(connect_alternately("ab", "xyz")), list("axby"))
        self.assertEqual(list(connect_alternately("abc", "")), ["a"])
        self.assertEqual(list(connect_alternately("", "xyz")), [])
        self.assertEqual(list(connect_alternately([1, 2], [3, 4])), [1, 3, 2, 4])

    def test_iterables(self):
        """Testy dla obiektów iterowalnych różnych typów."""
        it = connect_alternately((1, 2), "a")
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), "a")
        self.assertEqual(next(it), 2)
        with self.assertRaises(StopIteration):
            next(it)

    def test_infinite_iterators(self):
        """Testy dla nieskończonych iteratorów."""

        def infinite1():
            while True:
                yield 1

        def infinite2():
            while True:
                yield 2

        it = connect_alternately(infinite1(), infinite2())
        self.assertEqual([next(it) for _ in range(10)], [1, 2] * 5)
    
    def test_many_iterables(self):
        """Testy dla wielu iteratorów."""
        self.assertEqual(list(connect_alternately("a", "xy", "uvw")), list("axu"))
        self.assertEqual(list(connect_alternately("abc", "xy", "u")), list("axuby"))
        self.assertEqual(list(connect_alternately("abc", "kl", "", "u")), list("ak"))

if __name__ == "__main__":
    unittest.main()
