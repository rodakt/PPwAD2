"""Testy jednostkowe dla funkcji qsort z modułu qsort."""

import unittest
from qsort import qsort


class TestQSort(unittest.TestCase):

    def test_empty(self):
        """Pusta lista powinna pozostać pusta."""
        self.assertEqual(qsort([]), [])

    def test_single(self):
        """Lista jednoelementowa powinna pozostać niezmieniona."""
        self.assertEqual(qsort([42]), [42])

    def test_sorted(self):
        """Posortowana lista powinna pozostać niezmieniona."""
        self.assertEqual(qsort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reversed(self):
        """Sortowanie listy malejącej."""
        self.assertEqual(qsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random(self):
        """Sortowanie losowej listy."""
        self.assertEqual(
            qsort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        )

    def test_other_seq_type(self):
        """Sortowanie sekwencji innej niż lista."""
        self.assertEqual(
            qsort("ala ma kota"),
            [" ", " ", "a", "a", "a", "a", "k", "l", "m", "o", "t"],
        )

    def test_longer(self):
        """Test dla dłuższej sekwencji."""
        seq = range(100, 0, -1)
        self.assertEqual(qsort(seq), list(range(1, 101)))


if __name__ == "__main__":
    unittest.main()
