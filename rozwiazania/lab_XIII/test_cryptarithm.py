import unittest
from cryptarithm import solve_cryptarithm


class TestSolveCryptarithm(unittest.TestCase):

    def test_prosty_przyklad_dokladny(self):
        # A + A == B: A in 1..4 (bo 2*A <= 9), B = 2*A, A != B
        self.assertEqual(
            solve_cryptarithm('A', 'A', 'B'),
            [(1, 1, 2), (2, 2, 4), (3, 3, 6), (4, 4, 8)],
        )

    def test_wynik_jest_lista(self):
        self.assertIsInstance(solve_cryptarithm('A', 'A', 'B'), list)

    def test_kazde_rozwiazanie_jest_krotka(self):
        for sol in solve_cryptarithm('A', 'A', 'B'):
            self.assertIsInstance(sol, tuple)

    def test_dlugosc_krotki_rowna_liczbie_slow(self):
        words = ('A', 'A', 'B')
        for sol in solve_cryptarithm(*words):
            self.assertEqual(len(sol), len(words))

    def test_suma_skladnikow_rowna_wynikowi(self):
        for sol in solve_cryptarithm('A', 'A', 'B'):
            self.assertEqual(sum(sol[:-1]), sol[-1])

    def test_brak_zera_wiodacego(self):
        # każda wartość musi być >= 10^(len(slowo)-1)
        words = ('A', 'A', 'B')
        for sol in solve_cryptarithm(*words):
            for word, val in zip(words, sol):
                self.assertGreaterEqual(val, 10 ** (len(word) - 1))

    def test_send_more_money_jedno_rozwiazanie(self):
        self.assertEqual(len(solve_cryptarithm('SEND', 'MORE', 'MONEY')), 1)

    def test_send_more_money_znane_rozwiazanie(self):
        # jedyne rozwiązanie: S=9 E=5 N=6 D=7 M=1 O=0 R=8 Y=2
        self.assertIn((9567, 1085, 10652), solve_cryptarithm('SEND', 'MORE', 'MONEY'))

    def test_send_more_money_suma(self):
        sol = solve_cryptarithm('SEND', 'MORE', 'MONEY')[0]
        self.assertEqual(sol[0] + sol[1], sol[2])

    def test_send_more_money_brak_zera_wiodacego(self):
        words = ('SEND', 'MORE', 'MONEY')
        for sol in solve_cryptarithm(*words):
            for word, val in zip(words, sol):
                self.assertGreaterEqual(val, 10 ** (len(word) - 1))

    def test_two_two_four_wiele_rozwiazan(self):
        self.assertGreater(len(solve_cryptarithm('TWO', 'TWO', 'FOUR')), 1)


if __name__ == '__main__':
    unittest.main()
