import doctest


def is_arithmetic(seq):
    """Zwraca True, jeśli seq jest ciągiem arytmetycznym; w przeciwnym razie zwraca False.

    Parametry:
    seq -- ciąg liczb

    Przykłady:
    >>> is_arithmetic([])
    True
    >>> is_arithmetic([2])
    True
    >>> is_arithmetic([5, -1])
    True
    >>> is_arithmetic([1, 2, 3])
    True
    >>> is_arithmetic(range(100, -1000, -7))
    True
    >>> is_arithmetic((2, 5, 8, 10, 13))
    False
    """
    # konwersja na listę - funkcja akceptuje dowolny typ sekwencji
    seq = list(seq)
    if len(seq) <= 1:
        # ciąg pusty i jednoelementowy są arytmetyczne z definicji
        return True
    d = seq[1] - seq[0]
    # sprawdzamy czy każda kolejna różnica równa się d
    return all(seq[i] - seq[i - 1] == d for i in range(2, len(seq)))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
