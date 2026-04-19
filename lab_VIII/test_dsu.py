"""Testy jednostkowe dla modułu dsu."""

import unittest
from dsu import key_minmax, key_sort

OWOCE = (("jabłko", 1), ("arbuz", 10), ("banan", 4), ("gruszka", 6))
PUNKTY = ((0, 0), (0, 20), (1, 1), (10, -10))
SLOWA = ("ala", "ma", "kota", "i", "psa")


class TestKeyMinMax(unittest.TestCase):
    """Testy jednostkowe dla dekoratora key_minmax."""

    def test_metadata(self):
        """Test metadanych dekoratora."""

        @key_minmax(lambda x: x)
        def minimum(seq):
            """Zwraca minimum z sekwencji seq."""
            return min(seq)

        self.assertEqual(minimum.__name__, "minimum")
        self.assertEqual(minimum.__doc__, "Zwraca minimum z sekwencji seq.")

        @key_minmax(lambda x: x)
        def maksimum(seq):
            """Zwraca maksimum z sekwencji seq."""
            return max(seq)

        self.assertEqual(maksimum.__name__, "maksimum")
        self.assertEqual(maksimum.__doc__, "Zwraca maksimum z sekwencji seq.")

    def test_without_key(self):
        """Test key_minmax() bez klucza."""

        @key_minmax()
        def minimum(seq):
            """Zwraca minimum z sekwencji seq."""
            return min(seq)

        self.assertEqual(minimum([1, 2, 3, 4, 5]), 1)

        @key_minmax()
        def maksimum(seq):
            """Zwraca maksimum z sekwencji seq."""
            return max(seq)

        self.assertEqual(maksimum([1, 2, 3, 4, 5]), 5)

    def test_second_item(self):
        """Test key_minmax() dla klucza zwracającego drugi element krotki."""

        @key_minmax(lambda x: x[1])
        def minimum(seq):
            """Zwraca minimum z sekwencji seq."""
            return min(seq)

        self.assertEqual(minimum(OWOCE), ("jabłko", 1))

        @key_minmax(lambda x: x[1])
        def maksimum(seq):
            """Zwraca maksimum z sekwencji seq."""
            return max(seq)

        self.assertEqual(maksimum(OWOCE), ("arbuz", 10))

    def test_sq_norm(self):
        """Test key_minmax() dla klucza zwracającego kwadrat normy."""

        @key_minmax(lambda x: x[0] ** 2 + x[1] ** 2)
        def minimum(seq):
            """Zwraca minimum z sekwencji seq."""
            return min(seq)

        self.assertEqual(minimum(PUNKTY), (0, 0))

        @key_minmax(lambda x: x[0] ** 2 + x[1] ** 2)
        def maksimum(seq):
            """Zwraca maksimum z sekwencji seq."""
            return max(seq)

        self.assertEqual(maksimum(PUNKTY), (0, 20))

    def test_len(self):
        """Test key_minmax() dla klucza zwracającego długość sekwencji."""

        @key_minmax(len)
        def minimum(seq):
            """Zwraca minimum z sekwencji seq."""
            return min(seq)

        self.assertEqual(minimum(SLOWA), "i")

        @key_minmax(len)
        def maksimum(seq):
            """Zwraca maksimum z sekwencji seq."""
            return max(seq)

        self.assertEqual(maksimum(SLOWA), "kota")

    def test_noncomparable(self):
        """Test key_minmax() dla sekwencji nieporównywalnych obiektów."""

        class A:
            """Obiekty klasy A nie są porównywalne."""

            def __init__(self, x):
                self.x = x

        @key_minmax(lambda a: a.x)
        def minimum(seq):
            """Zwraca minimum z sekwencji seq."""
            return min(seq)

        lst = [A(10), A(20), A(5)]
        self.assertEqual(minimum(lst).x, 5)

        @key_minmax(lambda a: a.x)
        def maksimum(seq):
            """Zwraca maksimum z sekwencji seq."""
            return max(seq)

        lst = [A(10), A(20), A(5)]
        self.assertEqual(maksimum(lst).x, 20)


class TestKeySort(unittest.TestCase):
    """Testy jednostkowe dla dekoratora key_sort."""

    def test_metadata(self):
        """Test metadanych dekoratora."""

        @key_sort(lambda x: x)
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        self.assertEqual(sort.__name__, "sort")
        self.assertEqual(sort.__doc__, "Sortuje sekwencję seq.")

    def test_without_key(self):
        """Test key_sort() bez klucza."""

        @key_sort()
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        self.assertEqual(sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_second_item(self):
        """Test key_sort() dla klucza zwracającego drugi element krotki."""

        @key_sort(lambda x: x[1])
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        self.assertEqual(
            sort(OWOCE), [("jabłko", 1), ("banan", 4), ("gruszka", 6), ("arbuz", 10)]
        )

    def test_sq_norm(self):
        """Test key_sort() dla klucza zwracającego kwadrat normy."""

        @key_sort(lambda x: x[0] ** 2 + x[1] ** 2)
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        self.assertEqual(sort(PUNKTY), [(0, 0), (1, 1), (10, -10), (0, 20)])

    def test_len(self):
        """Test key_sort() dla klucza zwracającego długość sekwencji."""

        @key_sort(len)
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        self.assertEqual(sort(SLOWA), ["i", "ma", "ala", "psa", "kota"])

    def test_noncomparable(self):
        """Test key_sort() dla sekwencji nieporównywalnych obiektów."""

        class A:
            """Obiekty klasy A nie są porównywalne."""

            def __init__(self, x):
                self.x = x

        @key_sort(lambda a: a.x)
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        lst = [A(10), A(20), A(5)]
        self.assertEqual([a.x for a in sort(lst)], [5, 10, 20])

    def test_stability(self):
        """Test stabilności sortowania."""

        @key_sort(lambda x: x[0])
        def sort(seq):
            """Sortuje sekwencję seq."""
            return sorted(seq)

        seq = [(1, 2), (2, 1), (1, 1), (2, 2)]
        self.assertEqual(sort(seq), [(1, 2), (1, 1), (2, 1), (2, 2)])


if __name__ == "__main__":
    unittest.main()
