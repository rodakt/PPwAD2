import unittest
from change import make_change


def count_change(amount, coins):
    """Rekurencyjna wersja z lab IX — wyrocznia dla testów spójności."""
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)


class TestMakeChange(unittest.TestCase):

    def test_przyklad_z_docstringa_1(self):
        self.assertEqual(make_change(5, [1, 2, 5]),
                         [(5,), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)])

    def test_przyklad_z_docstringa_2(self):
        self.assertEqual(len(make_change(5, [1, 2, 5])), 4)

    def test_przyklad_z_docstringa_3(self):
        self.assertEqual(make_change(4, [2, 5]), [(2, 2)])

    def test_brak_rozwiazania(self):
        self.assertEqual(make_change(3, [2, 5]), [])

    def test_jeden_nominal(self):
        self.assertEqual(make_change(6, [2]), [(2, 2, 2)])

    def test_wynik_jest_lista(self):
        self.assertIsInstance(make_change(5, [1, 2, 5]), list)

    def test_elementy_sa_krotkami(self):
        for sposob in make_change(5, [1, 2, 5]):
            self.assertIsInstance(sposob, tuple)

    def test_kazda_krotka_posortowana(self):
        for sposob in make_change(10, [1, 2, 5]):
            self.assertEqual(list(sposob), sorted(sposob))

    def test_posortowane_po_licznosci(self):
        wynik = make_change(10, [1, 2, 5])
        dlugosci = [len(s) for s in wynik]
        self.assertEqual(dlugosci, sorted(dlugosci))

    def test_kazdy_sposob_ma_poprawna_sume(self):
        for sposob in make_change(10, [1, 2, 5]):
            self.assertEqual(sum(sposob), 10)

    def test_coins_w_dowolnej_kolejnosci(self):
        self.assertEqual(make_change(5, [5, 2, 1]),
                         [(5,), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)])

    def test_zgodnosc_z_count_change_5(self):
        self.assertEqual(len(make_change(5, [1, 2, 5])),
                         count_change(5, [1, 2, 5]))

    def test_zgodnosc_z_count_change_10(self):
        self.assertEqual(len(make_change(10, [1, 2, 5])),
                         count_change(10, [1, 2, 5]))

    def test_zgodnosc_z_count_change_brak(self):
        self.assertEqual(len(make_change(3, [2, 5])),
                         count_change(3, [2, 5]))


if __name__ == '__main__':
    unittest.main()
