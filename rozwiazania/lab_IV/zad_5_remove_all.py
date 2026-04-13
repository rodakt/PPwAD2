import doctest


def remove_all(lst, value):
    """Zwraca nową listę bez żadnych wystąpień value.

    Nie modyfikuje listy wejściowej.
    Zgłasza ValueError, jeśli value nie występuje w lst.

    >>> remove_all([1, 3, 2, 3, 4], 3)
    [1, 2, 4]
    >>> remove_all([2, 2, 2], 2)
    []
    >>> remove_all([1, 2, 3], 4)
    Traceback (most recent call last):
        ...
    ValueError: 4 not in lst
    >>> original = [1, 3, 2, 3, 4]
    >>> remove_all(original, 3)
    [1, 2, 4]
    >>> original
    [1, 3, 2, 3, 4]
    """
    if value not in lst:
        raise ValueError(f"{value} not in lst")
    return [elem for elem in lst if elem != value]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
