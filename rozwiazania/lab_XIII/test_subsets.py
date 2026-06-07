import unittest
from subsets import subsets_with_sum


class TestSubsetsWithSum(unittest.TestCase):

    def test_przyklad_z_docstringa_1(self):
        self.assertEqual(subsets_with_sum([2, 3, 5, 7], 10), [(3, 7), (2, 3, 5)])

    def test_przyklad_z_docstringa_2(self):
        self.assertEqual(subsets_with_sum([1, 2, 3, 4, 5], 5), [(5,), (1, 4), (2, 3)])

    def test_brak_rozwiazania(self):
        self.assertEqual(subsets_with_sum([1, 2, 3], 100), [])

    def test_jeden_element_trafny(self):
        self.assertEqual(subsets_with_sum([5], 5), [(5,)])

    def test_jeden_element_chybiony(self):
        self.assertEqual(subsets_with_sum([5], 3), [])

    def test_powtarzajace_sie_wartosci(self):
        # dwa razy 1 w liście — combinations traktuje je jako różne elementy
        self.assertEqual(subsets_with_sum([1, 1, 2], 2), [(2,), (1, 1)])

    def test_kolejnosc_elementow_z_numbers(self):
        # [3, 1, 2] — podzbiór (3,) pojawia się przed (1, 2), choć 3 > 1
        self.assertEqual(subsets_with_sum([3, 1, 2], 3), [(3,), (1, 2)])

    def test_posortowane_po_licznosci(self):
        wynik = subsets_with_sum([1, 2, 3, 4, 5], 5)
        dlugosci = [len(p) for p in wynik]
        self.assertEqual(dlugosci, sorted(dlugosci))

    def test_wynik_jest_lista(self):
        self.assertIsInstance(subsets_with_sum([1, 2, 3], 3), list)

    def test_elementy_sa_krotkami(self):
        for p in subsets_with_sum([2, 3, 5, 7], 10):
            self.assertIsInstance(p, tuple)

    def test_kazdy_podzbiór_ma_poprawna_sume(self):
        for p in subsets_with_sum([2, 3, 5, 7, 11], 10):
            self.assertEqual(sum(p), 10)


if __name__ == '__main__':
    unittest.main()
