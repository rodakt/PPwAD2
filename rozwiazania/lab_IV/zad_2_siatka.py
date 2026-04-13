import doctest


def create_grid(rows, cols, value=0):
    """Tworzy siatkę (listę list) o zadanych wymiarach wypełnioną wartością value.

    Każdy wiersz musi być niezależnym obiektem.

    >>> create_grid(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    >>> create_grid(3, 2, 'x')
    [['x', 'x'], ['x', 'x'], ['x', 'x']]
    >>> g = create_grid(3, 3)
    >>> g[0][0] = 1
    >>> g
    [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> g = create_grid(3, 3)
    >>> g[0] is g[1]
    False
    """
    # każda iteracja _ in range(rows) tworzy nowy obiekt [value] * cols
    return [[value] * cols for _ in range(rows)]


def identity_matrix(n):
    """Tworzy macierz jednostkową n x n.

    >>> identity_matrix(1)
    [[1]]
    >>> identity_matrix(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> m = identity_matrix(2)
    >>> m[0] is m[1]
    False
    """
    # każdy wiersz jest nowym obiektem; 1 tylko na przekątnej (i == j)
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
