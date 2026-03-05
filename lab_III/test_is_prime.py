"""Testy jednostkowe dla modułu is_prime."""

import unittest

from is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    """Testy jednostkowe dla funkcji is_prime()"""

    def test_1_small_primes(self):
        """Testy dla małych liczb pierwszych."""
        for p in [2, 3, 5, 7, 11, 13]:
            self.assertTrue(is_prime(p), f"{p} jest liczbą pierwszą")

    def test_2_small_composites(self):
        """Testy dla małych liczb złożonych."""
        for n in [4, 6, 8, 9, 10, 12, 15]:
            self.assertFalse(is_prime(n), f"{n} nie jest liczbą pierwszą")

    def test_3_edge_cases(self):
        """0 i 1 nie są liczbami pierwszymi."""
        self.assertFalse(is_prime(0), "0 nie jest liczbą pierwszą")
        self.assertFalse(is_prime(1), "1 nie jest liczbą pierwszą")

    def test_4_larger_prime(self):
        """Test dla większej liczby pierwszej."""
        self.assertTrue(is_prime(7919), "7919 jest liczbą pierwszą")

    def test_5_larger_composite(self):
        """Test dla większej liczby złożonej."""
        self.assertFalse(is_prime(7918), "7918 nie jest liczbą pierwszą")

    def test_6_negative_argument(self):
        """Dla n < 0 funkcja zgłasza ValueError."""
        with self.assertRaises(ValueError) as cm:
            is_prime(-5)
        self.assertEqual(str(cm.exception), "argument musi być nieujemny")


if __name__ == "__main__":
    unittest.main(verbosity=1)
