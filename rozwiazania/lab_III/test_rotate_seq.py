"""Testy jednostkowe dla modułu rotate_seq."""

import unittest

from rotate_seq import rotate, rotate_left, rotate_right


class TestRotate(unittest.TestCase):
    """Testy jednostkowe dla funkcji rotate()"""

    def test_1_rotate_different_seq_types(self):
        """Testy dla różnych typów sekwencji"""
        s = "abc"
        lst = list(s)
        tp = tuple(s)
        self.assertEqual(
            rotate(s, 3),
            "abc",
            "rotate('abc', 3) nie zwróciło oczekiwanej wartości 'abc'",
        )
        self.assertEqual(
            rotate(lst, 3),
            ["a", "b", "c"],
            "rotate(['a', 'b', 'c'], 3) nie zwróciło oczekiwanej wartości ['a', 'b', 'c']",
        )
        self.assertEqual(
            rotate(tp, 3),
            ("a", "b", "c"),
            "rotate(('a', 'b', 'c'), 3) nie zwróciło oczekiwanej wartości ('a', 'b', 'c')",
        )

    def test_2_rotate_empty_sequence(self):
        """Testy dla pustej sekwencji"""
        self.assertEqual(
            rotate("", 0),
            "",
            "rotate('', 0) nie zwróciło oczekiwanej wartości ''",
        )
        self.assertEqual(
            rotate("", 1),
            "",
            "rotate('', 1) nie zwróciło oczekiwanej wartości ''",
        )
        self.assertEqual(
            rotate("", -2),
            "",
            "rotate('', -2) nie zwróciło oczekiwanej wartości ''",
        )

    def test_3_rotate_single_element_sequence(self):
        """Testy dla sekwencji składającej się z jednego elementu"""
        self.assertEqual(
            rotate("a", 0),
            "a",
            "rotate('a', 0) nie zwróciło oczekiwanej wartości 'a'",
        )
        self.assertEqual(
            rotate("a", 1),
            "a",
            "rotate('a', 1) nie zwróciło oczekiwanej wartości 'a'",
        )
        self.assertEqual(
            rotate("a", -2),
            "a",
            "rotate('a', -2) nie zwróciło oczekiwanej wartości 'a'",
        )

    def test_4_rotate_identity(self):
        """Testy dla rotacji o wielokrotność długości sekwencji"""
        seq = list("abcdefgh")
        n = len(seq)
        for i in range(-2 * n, 2 * n + 1, n):
            self.assertEqual(
                rotate(seq, i),
                seq,
                f"rotate({seq}, {i}) nie zwróciło oczekiwanej wartości {seq}",
            )

    def test_5_rotate_longer_sequence(self):
        """Testy dla dłuższej sekwencji"""
        seq = list(range(10))
        self.assertEqual(
            rotate(seq, 0),
            seq,
            f"rotate({seq}, 0) nie zwróciło oczekiwanej wartości {seq}",
        )
        self.assertEqual(
            rotate(seq, 1),
            [9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
            f"rotate({seq}, 1) nie zwróciło oczekiwanej wartości [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]",
        )
        self.assertEqual(
            rotate(seq, -4),
            [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],
            f"rotate({seq}, -4) nie zwróciło oczekiwanej wartości [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]",
        )

    def test_6_rotate_big_n(self):
        """Testy dla dużego n"""
        seq = ["A", "B", "C"]
        self.assertEqual(
            rotate(seq, 3 * 10**6 + 1),
            ["C", "A", "B"],
            "rotate(['A', 'B', 'C'], 3*10**6 + 1) nie zwróciło oczekiwanej wartości ['C', 'A', 'B']",
        )
        self.assertEqual(
            rotate(seq, -3 * 10**6 - 1),
            ["B", "C", "A"],
            "rotate(['A', 'B', 'C'], -3*10**6 - 1) nie zwróciło oczekiwanej wartości ['B', 'C', 'A']",
        )


class TestRotateLeft(unittest.TestCase):
    """Testy jednostkowe dla funkcji rotate_left()"""

    def test_1_rotate_left_different_seq_types(self):
        """Testy dla różnych typów sekwencji"""
        s = "abc"
        lst = list(s)
        tp = tuple(s)
        self.assertEqual(
            rotate_left(s, 3),
            "abc",
            "rotate_left('abc', 3) nie zwróciło oczekiwanej wartości 'abc'",
        )
        self.assertEqual(
            rotate_left(lst, 3),
            ["a", "b", "c"],
            "rotate_left(['a', 'b', 'c'], 3) nie zwróciło oczekiwanej wartości ['a', 'b', 'c']",
        )
        self.assertEqual(
            rotate_left(tp, 3),
            ("a", "b", "c"),
            "rotate_left(('a', 'b', 'c'), 3) nie zwróciło oczekiwanej wartości ('a', 'b', 'c')",
        )

    def test_2_rotate_left_empty_sequence(self):
        """Testy dla pustej sekwencji"""
        self.assertEqual(
            rotate_left("", 0),
            "",
            "rotate_left('', 0) nie zwróciło oczekiwanej wartości ''",
        )
        self.assertEqual(
            rotate_left("", 1),
            "",
            "rotate_left('', 1) nie zwróciło oczekiwanej wartości ''",
        )

    def test_3_rotate_left_single_element_sequence(self):
        """Testy dla sekwencji składającej się z jednego elementu"""
        self.assertEqual(
            rotate_left("a", 0),
            "a",
            "rotate_left('a', 0) nie zwróciło oczekiwanej wartości 'a'",
        )
        self.assertEqual(
            rotate_left("a", 1),
            "a",
            "rotate_left('a', 1) nie zwróciło oczekiwanej wartości 'a'",
        )

    def test_4_rotate_left_identity(self):
        """Testy dla rotacji o wielokrotność długości sekwencji"""
        seq = list("abcdefgh")
        n = len(seq)
        for i in [0, n, 2 * n]:
            self.assertEqual(
                rotate_left(seq, i),
                seq,
                f"rotate_left({seq}, {i}) nie zwróciło oczekiwanej wartości {seq}",
            )

    def test_5_rotate_left_longer_sequence(self):
        """Testy dla dłuższej sekwencji"""
        seq = list(range(10))
        self.assertEqual(
            rotate_left(seq, 0),
            seq,
            f"rotate_left({seq}, 0) nie zwróciło oczekiwanej wartości {seq}",
        )
        self.assertEqual(
            rotate_left(seq, 1),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            f"rotate_left({seq}, 1) nie zwróciło oczekiwanej wartości [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]",
        )
        self.assertEqual(
            rotate_left(seq, 4),
            [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],
            f"rotate_left({seq}, 4) nie zwróciło oczekiwanej wartości [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]",
        )

    def test_6_rotate_left_negative_shift(self):
        """Testy dla ujemnego przesunięcia"""
        seq = list(range(10))
        with self.assertRaises(ValueError) as cm:
            rotate_left(seq, -1)
        self.assertEqual(str(cm.exception), "n musi być liczbą nieujemną")

    def test_7_rotate_left_big_n(self):
        """Testy dla dużego n"""
        seq = ["A", "B", "C"]
        self.assertEqual(
            rotate_left(seq, 3 * 10**6 + 1),
            ["B", "C", "A"],
            "rotate_left(['A', 'B', 'C'], 3*10**6 + 1) nie zwróciło oczekiwanej wartości ['B', 'C', 'A']",
        )


class TestRotateRight(unittest.TestCase):
    """Testy jednostkowe dla funkcji rotate_right()"""

    def test_1_rotate_right_different_seq_types(self):
        """Testy dla różnych typów sekwencji"""
        s = "abc"
        lst = list(s)
        tp = tuple(s)
        self.assertEqual(
            rotate_right(s, 3),
            "abc",
            "rotate_right('abc', 3) nie zwróciło oczekiwanej wartości 'abc'",
        )
        self.assertEqual(
            rotate_right(lst, 3),
            ["a", "b", "c"],
            "rotate_right(['a', 'b', 'c'], 3) nie zwróciło oczekiwanej wartości ['a', 'b', 'c']",
        )
        self.assertEqual(
            rotate_right(tp, 3),
            ("a", "b", "c"),
            "rotate_right(('a', 'b', 'c'), 3) nie zwróciło oczekiwanej wartości ('a', 'b', 'c')",
        )

    def test_2_rotate_right_empty_sequence(self):
        """Testy dla pustej sekwencji"""
        self.assertEqual(
            rotate_right("", 0),
            "",
            "rotate_right('', 0) nie zwróciło oczekiwanej wartości ''",
        )
        self.assertEqual(
            rotate_right("", 1),
            "",
            "rotate_right('', 1) nie zwróciło oczekiwanej wartości ''",
        )

    def test_3_rotate_right_single_element_sequence(self):
        """Testy dla sekwencji składającej się z jednego elementu"""
        self.assertEqual(
            rotate_right("a", 0),
            "a",
            "rotate_right('a', 0) nie zwróciło oczekiwanej wartości 'a'",
        )
        self.assertEqual(
            rotate_right("a", 1),
            "a",
            "rotate_right('a', 1) nie zwróciło oczekiwanej wartości 'a'",
        )

    def test_4_rotate_right_identity(self):
        """Testy dla rotacji o wielokrotność długości sekwencji"""
        seq = list("abcdefgh")
        n = len(seq)
        for i in [0, n, 2 * n]:
            self.assertEqual(
                rotate_right(seq, i),
                seq,
                f"rotate_right({seq}, {i}) nie zwróciło oczekiwanej wartości {seq}",
            )

    def test_5_rotate_right_longer_sequence(self):
        """Testy dla dłuższej sekwencji"""
        seq = list(range(10))
        self.assertEqual(
            rotate_right(seq, 0),
            seq,
            f"rotate_right({seq}, 0) nie zwróciło oczekiwanej wartości {seq}",
        )
        self.assertEqual(
            rotate_right(seq, 1),
            [9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
            f"rotate_right({seq}, 1) nie zwróciło oczekiwanej wartości [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]",
        )
        self.assertEqual(
            rotate_right(seq, 4),
            [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
            f"rotate_right({seq}, 4) nie zwróciło oczekiwanej wartości [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]",
        )

    def test_6_rotate_right_negative_shift(self):
        """Testy dla ujemnego przesunięcia"""
        seq = list(range(10))
        with self.assertRaises(ValueError) as cm:
            rotate_right(seq, -1)
        self.assertEqual(str(cm.exception), "n musi być liczbą nieujemną")

    def test_7_rotate_right_big_n(self):
        """Testy dla dużego n"""
        seq = ["A", "B", "C"]
        self.assertEqual(
            rotate_right(seq, 3 * 10**6 + 1),
            ["C", "A", "B"],
            "rotate_right(['A', 'B', 'C'], 3*10**6 + 1) nie zwróciło oczekiwanej wartości ['C', 'A', 'B']",
        )


class TestIntegrationTests(unittest.TestCase):
    """Testy integracyjne dla funkcji rotate(), rotate_left() i rotate_right()"""

    def test_1_rotate_left_and_right(self):
        """Testy dla rotate_left() i rotate_right() jako odwrotności siebie"""
        seq = list(range(10))
        for i in range(10):
            self.assertEqual(
                rotate_right(rotate_left(seq, i), i),
                seq,
                f"rotate_right(rotate_left(seq, {i}), {i}) != seq",
            )

    def test_2_rotate_and_rotate_right(self):
        """200 razy rotate(1) plus rotate_right(800) dla sekwencji 1000 elementowej"""
        seq = list(range(1000))
        new_seq = seq[:]
        for _ in range(200):
            new_seq = rotate(new_seq, 1)
        self.assertEqual(
            seq,
            rotate_right(new_seq, 800),
            "rotate(1) 200 razy + rotate_right(800) != seq",
        )

    def test_3_rotate_and_rotate_left(self):
        """200 razy rotate(-1) plus rotate_left(800) dla sekwencji 1000 elementowej"""
        seq = list(range(1000))
        new_seq = seq[:]
        for _ in range(200):
            new_seq = rotate(new_seq, -1)
        self.assertEqual(
            seq,
            rotate_left(new_seq, 800),
            "rotate(-1) 200 razy + rotate_left(800) != seq",
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
