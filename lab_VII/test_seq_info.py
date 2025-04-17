"""Moduł zawiera testy dla funkcji z modułu seq_info"""

import unittest

from seq_info import *

STRICTLY_ASCENDING_SEQS = [
    [1, 2, 3],
    [1, 2, 3, 10],
    range(1, 10),
    [i**2 for i in range(10)],
]

STRICTLY_DESCENDING_SEQS = [
    [3, 2, 1],
    [10, 3, 2, 1],
    range(10, 0, -1),
    [i**2 for i in range(10, 0, -1)],
]

NON_STRICTLY_ASCENDING_SEQS = [
    [1, 1, 1],
    [1, 2, 2],
    [1, 5, 5, 10],
    100 * [1] + [2] + 100 * [3],
]

NON_STRICTLY_DESCENDING_SEQS = [
    [1, 1, 1],
    [2, 2, 1],
    [10, 5, 5, 1],
    100 * [3] + [2] + 100 * [1],
]

ASCENDING_SEQS = STRICTLY_ASCENDING_SEQS + NON_STRICTLY_ASCENDING_SEQS
DESCENDING_SEQS = STRICTLY_DESCENDING_SEQS + NON_STRICTLY_DESCENDING_SEQS
MONOTONIC_SEQS = ASCENDING_SEQS + DESCENDING_SEQS
STRICTLY_MONOTONIC_SEQS = STRICTLY_ASCENDING_SEQS + STRICTLY_DESCENDING_SEQS

NON_MONOTONIC_SEQS = [
    [1, 2, 3, 2],
    [1, 2, 2, 1],
    [1, 2, 1, 2],
    [1, 2, 3, 1],
    [1, 2, 3, 1, 2],
    [1, 2, 3, 1, 2, 3],
    [1, 2, 3, 1, 2, 3, 1],
    [1, 2, 3, 1, 2, 3, 1, 2],
    [1, 2, 3, 1, 2, 3, 1, 2, 3],
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
    tuple(range(10)) + (0,),
    [i**2 for i in range(-10, 10)],
]

CONSTANT_SEQS = [
    [5, 5],
    [1, 1, 1],
    10 * [0],
]

NON_CONSTANT_SEQS = [
    [5, 10],
    [1, 1, 2],
    [1, 2, 1],
    [1, 2, 3],
    [1, 2, 3, 1],
    [1, 2, 3, 1, 2],
    range(10),
]

ALTERNATING_SEQS = [
    [5, -2],
    [-5, 2],
    [1, -1, 1],
    [-1, 1, -1],
    [1, -1, 1, -1],
    [-3, 2, -1, 3],
]

NON_ALTERNATING_SEQS = [
    [1, 2],
    [1, -2, -5],
    [-3, -4, -5],
    [-3, -4, 5],
    [-3, 2, -1, -4],
]

ARITHMETIC_SEQS = [
    [1, 5],
    [1, 3, 5],
    [1, 4, 7, 10],
    range(1, 1000, 3),
    range(1000, 1, -4),
]

NON_ARITHMETIC_SEQS = [[1, 3, 6], [1, 4, 7, 10, 15], [10, 9, 8, 7, 6, 0]]

GEOMETRIC_SEQS = [
    [1, 2],
    [1, 2, 4],
    [2 * 7**i for i in range(10)],
    [(-2) ** i for i in range(10)],
]


NON_GEOMETRIC_SEQS = [
    [1, 3, 8],
    [1, 3, 4, 8, 16],
]


class TestIsAscending(unittest.TestCase):
    """Testy funkcji is_ascending()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_ascending([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_ascending([1]))

    def test_is_ascending_positive(self):
        """Test dla sekwencji rosnącej"""
        for seq in ASCENDING_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_ascending(seq), seq)

    def test_is_ascending_negative(self):
        """Test dla sekwencji, które nie są rosnące"""
        for seq in NON_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_ascending(seq), seq)


class TestIsDescending(unittest.TestCase):
    """Testy funkcji is_descending()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_descending([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_descending([1]))

    def test_is_descending_positive(self):
        """Test dla sekwencji malejącej"""
        for seq in DESCENDING_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_descending(seq), seq)

    def test_is_descending_negative(self):
        """Test dla sekwencji, które nie są malejące"""
        for seq in NON_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_descending(seq), seq)


class TestIsStrictlyAscending(unittest.TestCase):
    """Testy funkcji is_strictly_ascending()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_strictly_ascending([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_strictly_ascending([1]))

    def test_is_strictly_ascending_positive(self):
        """Test dla sekwencji ściśle rosnącej"""
        for seq in STRICTLY_ASCENDING_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_strictly_ascending(seq), seq)

    def test_is_strictly_ascending_negative(self):
        """Test dla sekwencji, które nie są ściśle rosnące"""
        for seq in NON_STRICTLY_ASCENDING_SEQS + NON_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_strictly_ascending(seq), seq)


class TestIsStrictlyDescending(unittest.TestCase):
    """Testy funkcji is_strictly_descending()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_strictly_descending([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_strictly_descending([1]))

    def test_is_strictly_descending_positive(self):
        """Test dla sekwencji ściśle malejącej"""
        for seq in STRICTLY_DESCENDING_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_strictly_descending(seq), seq)

    def test_is_strictly_descending_negative(self):
        """Test dla sekwencji, które nie są ściśle malejące"""
        for seq in NON_STRICTLY_DESCENDING_SEQS + NON_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_strictly_descending(seq), seq)


class TestIsMonotonic(unittest.TestCase):
    """Testy funkcji is_monotonic()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_monotonic([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_monotonic([1]))

    def test_is_monotonic_positive(self):
        """Test dla sekwencji monotonicznej"""
        for seq in MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_monotonic(seq), seq)

    def test_is_monotonic_negative(self):
        """Test dla sekwencji, które nie są monotoniczne"""
        for seq in NON_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_monotonic(seq), seq)


class TestIsStrictlyMonotonic(unittest.TestCase):
    """Testy funkcji is_strictly_monotonic()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_strictly_monotonic([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_strictly_monotonic([1]))

    def test_is_strictly_monotonic_positive(self):
        """Test dla sekwencji ściśle monotonicznej"""
        for seq in STRICTLY_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_strictly_monotonic(seq), seq)

    def test_is_strictly_monotonic_negative(self):
        """Test dla sekwencji, które nie są ściśle monotoniczne"""
        for seq in NON_MONOTONIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_strictly_monotonic(seq), seq)


class TestIsConstant(unittest.TestCase):
    """Testy funkcji is_constant()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_constant([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_constant([1]))

    def test_is_constant_positive(self):
        """Test dla sekwencji stałej"""
        for seq in CONSTANT_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_constant(seq), seq)

    def test_is_constant_negative(self):
        """Test dla sekwencji, które nie są stałe"""
        for seq in NON_CONSTANT_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_constant(seq), seq)


class TestIsAlternating(unittest.TestCase):
    """Testy funkcji is_alternating()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_alternating([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_alternating([1]))

    def test_is_alternating_positive(self):
        """Test dla sekwencji naprzemiennych"""
        for seq in ALTERNATING_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_alternating(seq), seq)

    def test_is_alternating_negative(self):
        """Test dla sekwencji, które nie są naprzemienne"""
        for seq in NON_ALTERNATING_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_alternating(seq), seq)


class TestIsArithmetic(unittest.TestCase):
    """Testy funkcji is_arithmetic()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_arithmetic([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_arithmetic([1]))

    def test_is_arithmetic_positive(self):
        """Test dla sekwencji arytmetycznych"""
        for seq in ARITHMETIC_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_arithmetic(seq), seq)

    def test_is_arithmetic_negative(self):
        """Test dla sekwencji, które nie są arytmetyczne"""
        for seq in NON_ARITHMETIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_arithmetic(seq), seq)


class TestIsGeometric(unittest.TestCase):
    """Testy funkcji is_geometric()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(is_geometric([]))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(is_geometric([1]))

    def test_is_geometric_positive(self):
        """Test dla sekwencji geometrycznych"""
        for seq in GEOMETRIC_SEQS:
            with self.subTest(seq=seq):
                self.assertTrue(is_geometric(seq), seq)

    def test_is_geometric_negative(self):
        """Test dla sekwencji, które nie są geometryczne"""
        for seq in NON_GEOMETRIC_SEQS:
            with self.subTest(seq=seq):
                self.assertFalse(is_geometric(seq), seq)

    def test_is_geometric_nonint_quotient(self):
        """Test dla sekwencji, która jest geometryczna, ale nie ma całkowitego ilorazu"""
        seq = [9, 15, 25]
        self.assertFalse(
            is_geometric(seq), f"w sekwencji {seq} iloraz nie jest liczbą całkowitą"
        )


class TestCheckAdjacent(unittest.TestCase):
    """Testy funkcji check_adjacent()"""

    def test_empty(self):
        """Test dla pustej sekwencji"""
        self.assertTrue(check_adjacent([], lambda a, b: a == b))

    def test_single(self):
        """Test dla jednoelementowej sekwencji"""
        self.assertTrue(check_adjacent([1], lambda a, b: a == b))

    def test_check_adjacent_positive(self):
        """Test dla sekwencji, w której sąsiednie elementy spełniają warunek"""
        seq = [1, 2, 3]
        self.assertTrue(check_adjacent(seq, lambda a, b: a < b), seq)

    def test_check_adjacent_negative(self):
        """Test dla sekwencji, w której sąsiednie elementy nie spełniają warunku"""
        seq = [1, 2, 3]
        self.assertFalse(check_adjacent(seq, lambda a, b: a > b), seq)

    def test_check_adjacent_true_predicate(self):
        """Test dla predykatu, który zawsze zwraca True"""
        seq = [1, 2, 3]
        self.assertTrue(check_adjacent(seq, lambda a, b: True), seq)

    def test_check_adjacent_false_predicate(self):
        """Test dla predykatu, który zawsze zwraca False"""
        self.assertTrue(check_adjacent([], lambda a, b: False))
        self.assertTrue(check_adjacent([1], lambda a, b: False))
        seq = [1, 2, 3]
        self.assertFalse(check_adjacent(seq, lambda a, b: False), seq)


if __name__ == "__main__":
    unittest.main()
