import doctest


def flatten(matrix):
    """Spłaszcza macierz (listę list) do jednej listy.

    >>> flatten([[1, 2, 3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten([[1], [2], [3]])
    [1, 2, 3]
    >>> flatten([[], [1, 2], []])
    [1, 2]
    >>> flatten([])
    []
    """
    return [elem for wiersz in matrix for elem in wiersz]


def reshape(flat_list, rows, cols):
    """Przekształca płaską listę w macierz o zadanej liczbie wierszy i kolumn.

    Jeśli rows * cols != len(flat_list), zgłasza ValueError.
    Wiersze wynikowej macierzy są niezależne od flat_list.

    >>> reshape([1, 2, 3, 4, 5, 6], 2, 3)
    [[1, 2, 3], [4, 5, 6]]
    >>> reshape([1, 2, 3, 4], 2, 2)
    [[1, 2], [3, 4]]
    >>> reshape([], 0, 0)
    []
    >>> flat = [1, 2, 3, 4, 5, 6]
    >>> m = reshape(flat, 2, 3)
    >>> m[0][0] = 99
    >>> flat
    [1, 2, 3, 4, 5, 6]
    >>> reshape([1, 2, 3], 2, 2)
    Traceback (most recent call last):
        ...
    ValueError: nie można przekształcić listy o długości 3 w macierz 2 x 2
    """
    if rows * cols != len(flat_list):
        raise ValueError(
            f"nie można przekształcić listy o długości {len(flat_list)}"
            f" w macierz {rows} x {cols}"
        )
    # wycinek flat_list[i*cols:(i+1)*cols] tworzy nową listę - wiersze są niezależne
    return [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
