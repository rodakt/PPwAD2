"""Testy jednostkowe dla funkcji accumulate z modułu accumulate."""

import unittest
from operator import add, mul

from accumulate import accumulate


class TestAccumulateReturnsIterator(unittest.TestCase):
    """Sprawdza, że accumulate zwraca iterator."""

    def test_returns_iterator(self):
        result = accumulate([1, 2, 3], add)
        self.assertTrue(hasattr(result, '__iter__'))
        self.assertTrue(hasattr(result, '__next__'))
        self.assertIs(iter(result), result)

    def test_lazy_evaluation(self):
        """Kolejne wartości pobierane są przez next."""
        it = accumulate([1, 2, 3, 4], add)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 3)
        self.assertEqual(next(it), 6)
        self.assertEqual(next(it), 10)
        with self.assertRaises(StopIteration):
            next(it)


class TestAccumulateAdd(unittest.TestCase):
    """Testy dla func=add (bieżąca suma)."""

    def test_add_no_initial(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4], add)), [1, 3, 6, 10])

    def test_add_with_initial(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4], add, initial=0)), [0, 1, 3, 6, 10])

    def test_add_initial_nonzero(self):
        self.assertEqual(list(accumulate([1, 2, 3], add, initial=10)), [10, 11, 13, 16])

    def test_add_single_element(self):
        self.assertEqual(list(accumulate([5], add)), [5])
        self.assertEqual(list(accumulate([5], add, initial=0)), [0, 5])


class TestAccumulateMul(unittest.TestCase):
    """Testy dla func=mul (bieżący iloczyn)."""

    def test_mul_no_initial(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4], mul)), [1, 2, 6, 24])

    def test_mul_with_initial(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4], mul, initial=1)), [1, 1, 2, 6, 24])

    def test_mul_with_zero(self):
        self.assertEqual(list(accumulate([1, 2, 0, 4], mul)), [1, 2, 0, 0])


class TestAccumulateMaxMin(unittest.TestCase):
    """Testy dla func=max i func=min (bieżące ekstremum)."""

    def test_max(self):
        self.assertEqual(list(accumulate([1, 2, 3, 2, 0, 7], max)), [1, 2, 3, 3, 3, 7])

    def test_min(self):
        self.assertEqual(list(accumulate([1, 2, 3, 2, 0, 7], min)), [1, 1, 1, 1, 0, 0])

    def test_max_decreasing(self):
        self.assertEqual(list(accumulate([5, 4, 3, 2, 1], max)), [5, 5, 5, 5, 5])

    def test_min_increasing(self):
        self.assertEqual(list(accumulate([1, 2, 3, 4, 5], min)), [1, 1, 1, 1, 1])


class TestAccumulateCustomFunc(unittest.TestCase):
    """Testy dla własnej funkcji dwuargumentowej."""

    def test_subtraction(self):
        self.assertEqual(list(accumulate([10, 1, 2, 3], lambda a, b: a - b)), [10, 9, 7, 4])

    def test_string_concat(self):
        self.assertEqual(
            list(accumulate(['a', 'b', 'c'], lambda a, b: a + b)),
            ['a', 'ab', 'abc']
        )


class TestAccumulateOnIterator(unittest.TestCase):
    """Sprawdza, że accumulate działa na dowolnym iteratorze, nie tylko liście."""

    def test_on_iter(self):
        it = iter([1, 2, 3, 4])
        self.assertEqual(list(accumulate(it, add)), [1, 3, 6, 10])

    def test_on_generator(self):
        def naturals():
            n = 1
            while True:
                yield n
                n += 1

        result = accumulate(naturals(), add)
        self.assertEqual([next(result) for _ in range(5)], [1, 3, 6, 10, 15])

    def test_on_range(self):
        self.assertEqual(list(accumulate(range(1, 6), mul)), [1, 2, 6, 24, 120])

    def test_on_tuple(self):
        self.assertEqual(list(accumulate((3, 1, 4, 1, 5), add)), [3, 4, 8, 9, 14])


class TestAccumulateEmpty(unittest.TestCase):
    """Testy dla pustego it."""

    def test_empty_no_initial(self):
        self.assertEqual(list(accumulate([], add)), [])

    def test_empty_with_initial(self):
        self.assertEqual(list(accumulate([], add, initial=0)), [0])

    def test_empty_iterator_no_initial(self):
        self.assertEqual(list(accumulate(iter([]), mul)), [])

    def test_empty_iterator_with_initial(self):
        self.assertEqual(list(accumulate(iter([]), mul, initial=1)), [1])


if __name__ == '__main__':
    unittest.main()
