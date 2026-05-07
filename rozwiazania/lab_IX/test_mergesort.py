"""Testy jednostkowe dla funkcji merge i mergesort z modułu mergesort."""

import unittest
from mergesort import merge, mergesort


class TestMerge(unittest.TestCase):

    def test_empty(self):
        """Łączenie dwóch pustych list."""
        A = []
        merge(A, 0, 0, 0)
        self.assertEqual(A, [])

    def test_single(self):
        """Łączenie dwóch jednoelementowych list."""
        A = [42]
        merge(A, 0, 1, 1)
        self.assertEqual(A, [42])
        merge(A, 0, 0, 1)
        self.assertEqual(A, [42])

    def test_two_elements(self):
        """Łączenie dwóch dwuelementowych list."""
        A = [2, 1]
        merge(A, 0, 1, 2)
        self.assertEqual(A, [1, 2])

    def test_two_elements_reversed(self):
        """Łączenie dwóch dwuelementowych list w odwrotnej kolejności."""
        A = [1, 2]
        merge(A, 0, 1, 2)
        self.assertEqual(A, [1, 2])

    def test_two_elements_equal(self):
        """Łączenie dwóch dwuelementowych list z takimi samymi elementami."""
        A = [1, 1]
        merge(A, 0, 1, 2)
        self.assertEqual(A, [1, 1])

    def test_longer(self):
        """Łączenie dwóch dłuższych list."""
        A = [1, 3, 5, 2, 4, 6]
        merge(A, 0, 3, 6)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
        A = [1, 3, 2, 4, 5, 6]
        merge(A, 0, 2, 6)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])


class TestMergeSort(unittest.TestCase):

    def test_empty(self):
        """Pusta lista powinna pozostać pusta."""
        A = []
        mergesort(A)
        self.assertEqual(A, [])

    def test_single(self):
        """Lista jednoelementowa powinna pozostać niezmieniona."""
        A = [42]
        mergesort(A)
        self.assertEqual(A, [42])

    def test_sorted(self):
        """Posortowana lista powinna pozostać niezmieniona."""
        A = [1, 2, 3, 4, 5]
        mergesort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_reversed(self):
        """Sortowanie listy malejącej."""
        A = [5, 4, 3, 2, 1]
        mergesort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_random(self):
        """Sortowanie losowej listy."""
        A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        mergesort(A)
        self.assertEqual(A, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_other_seq_type(self):
        """Sortowanie listy z elementami innego typu."""
        A = list("ala ma kota")
        mergesort(A)
        self.assertEqual(A, [" ", " ", "a", "a", "a", "a", "k", "l", "m", "o", "t"])

    def test_longer(self):
        """Test dla dłuższej sekwencji."""
        A = list(range(100, 0, -1))
        mergesort(A)
        self.assertEqual(A, list(range(1, 101)))


if __name__ == "__main__":
    unittest.main()
