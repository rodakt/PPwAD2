"""Testy jednostkowe dla klas AverageSpeed i MovingAverage."""

import unittest
from moving_average import AverageSpeed, MovingAverage


class TestAverageSpeed(unittest.TestCase):
    """Testy jednostkowe dla klasy AverageSpeed."""

    def setUp(self):
        self.p = AverageSpeed()

    def test_initial_values(self):
        """Testuje wartości początkowe obiektu."""
        self.assertEqual(self.p.distance, 0)
        self.assertEqual(self.p.time, 0)

    def test_add_section(self):
        """Testuje dodawanie nowego odcinka trasy."""
        self.p.add_section(distance=30, time=15)
        self.assertEqual(self.p.distance, 30)
        self.assertEqual(self.p.time, 15)
        self.assertEqual(self.p.average_speed, 2.0)

        self.p.add_section(distance=170, time=35)
        self.assertEqual(self.p.distance, 200)
        self.assertEqual(self.p.time, 50)
        self.assertEqual(self.p.average_speed, 4.0)


class TestMovingAverage(unittest.TestCase):
    """Testy jednostkowe dla klasy MovingAverage."""

    def setUp(self):
        self.m = MovingAverage()

    def test_initial_values(self):
        """Testuje wartości początkowe obiektu."""
        self.assertEqual(self.m.total, 0)
        self.assertEqual(self.m.count, 0)

    def test_add_value(self):
        """Testuje dodawanie nowej wartości."""
        self.assertAlmostEqual(self.m.add_value(10), 10)
        self.assertAlmostEqual(self.m.add_value(20), 15)
        self.assertAlmostEqual(self.m.add_value(30), 20)
        self.assertAlmostEqual(self.m.add_value(40), (10 + 20 + 30 + 40) / 4)

    def test_independence_of_instances(self):
        """Testuje niezależność różnych instancji klasy MovingAverage."""
        m1 = MovingAverage()
        m2 = MovingAverage()
        m1.add_value(10)
        self.assertAlmostEqual(m1.add_value(20), 15)
        self.assertAlmostEqual(m2.add_value(30), 30)
        self.assertAlmostEqual(m1.add_value(40), (10 + 20 + 40) / 3)
        self.assertAlmostEqual(m2.add_value(50), 40)


if __name__ == "__main__":
    unittest.main()
