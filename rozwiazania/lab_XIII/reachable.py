from itertools import product


def reachable(numbers):
    """Posortowana lista różnych wartości wyrażeń
    numbers[0] ± numbers[1] ± ... ± numbers[-1].

    >>> reachable([1, 2, 3])
    [-4, 0, 2, 6]
    >>> reachable([5])
    [5]
    >>> reachable([10, 10])
    [0, 20]
    """
    wyniki = set()
    for znaki in product(['+', '-'], repeat=len(numbers) - 1):
        wartosc = numbers[0]
        for znak, n in zip(znaki, numbers[1:]):
            if znak == '+':
                wartosc += n
            else:
                wartosc -= n
        wyniki.add(wartosc)
    return sorted(wyniki)
