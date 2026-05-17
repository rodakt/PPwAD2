"""Testy jednostkowe dla funkcji z modułu helpers."""

import unittest

from helpers import my_enumerate, take, repeat_each, geometric


class TestMyEnumerate(unittest.TestCase):

    def test_returns_iterator(self):
        result = my_enumerate('abc')
        self.assertTrue(hasattr(result, '__iter__'))
        self.assertTrue(hasattr(result, '__next__'))
        self.assertIs(iter(result), result)

    def test_default_start(self):
        self.assertEqual(list(my_enumerate('abc')), [(0, 'a'), (1, 'b'), (2, 'c')])

    def test_custom_start(self):
        self.assertEqual(list(my_enumerate('abc', start=10)), [(10, 'a'), (11, 'b'), (12, 'c')])

    def test_start_negative(self):
        self.assertEqual(list(my_enumerate('ab', start=-1)), [(-1, 'a'), (0, 'b')])

    def test_empty(self):
        self.assertEqual(list(my_enumerate([])), [])

    def test_on_iterator(self):
        it = iter([10, 20, 30])
        self.assertEqual(list(my_enumerate(it)), [(0, 10), (1, 20), (2, 30)])

    def test_on_range(self):
        self.assertEqual(list(my_enumerate(range(3, 6))), [(0, 3), (1, 4), (2, 5)])

    def test_lazy(self):
        it = my_enumerate([10, 20, 30])
        self.assertEqual(next(it), (0, 10))
        self.assertEqual(next(it), (1, 20))
        self.assertEqual(next(it), (2, 30))
        with self.assertRaises(StopIteration):
            next(it)


class TestTake(unittest.TestCase):

    def test_returns_iterator(self):
        result = take(range(100), 5)
        self.assertTrue(hasattr(result, '__iter__'))
        self.assertTrue(hasattr(result, '__next__'))
        self.assertIs(iter(result), result)

    def test_basic(self):
        self.assertEqual(list(take(range(100), 5)), [0, 1, 2, 3, 4])

    def test_fewer_than_n(self):
        self.assertEqual(list(take('abc', 10)), ['a', 'b', 'c'])

    def test_zero(self):
        self.assertEqual(list(take('abc', 0)), [])

    def test_empty(self):
        self.assertEqual(list(take([], 5)), [])

    def test_on_iterator(self):
        it = iter([1, 2, 3, 4, 5])
        self.assertEqual(list(take(it, 3)), [1, 2, 3])

    def test_on_infinite_generator(self):
        def naturals():
            n = 0
            while True:
                yield n
                n += 1

        self.assertEqual(list(take(naturals(), 6)), [0, 1, 2, 3, 4, 5])

    def test_lazy(self):
        it = take([10, 20, 30], 2)
        self.assertEqual(next(it), 10)
        self.assertEqual(next(it), 20)
        with self.assertRaises(StopIteration):
            next(it)


class TestRepeatEach(unittest.TestCase):

    def test_returns_iterator(self):
        result = repeat_each([1, 2, 3], 2)
        self.assertTrue(hasattr(result, '__iter__'))
        self.assertTrue(hasattr(result, '__next__'))
        self.assertIs(iter(result), result)

    def test_k2(self):
        self.assertEqual(list(repeat_each([1, 2, 3], 2)), [1, 1, 2, 2, 3, 3])

    def test_k3_string(self):
        self.assertEqual(list(repeat_each('ab', 3)), ['a', 'a', 'a', 'b', 'b', 'b'])

    def test_k1(self):
        self.assertEqual(list(repeat_each([1, 2, 3], 1)), [1, 2, 3])

    def test_k0(self):
        self.assertEqual(list(repeat_each([1, 2, 3], 0)), [])

    def test_empty(self):
        self.assertEqual(list(repeat_each([], 5)), [])

    def test_on_iterator(self):
        it = iter([10, 20])
        self.assertEqual(list(repeat_each(it, 3)), [10, 10, 10, 20, 20, 20])

    def test_lazy(self):
        it = repeat_each([1, 2], 2)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 2)
        with self.assertRaises(StopIteration):
            next(it)


class TestGeometric(unittest.TestCase):

    def test_returns_iterator(self):
        result = geometric(1, 2)
        self.assertTrue(hasattr(result, '__iter__'))
        self.assertTrue(hasattr(result, '__next__'))
        self.assertIs(iter(result), result)

    def test_powers_of_2(self):
        g = geometric(1, 2)
        self.assertEqual([next(g) for _ in range(6)], [1, 2, 4, 8, 16, 32])

    def test_custom_start(self):
        g = geometric(3, 10)
        self.assertEqual([next(g) for _ in range(4)], [3, 30, 300, 3000])

    def test_r1(self):
        g = geometric(5, 1)
        self.assertEqual([next(g) for _ in range(5)], [5, 5, 5, 5, 5])

    def test_fraction(self):
        g = geometric(1, 0.5)
        result = [next(g) for _ in range(4)]
        self.assertAlmostEqual(result[0], 1.0)
        self.assertAlmostEqual(result[1], 0.5)
        self.assertAlmostEqual(result[2], 0.25)
        self.assertAlmostEqual(result[3], 0.125)

    def test_infinite(self):
        """Generator nie kończy się po skończonej liczbie wywołań next."""
        g = geometric(1, 2)
        for _ in range(100):
            next(g)


if __name__ == '__main__':
    unittest.main()
