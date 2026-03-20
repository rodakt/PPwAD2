"""Testy jednostkowe dla funkcji draw_from_urn() z modułu fprob."""

import unittest

from fprob import draw_from_urn


class TestDrawFromUrn(unittest.TestCase):
    """Testy jednostkowe dla funkcji draw_from_urn()."""

    def test_with_replacement_exact_test(self):
        """Dokładny test dla losowania z powtórzeniami.

        100 losowań z urny zawierającej 3 czerwone, 2 niebieskie i 0 zielonych kul.
        - funkcja powinna zwrócić 100-elementową listę kolorów kul,
        - w tej liście nie powinno być koloru "c" (zielonej kuli).
        """
        bag = draw_from_urn(100, with_replacement=True, red=3, blue=2, green=0)
        self.assertEqual(len(bag), 100)
        self.assertTrue("green" not in bag)

    def test_without_replacement_exact_test(self):
        """Dokładny test dla losowania bez powtórzeń.

        5 losowań z urny zawierającej 3 czerwone, 2 niebieskie i 0 zielonych kul.
        - funkcja powinna zwrócić 5-elementową listę kolorów kul,
        - w tej liście powinno być 3 czerwone i 2 niebieskie kule.
        """
        bag = draw_from_urn(5, with_replacement=False, red=3, blue=2, green=0)
        self.assertEqual(len(bag), 5)
        self.assertEqual(sorted(bag), ["blue", "blue", "red", "red", "red"])

    def test_with_replacement_probability_test(self):
        """Test probabilistyczny dla losowania z powtórzeniami.

        500 losowań z urny zawierającej 3 czerwone, 2 niebieskie i 1 zieloną kulę.
        - funkcja powinna zwrócić 500-elementową listę kolorów kul,
        - liczba czerwonych kul powinna być większa niż liczba niebieskich kul,
        - liczba niebieskich kul powinna być większa niż liczba zielonych kul.
        """
        bag = draw_from_urn(500, with_replacement=True, red=3, blue=2, green=1)
        self.assertEqual(len(bag), 500)
        self.assertGreater(
            bag.count("red"),
            bag.count("blue"),
            "Błąd w funkcji draw_from_urn() lub zaszło zdarzenie o prawdopodobieństwie < 3e-8",
        )
        self.assertGreater(
            bag.count("blue"),
            bag.count("green"),
            "Błąd w funkcji draw_from_urn() lub zaszło zdarzenie o prawdopodobieństwie < 3e-10",
        )

    def test_exception(self):
        """Test wyjątku ValueError."""
        with self.assertRaises(ValueError) as context:
            draw_from_urn(7, False, red=3, blue=2, green=1)
        self.assertEqual(
            str(context.exception),
            "Liczba losowań bez zwracania przekracza liczbę kul w urnie.",
        )


if __name__ == "__main__":
    unittest.main()
