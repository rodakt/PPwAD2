import doctest


def add_scalar(matrix, scalar):
    """Zwraca nową macierz, w której każdy element jest zwiększony o scalar.

    Nie modyfikuje macierzy wejściowej.

    >>> m = [[1, 2], [3, 4]]
    >>> add_scalar(m, 10)
    [[11, 12], [13, 14]]
    >>> m
    [[1, 2], [3, 4]]
    """
    return [[elem + scalar for elem in wiersz] for wiersz in matrix]


def add_scalar_in_place(matrix, scalar):
    """Zwiększa każdy element macierzy o scalar, modyfikując ją w miejscu.

    Zwraca None.

    >>> m = [[1, 2], [3, 4]]
    >>> add_scalar_in_place(m, 10)
    >>> m
    [[11, 12], [13, 14]]
    """
    for wiersz in matrix:
        for i in range(len(wiersz)):
            wiersz[i] += scalar


def transpose(matrix):
    """Zwraca transponowaną macierz (listę list).

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    >>> transpose([[1]])
    [[1]]
    >>> transpose([[1, 2], [3, 4], [5, 6]])
    [[1, 3, 5], [2, 4, 6]]
    """
    # zip(*matrix) paruje elementy o tych samych indeksach kolumnowych
    return [list(kolumna) for kolumna in zip(*matrix)]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
