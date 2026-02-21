"""Testy jednostkowe dla funkcji z modułu max_subseq."""

import unittest

from max_subseq import max_subseq


class TestMaxSubseq(unittest.TestCase):
    """Testy jednostkowe dla funkcji max_subseq."""

    def test_max_subseq_all_seq(self):
        """Predykat spełniony na całej sekwencji."""
        self.assertEqual(max_subseq([1, 2, 3, 4], lambda subseq: True), [1, 2, 3, 4])

    def test_max_subseq_empty_seq(self):
        """Predykat nie jest spełniony na żadnej niepustej podsekwencji."""
        self.assertEqual(max_subseq([1, 3, 5, 7], len), [])

    def test_max_subseq(self):
        """Predykat spełniony na niepustej podsekwencji."""
        for n in range(5, 10):
            for i in range(n - 5 + 1):
                seq = i * [0] + 5 * [1] + (n - 5 - i) * [0]
                subseq = 5 * [1]

                def pred(subeq):
                    return all(x == 1 for x in subseq)

                with self.subTest(seq=seq, subseq=subseq, pred=pred):
                    self.assertEqual(max_subseq(seq, pred), subseq)


if __name__ == "__main__":
    unittest.main()
