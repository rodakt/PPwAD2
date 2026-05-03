"""Testy jednostkowe dla modułu temperature."""

import unittest
from temperature import Temperature

# Jednostki temperatury.
UNITS = "K C F".split()

# Temeratura wrzenia wody.
BOLING_POINT = [("K", 373.15), ("C", 100), ("F", 212)]


class TestTemperature(unittest.TestCase):
    """Testy jednostkowe dla klasy Temperature."""

    def test_temperature(self):
        """Testy konstruktora klasy Temperature."""
        temp = Temperature()
        self.assertEqual(temp.value, 0)
        self.assertEqual(temp.unit, "K")

        temp = Temperature(200)
        self.assertEqual(temp.value, 200)
        self.assertEqual(temp.unit, "K")

        temp = Temperature(10, unit="C")
        self.assertEqual(temp.value, 10)
        self.assertEqual(temp.unit, "C")

        temp = Temperature(20, unit="F")
        self.assertEqual(temp.value, 20)
        self.assertEqual(temp.unit, "F")

    def test_converters(self):
        """Testy konwersji jednostek."""
        for unit0, t0 in BOLING_POINT:
            for unit1, t1 in BOLING_POINT:
                temp = Temperature(value=t0, unit=unit0)
                temp.convert(unit1)
                self.assertAlmostEqual(temp.value, t1, msg=f"{unit0} -> {unit1}")

    def test_circular_conversion(self):
        """Test przeliczania "w kółko"."""
        temp = Temperature()
        temp.convert("F")
        temp.convert("C")
        temp.convert("K")
        self.assertAlmostEqual(temp.value, 0)

    def test_repr(self):
        """Test formalnej reprezentacji tekstowej."""
        temp = Temperature(100, "C")
        self.assertEqual(repr(temp), "Temperature(100, 'C')")

        temp = Temperature(100, "F")
        self.assertEqual(repr(temp), "Temperature(100, 'F')")

        temp = Temperature(100, "K")
        self.assertEqual(repr(temp), "Temperature(100, 'K')")

    def test_str(self):
        """Test nieformalnej reprezentacji tekstowej."""
        temp = Temperature(100, "C")
        self.assertEqual(str(temp), "100°C")

        temp = Temperature(100, "F")
        self.assertEqual(str(temp), "100°F")

        temp = Temperature(100, "K")
        self.assertEqual(str(temp), "100 K")


if __name__ == "__main__":
    unittest.main()
