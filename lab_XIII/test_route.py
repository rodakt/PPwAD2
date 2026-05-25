import unittest
from route import shortest_route

M2 = [[0, 5],
      [5, 0]]

M3 = [[0, 1, 2],
      [1, 0, 3],
      [2, 3, 0]]

M4 = [[0, 10, 15, 20],
      [10,  0, 35, 25],
      [15, 35,  0, 30],
      [20, 25, 30,  0]]


class TestShortestRoute(unittest.TestCase):

    def test_dwa_miasta(self):
        self.assertEqual(shortest_route(M2), (10, (0, 1, 0)))

    def test_trzy_miasta(self):
        dlugosc, trasa = shortest_route(M3)
        self.assertEqual(dlugosc, 6)
        self.assertIn(trasa, [(0, 1, 2, 0), (0, 2, 1, 0)])

    def test_cztery_miasta(self):
        dlugosc, trasa = shortest_route(M4)
        self.assertEqual(dlugosc, 80)
        self.assertIn(trasa, [(0, 1, 3, 2, 0), (0, 2, 3, 1, 0)])

    def test_wynik_jest_krotka(self):
        self.assertIsInstance(shortest_route(M4), tuple)

    def test_trasa_jest_krotka(self):
        _, trasa = shortest_route(M4)
        self.assertIsInstance(trasa, tuple)

    def test_trasa_zaczyna_sie_w_zero(self):
        _, trasa = shortest_route(M4)
        self.assertEqual(trasa[0], 0)

    def test_trasa_konczy_sie_w_zero(self):
        _, trasa = shortest_route(M4)
        self.assertEqual(trasa[-1], 0)

    def test_trasa_zawiera_wszystkie_miasta(self):
        n = len(M4)
        _, trasa = shortest_route(M4)
        self.assertEqual(sorted(trasa[1:-1]), list(range(1, n)))

    def test_dlugosc_zgodna_z_trasa(self):
        dlugosc, trasa = shortest_route(M4)
        oczekiwana = sum(M4[trasa[i]][trasa[i + 1]] for i in range(len(trasa) - 1))
        self.assertEqual(dlugosc, oczekiwana)


if __name__ == '__main__':
    unittest.main()
