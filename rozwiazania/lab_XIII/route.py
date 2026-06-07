from itertools import permutations


def shortest_route(matrix):
    """(długość, trasa) najkrótszego cyklu odwiedzającego wszystkie miasta.

    Trasa zaczyna się i kończy w mieście 0. `matrix[i][j]` to odległość
    między miastem i a j.

    >>> M = [[0, 10, 15, 20],
    ...      [10, 0, 35, 25],
    ...      [15, 35, 0, 30],
    ...      [20, 25, 30, 0]]
    >>> length, route = shortest_route(M)
    >>> length
    80
    """
    n = len(matrix)
    najkrótsza = None
    najlepsza_trasa = None
    for perm in permutations(range(1, n)):
        trasa = (0,) + perm + (0,)
        długość = sum(matrix[trasa[i]][trasa[i + 1]] for i in range(len(trasa) - 1))
        if najkrótsza is None or długość < najkrótsza:
            najkrótsza = długość
            najlepsza_trasa = trasa
    return najkrótsza, najlepsza_trasa
