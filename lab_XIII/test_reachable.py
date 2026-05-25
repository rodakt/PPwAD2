import unittest
from reachable import reachable


class TestReachable(unittest.TestCase):

    def test_przyklad_z_docstringa(self):
        self.assertEqual(reachable([1, 2, 3]), [-4, 0, 2, 6])

    def test_jeden_element(self):
        self.assertEqual(reachable([5]), [5])

    def test_dwa_jednakowe(self):
        self.assertEqual(reachable([10, 10]), [0, 20])

    def test_zero(self):
        self.assertEqual(reachable([0]), [0])

    def test_dwa_elementy_rozne(self):
        # 3+7=10, 3-7=-4
        self.assertEqual(reachable([3, 7]), [-4, 10])

    def test_duplikaty_wynikow(self):
        # 2+2+2=6, 2+2-2=2, 2-2+2=2, 2-2-2=-2 → unikalne: [-2, 2, 6]
        self.assertEqual(reachable([2, 2, 2]), [-2, 2, 6])

    def test_ujemne(self):
        # -1+2=1, -1-2=-3
        self.assertEqual(reachable([-1, 2]), [-3, 1])

    def test_wynik_posortowany(self):
        wynik = reachable([4, 1, 2])
        self.assertEqual(wynik, sorted(wynik))

    def test_wynik_jest_lista(self):
        self.assertIsInstance(reachable([1, 2]), list)

    def test_brak_powtorzen(self):
        wynik = reachable([3, 3, 3])
        self.assertEqual(len(wynik), len(set(wynik)))


if __name__ == '__main__':
    unittest.main()
