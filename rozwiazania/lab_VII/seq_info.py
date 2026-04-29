def check_adjacent(seq, pred):
    """Zwraca True, jeśli pred(x, y) zachodzi dla każdej pary sąsiednich elementów."""
    return all(pred(x, y) for x, y in zip(seq[:-1], seq[1:]))


def is_ascending(seq):
    """Zwraca True, jeśli sekwencja jest niemalejąca."""
    return check_adjacent(seq, lambda x, y: x <= y)


def is_strictly_ascending(seq):
    """Zwraca True, jeśli sekwencja jest ściśle rosnąca."""
    return check_adjacent(seq, lambda x, y: x < y)


def is_descending(seq):
    """Zwraca True, jeśli sekwencja jest nierosnąca."""
    return check_adjacent(seq, lambda x, y: x >= y)


def is_strictly_descending(seq):
    """Zwraca True, jeśli sekwencja jest ściśle malejąca."""
    return check_adjacent(seq, lambda x, y: x > y)


def is_monotonic(seq):
    """Zwraca True, jeśli sekwencja jest monotoniczna."""
    return is_ascending(seq) or is_descending(seq)


def is_strictly_monotonic(seq):
    """Zwraca True, jeśli sekwencja jest ściśle monotoniczna."""
    return is_strictly_ascending(seq) or is_strictly_descending(seq)


def is_constant(seq):
    """Zwraca True, jeśli sekwencja jest stała."""
    return check_adjacent(seq, lambda x, y: x == y)


def is_alternating(seq):
    """Zwraca True, jeśli sekwencja jest naprzemienna (każda para sąsiednich ma różne znaki)."""
    return check_adjacent(seq, lambda x, y: x * y < 0)


def is_arithmetic(seq, r=None):
    """Zwraca True, jeśli sekwencja jest ciągiem arytmetycznym (o różnicy r, jeśli podane)."""
    if r is not None:
        return check_adjacent(seq, lambda x, y: y - x == r)
    
    if len(seq) <= 1:
        return True
    return is_arithmetic(seq, r=seq[1] - seq[0])


def is_geometric(seq, q=None):
    """Zwraca True, jeśli sekwencja jest ciągiem geometrycznym o całkowitym ilorazie."""
    if q is not None:
        return check_adjacent(seq, lambda x, y: x != 0 and y == x * q)

    if len(seq) <= 1:
        return True
    if seq[0] == 0:
        return False
    # obliczamy iloraz dzieleniem całkowitym i sprawdzamy rekurencyjnie
    return is_geometric(seq, q=seq[1] // seq[0])
