"""Moduł sprawdzający własności ciągów liczbowych"""


def check_adjacent(seq, pred):
    """Zwraca True, jeśli dla każdej pary a, b sąsiednich elementów seq
    wywołanie pred(a, b) zwraca True"""
    return all(pred(a, b) for a, b in zip(seq[:-1], seq[1:]))


def is_ascending(seq):
    """Zwraca True, jeśli seq jest niemalejący"""
    return check_adjacent(seq, lambda a, b: a <= b)


def is_strictly_ascending(seq):
    """Zwraca True, jeśli seq jest ściśle rosnący"""
    return check_adjacent(seq, lambda a, b: a < b)


def is_descending(seq):
    """Zwraca True, jeśli seq jest nierosnący"""
    return check_adjacent(seq, lambda a, b: a >= b)


def is_strictly_descending(seq):
    """Zwraca True, jeśli seq jest ściśle malejący"""
    return check_adjacent(seq, lambda a, b: a > b)


def is_monotonic(seq):
    """Zwraca True, jeśli seq jest monotoniczny"""
    return is_ascending(seq) or is_descending(seq)


def is_strictly_monotonic(seq):
    """Zwraca True, jeśli seq jest ściśle monotoniczny"""
    return is_strictly_ascending(seq) or is_strictly_descending(seq)


def is_constant(seq):
    """Zwraca True, jeśli seq jest stały"""
    return check_adjacent(seq, lambda a, b: a == b)


def is_alternating(seq):
    """Zwraca True, jeśli seq jest naprzemienny"""
    return check_adjacent(seq, lambda a, b: a * b < 0)


def is_arithmetic(seq, r=None):
    """Zwraca True, jeśli seq jest arytmetyczny"""
    if r is None:
        try:
            r = seq[1] - seq[0]
        except IndexError:
            return True
        return is_arithmetic(seq, r)
    return check_adjacent(seq, lambda a, b: b - a == r)


def is_geometric(seq, q=None):
    """Zwraca True, jeśli seq jest geometryczny o całkowitym ilorazie"""
    if q is None:
        try:
            q = seq[1] // seq[0]
        except IndexError:
            return True
        except ZeroDivisionError:
            # jest geometryczny, o ile składa się z samych zer
            return is_constant(seq)
        return is_geometric(seq, q)
    return check_adjacent(seq, lambda a, b: b == a * q)
