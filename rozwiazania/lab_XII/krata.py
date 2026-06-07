"""Krata punktów pierwszej ćwiartki - wyliczenie zbioru N x N.

Budowa analogiczna do spirali z wykładu XI: główny generator `krata`
składa się z dwóch pomocniczych iteratorów - `kroki` (długości kolejnych
odcinków trasy) i `kierunki` (kierunek każdego odcinka) - oraz słownika
`PRZESUNIĘCIA` przekształcającego punkt zgodnie z kierunkiem.

Trasa to zygzak po przekątnych x + y = 0, 1, 2, ... Każdą przekątną
przechodzimy w całości, a między przekątnymi robimy pojedynczy krok
łączący. Dzięki temu koniec jednej przekątnej sąsiaduje z początkiem
następnej i łamana łącząca punkty nie ma długich przeskoków.
"""

import csv
from itertools import islice


def kroki():
    """Długości kolejnych odcinków trasy: 1, 1, 1, 2, 1, 3, 1, 4, ...

    Na przemian: łącznik (zawsze długość 1) i przekątna (długość rośnie).
    """
    k = 1
    while True:
        yield 1
        yield k
        k += 1


def kierunki():
    """Kierunki kolejnych odcinków: G, D, P, U, G, D, P, U, ...

    G - góra, D - skos w dół-prawo (po przekątnej), P - prawo,
    U - skos w górę-lewo (po przekątnej).
    """
    while True:
        for kierunek in "GDPU":
            yield kierunek


PRZESUNIĘCIA = {
    "G": lambda x, y: (x, y + 1),
    "D": lambda x, y: (x + 1, y - 1),
    "P": lambda x, y: (x + 1, y),
    "U": lambda x, y: (x - 1, y + 1),
}


def krata():
    """Nieskończony strumień punktów (x, y) o całkowitych nieujemnych
    współrzędnych - każdy punkt pierwszej ćwiartki dokładnie raz.

    >>> list(islice(krata(), 9))
    [(0, 0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2), (0, 3), (1, 2), (2, 1)]
    """
    długości = kroki()
    kier = kierunki()
    x, y = 0, 0
    while True:
        długość = next(długości)
        kierunek = next(kier)
        for _ in range(długość):
            yield x, y
            x, y = PRZESUNIĘCIA[kierunek](x, y)


def krata_do_csv(filename, n=144):
    """Zapisuje pierwszych n punktów kraty do pliku CSV."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y"])
        writer.writerows(islice(krata(), n))


if __name__ == "__main__":
    krata_do_csv("krata.csv")
