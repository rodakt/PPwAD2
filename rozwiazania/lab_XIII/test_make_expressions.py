import re
import unittest

from make_expressions import make_expressions


def oblicz(wyrażenie):
    """Wartość wyrażenia złożonego z liczb rozdzielonych '+' i '-'."""
    return sum(int(składnik) for składnik in re.findall(r'[+-]?\d+', wyrażenie))


class TestMakeExpressions(unittest.TestCase):

    def test_dodawanie_dwoch_cyfr(self):
        self.assertEqual(make_expressions('12', 3), ['1+2'])

    def test_odejmowanie_dwoch_cyfr(self):
        self.assertEqual(make_expressions('12', -1), ['1-2'])

    def test_sklejenie_dwoch_cyfr(self):
        self.assertEqual(make_expressions('12', 12), ['12'])

    def test_brak_rozwiazania(self):
        self.assertEqual(make_expressions('12', 99), [])

    def test_jedna_cyfra_trafna(self):
        self.assertEqual(make_expressions('1', 1), ['1'])

    def test_jedna_cyfra_chybiona(self):
        self.assertEqual(make_expressions('1', 5), [])

    def test_trzy_cyfry_suma(self):
        self.assertEqual(make_expressions('123', 6), ['1+2+3'])

    def test_trzy_cyfry_sklejenie(self):
        self.assertEqual(make_expressions('123', 123), ['123'])

    def test_posortowane_leksykograficznie(self):
        wynik = make_expressions('123456789', 100)
        self.assertEqual(wynik, sorted(wynik))

    def test_wynik_jest_lista(self):
        self.assertIsInstance(make_expressions('12', 3), list)

    def test_wszystkie_wyrazenia_rowne_celowi(self):
        for e in make_expressions('123456789', 100):
            self.assertEqual(oblicz(e), 100)

    def test_liczba_wyrazen_dla_100(self):
        self.assertEqual(len(make_expressions('123456789', 100)), 11)

    def test_znane_wyrazenie_w_wyniku(self):
        self.assertIn('1+2+3-4+5+6+78+9', make_expressions('123456789', 100))


if __name__ == '__main__':
    unittest.main()
