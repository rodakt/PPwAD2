"""Testy dla funkcji z modułu running_values."""

import unittest

from running_values import (
    running_total,
    running_product,
    running_max,
    running_min,
    running_extremum,
)


class TestRunningTotal(unittest.TestCase):
    """Testy dla funkcji running_total."""

    def test_empty(self):
        """Test dla pustego obiektu."""
        self.assertEqual(list(running_total([])), [0])

    def test_single(self):
        """Test dla obiektu z jednym elementem."""
        self.assertEqual(list(running_total([7])), [0, 7])

    def test_multiple(self):
        """Test dla obiektu z wieloma elementami."""
        self.assertEqual(list(running_total([1, 2, 3, 4, 5])), [0, 1, 3, 6, 10, 15])

    def test_iterator(self):
        """Test dla iteratora."""
        it = iter([1, 2, 3, 4, 5])
        self.assertEqual(list(running_total(it)), [0, 1, 3, 6, 10, 15])

    def test_iterator_empty(self):
        """Test dla pustego iteratora."""
        it = iter([])
        self.assertEqual(list(running_total(it)), [0])

    def test_iterator_infinite(self):
        """Test dla nieskończonego iteratora."""

        def ones():
            while True:
                yield 1

        it = ones()
        for i, total in enumerate(running_total(it)):
            self.assertEqual(total, i)
            if i > 10:
                break

    def test_return_iterator(self):
        """Test zwracania iteratora."""
        it = iter([1, 2, 3, 4, 5])
        running = running_total(it)
        self.assertEqual(next(running), 0)
        self.assertEqual(next(running), 1)
        self.assertEqual(next(running), 3)
        self.assertEqual(next(running), 6)
        self.assertEqual(next(running), 10)
        self.assertEqual(next(running), 15)
        with self.assertRaises(StopIteration):
            next(running)


class TestRunningProduct(unittest.TestCase):
    """Testy dla funkcji running_product."""

    def test_empty(self):
        """Test dla pustego obiektu."""
        self.assertEqual(list(running_product([])), [1])

    def test_single(self):
        """Test dla obiektu z jednym elementem."""
        self.assertEqual(list(running_product([7])), [1, 7])

    def test_multiple(self):
        """Test dla obiektu z wieloma elementami."""
        self.assertEqual(list(running_product([1, 2, 3, 4, 5])), [1, 1, 2, 6, 24, 120])

    def test_iterator(self):
        """Test dla iteratora."""
        it = iter([1, 2, 3, 4, 5])
        self.assertEqual(list(running_product(it)), [1, 1, 2, 6, 24, 120])

    def test_iterator_empty(self):
        """Test dla pustego iteratora."""
        it = iter([])
        self.assertEqual(list(running_product(it)), [1])

    def test_iterator_infinite(self):
        """Test dla nieskończonego iteratora."""

        def ones():
            while True:
                yield 1

        it = ones()
        for i, product in enumerate(running_product(it)):
            self.assertEqual(product, 1**i)
            if i > 10:
                break

    def test_return_iterator(self):
        """Test zwracania iteratora."""
        it = iter([1, 2, 3, 4, 5])
        running = running_product(it)
        self.assertEqual(next(running), 1)
        self.assertEqual(next(running), 1)
        self.assertEqual(next(running), 2)
        self.assertEqual(next(running), 6)
        self.assertEqual(next(running), 24)
        self.assertEqual(next(running), 120)
        with self.assertRaises(StopIteration):
            next(running)


class TestRunningMax(unittest.TestCase):
    """Testy dla funkcji running_max."""

    def test_empty(self):
        """Test dla pustego obiektu."""
        self.assertEqual(list(running_max([])), [])

    def test_single(self):
        """Test dla obiektu z jednym elementem."""
        self.assertEqual(list(running_max([7])), [7])

    def test_multiple(self):
        """Test dla obiektu z wieloma elementami."""
        self.assertEqual(list(running_max([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(running_max([5, 4, 3, 2, 1])), [5])
        self.assertEqual(list(running_max([5, 4, 3, 7, 2, 1, 6, 8, 9])), [5, 7, 8, 9])
    
    def test_key(self):
        """Test dla klucza."""
        self.assertEqual(list(running_max([1, 2, 3, 4, 5], key=lambda x: -x)), [1])
        self.assertEqual(list(running_max([5, 4, 3, 2, 1], key=lambda x: -x)), [5, 4, 3, 2, 1])
        self.assertEqual(list(running_max([5, 4, 3, 7, 2, 1, 6, 8, 9], key=lambda x: -x)), [5, 4, 3, 2, 1])
    
    def test_iterator(self):
        """Test dla iteratora."""
        it = iter([1, 2, 3, 4, 5])
        self.assertEqual(list(running_max(it)), [1, 2, 3, 4, 5])
        
    def test_iterator_empty(self):
        """Test dla pustego iteratora."""
        it = iter([])
        self.assertEqual(list(running_max(it)), [])
        
    def test_iterator_infinite(self):
        """Test dla nieskończonego iteratora."""
        
        def naturals():
            i = 1
            while True:
                yield i
                i += 1
        
        it = naturals()
        self.assertEqual(
            [next(it) for _ in range(10)],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
    
    def test_return_iterator(self):
        """Test zwracania iteratora."""
        it = iter([1, 2, 3, 4, 5])
        running = running_max(it)
        self.assertEqual(next(running), 1)
        self.assertEqual(next(running), 2)
        self.assertEqual(next(running), 3)
        self.assertEqual(next(running), 4)
        self.assertEqual(next(running), 5)
        with self.assertRaises(StopIteration):
            next(running)


class TestRunningMin(unittest.TestCase):
    """Testy dla funkcji running_min."""

    def test_empty(self):
        """Test dla pustego obiektu."""
        self.assertEqual(list(running_min([])), [])

    def test_single(self):
        """Test dla obiektu z jednym elementem."""
        self.assertEqual(list(running_min([7])), [7])

    def test_multiple(self):
        """Test dla obiektu z wieloma elementami."""
        self.assertEqual(list(running_min([1, 2, 3, 4, 5])), [1])
        self.assertEqual(list(running_min([5, 4, 3, 2, 1])), [5, 4, 3, 2, 1])
        self.assertEqual(list(running_min([5, 4, 3, 7, 2, 1, 6, 8, 9])), [5, 4, 3, 2, 1])
    
    def test_key(self):
        """Test dla klucza."""
        self.assertEqual(list(running_min([1, 2, 3, 4, 5], key=lambda x: -x)), [1, 2, 3, 4, 5])
        self.assertEqual(list(running_min([5, 4, 3, 2, 1], key=lambda x: -x)), [5])
        self.assertEqual(list(running_min([5, 4, 3, 7, 2, 1, 6, 8, 9], key=lambda x: -x)), [5, 7, 8, 9])
    
    def test_iterator(self):
        """Test dla iteratora."""
        it = iter([1, 2, 3, 4, 5])
        self.assertEqual(list(running_min(it)), [1])
        
    def test_iterator_empty(self):
        """Test dla pustego iteratora."""
        it = iter([])
        self.assertEqual(list(running_min(it)), [])
        
    def test_iterator_infinite(self):
        """Test dla nieskończonego iteratora."""
        
        def negatives():
            i = -1
            while True:
                yield i
                i -= 1
        
        it = negatives()
        self.assertEqual(
            [next(it) for _ in range(10)],
            [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        )
    
    def test_return_iterator(self):
        """Test zwracania iteratora."""
        it = iter([1, 2, 3, 4, 5])
        running = running_min(it)
        self.assertEqual(next(running), 1)
        with self.assertRaises(StopIteration):
            next(running)
        
class TestRunningExtremum(unittest.TestCase):
    """Testy dla funkcji running_extremum."""

    def test_empty(self):
        """Test dla pustego obiektu."""
        self.assertEqual(list(running_extremum([])), [])

    def test_single(self):
        """Test dla obiektu z jednym elementem."""
        self.assertEqual(list(running_extremum([7])), [7])

    def test_multiple(self):
        """Test dla obiektu z wieloma elementami."""
        self.assertEqual(list(running_extremum([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(running_extremum([5, 4, 3, 2, 1])), [5, 4, 3, 2, 1])
        self.assertEqual(list(running_extremum([5, 4, 3, 7, 2, 1, 6, 8, 9])), [5, 4, 3, 7, 2, 1, 8, 9])
        self.assertEqual(list(running_extremum([5, 4, 1, 2, 3, 6,])), [5, 4, 1, 6])
    
    def test_key(self):
        """Test dla klucza."""
        self.assertEqual(list(running_extremum([1, 2, 3, 4, 5], key=lambda x: -x)), [1, 2, 3, 4, 5])
        self.assertEqual(list(running_extremum([5, 4, 3, 2, 1], key=lambda x: -x)), [5, 4, 3, 2, 1])
        self.assertEqual(list(running_extremum([5, 4, 3, 7, 2, 1, 6, 8, 9], key=lambda x: -x)), [5, 4, 3, 7, 2, 1, 8, 9])
        
    def test_iterator(self):
        """Test dla iteratora."""
        it = iter([1, 2, 3, 4, 5])
        self.assertEqual(list(running_extremum(it)), [1, 2, 3, 4, 5])
        
    def test_iterator_empty(self):
        """Test dla pustego iteratora."""
        it = iter([])
        self.assertEqual(list(running_extremum(it)), [])
        
    def test_iterator_infinite(self):
        """Test dla nieskończonego iteratora."""
        
        def alternating():
            i = 1
            while True:
                yield i
                if i > 0:
                    i += 1
                    i = -i
                else:
                    i -= 1
                    i = -i
            
        it = alternating()
        self.assertEqual(
            [next(it) for _ in range(10)],
            [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
        )
        
    def test_return_iterator(self):
        """Test zwracania iteratora."""
        it = iter([1, 2, 3, 4, 5])
        running = running_extremum(it)
        self.assertEqual(next(running), 1)
        self.assertEqual(next(running), 2)
        self.assertEqual(next(running), 3)
        self.assertEqual(next(running), 4)
        self.assertEqual(next(running), 5)
        with self.assertRaises(StopIteration):
            next(running)
                    

if __name__ == "__main__":
    unittest.main()
