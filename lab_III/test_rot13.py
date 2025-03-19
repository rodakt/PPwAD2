"""Testy jednostkowe dla modułu rot13."""

import unittest
import string

from rot13 import is_ascii, rot13, rot47


class TestIsAscii(unittest.TestCase):
    """Testy jednostkowe dla funkcji is_ascii()"""

    def test_1_is_ascii_empty_sequence(self):
        """Test dla pustego ciągu znaków."""
        s = ""
        self.assertTrue(
            is_ascii(s),
            f"is_ascii({s}) nie zwróciło oczekiwanej wartości True",
        )

    def test_2_is_ascii_ascii_sequence(self):
        """Test dla wszystkich znaków ASCII."""
        s = ""
        for i in range(128):
            s += chr(i)
            self.assertTrue(
                is_ascii(s),
                f"is_ascii({s}) nie zwróciło oczekiwanej wartości True",
            )

    def test_3_is_ascii_non_ascii_sequence(self):
        """Test dla ciągu znaków zawierającego znaki spoza zakresu ASCII."""
        for i in range(128, 1000, 10):
            self.assertEqual(
                is_ascii("abcd" + chr(i) + "xyz"),
                False,
                f"is_ascii(abcd{chr(i)}xyz) nie zwróciło oczekiwanej wartości False",
            )


class TestRot13(unittest.TestCase):
    """Testy jednostkowe dla funkcji rot13()"""

    def test_1_rot13_empty_sequence(self):
        """Test dla pustego ciągu znaków."""
        self.assertEqual(
            rot13(""),
            "",
            "rot13('') nie zwróciło oczekiwanej wartości ''",
        )

    def test_2_rot13_latin_alphabet(self):
        """Test dla alfabetu łacińskiego."""
        self.assertEqual(
            rot13(string.ascii_lowercase),
            string.ascii_lowercase[13:] + string.ascii_lowercase[:13],
            f"rot13({string.ascii_lowercase}) nie zwróciło "
            "oczekiwanej wartości 'nopqrstuvwxyzabcdefghijklm'",
        )
        self.assertEqual(
            rot13(string.ascii_uppercase),
            string.ascii_uppercase[13:] + string.ascii_uppercase[:13],
            f"rot13({string.ascii_uppercase}) nie zwróciło "
            "oczekiwanej wartości 'NOPQRSTUVWXYZABCDEFGHIJKLM'",
        )

    def test_3_rot13_ascii_sequence(self):
        """Test dla ciągu znaków zawierającego tylko znaki ASCII."""
        s = "The quick brown fox jumps over the lazy dog."
        self.assertEqual(
            rot13(s),
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
            f"rot13({s}) nie zwróciło oczekiwanej wartości 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'",
        )

    def test_4_rot13_non_ascii_sequence(self):
        """Test dla ciągu znaków zawierającego znaki spoza zakresu ASCII."""
        s = "zażółć gęślą jaźń"
        self.assertEqual(
            rot13(s),
            "mnżółć tęśyą wnźń",
            f"rot13({s}) nie zwróciło oczekiwanej wartości 'mnżółć tęślą wnźń'",
        )

    def test_5_rot13_ascii_only(self):
        """Test wyjątku ValueError dla ciągu znaków zawierającego znaki spoza zakresu ASCII."""
        s = "zażółć gęślą jaźń"
        with self.assertRaises(ValueError) as cm:
            rot13(s, use_ascii_only=True)
        self.assertEqual(str(cm.exception), "znaleziono znak spoza zakresu ASCII")


class TestRot47(unittest.TestCase):
    """Testy jednostkowe dla funkcji rot47()"""

    def test_1_rot47_empty_sequence(self):
        """Test dla pustego ciągu znaków."""
        self.assertEqual(
            rot47(""),
            "",
            "rot47('') nie zwróciło oczekiwanej wartości ''",
        )

    def test_2_rot47_single_character(self):
        """Test dla wszystkich znaków ASCII."""
        for i in range(33, 126):
            if i + 47 < 127:
                self.assertEqual(
                    rot47(chr(i)),
                    chr(i + 47),
                    f"rot47({chr(i)}) nie zwróciło oczekiwanej wartości {chr(i + 47)}",
                )
            else:
                self.assertEqual(
                    rot47(chr(i)),
                    chr(i + 47 - 127 + 33),
                    f"rot47({chr(i)}) nie zwróciło oczekiwanej wartości {chr(i + 47 - 127 + 33)}",
                )

    def test_3_rot47_ascii_sequence(self):
        """Test dla ciągu znaków zawierającego tylko znaki ASCII."""
        s = "012"
        self.assertEqual(
            rot47(s),
            chr(ord("0") + 47) + chr(ord("1") + 47) + chr(ord("2") + 47),
            f"rot47({s}) nie zwróciło "
            "oczekiwanej wartości {chr(ord('0') + 47) + chr(ord('1') + 47) + chr(ord('2') + 47)}",
        )

    def test_4_rot47_non_ascii_sequence(self):
        """Test dla ciągu znaków zawierającego znaki spoza zakresu ASCII."""
        s = "01ą2"
        self.assertEqual(
            rot47(s),
            chr(ord("0") + 47) + chr(ord("1") + 47) + "ą" + chr(ord("2") + 47),
            f"rot47({s}) nie zwróciło "
            "oczekiwanej wartości {chr(ord('0') + 47) + chr(ord('1') + 47) + 'ą' + chr(ord('2') + 47)}",
        )

    def test_5_rot47_ascii_only(self):
        """Test wyjątku ValueError dla ciągu znaków zawierającego znaki spoza zakresu ASCII."""
        s = "zażółć gęślą jaźń"
        with self.assertRaises(ValueError) as cm:
            rot47(s, use_ascii_only=True)
        self.assertEqual(str(cm.exception), "znaleziono znak spoza zakresu ASCII")


if __name__ == "__main__":
    unittest.main(verbosity=1)
