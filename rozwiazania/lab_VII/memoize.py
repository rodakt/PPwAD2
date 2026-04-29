"""Zapamiętywanie wyników funkcji."""


def make_memoized(f):
    """Zwraca wersję f zapamiętującą wyniki wcześniejszych wywołań.

    >>> call_count = 0
    >>> def slow_square(x):
    ...     global call_count
    ...     call_count += 1
    ...     return x * x
    >>> memo_square = make_memoized(slow_square)
    >>> memo_square(4)
    16
    >>> memo_square(4)
    16
    >>> memo_square(5)
    25
    >>> call_count
    2
    """
    pamięć = {}

    def memoized(x):
        if x not in pamięć:
            pamięć[x] = f(x)
        return pamięć[x]

    return memoized


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
