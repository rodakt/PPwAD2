def fib(a=0, b=1):
    """Iterator ciągu Fibonacciego z warunkami początkowymi a, b.

    >>> f = fib()
    >>> [next(f) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> f = fib(2, 1)
    >>> [next(f) for _ in range(8)]
    [2, 1, 3, 4, 7, 11, 18, 29]
    """
    return fib_general(a, b)


def trib(a=0, b=0, c=1):
    """Iterator ciągu Tribonacciego z warunkami początkowymi a, b, c.

    >>> t = trib()
    >>> [next(t) for _ in range(10)]
    [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    """
    return fib_general(a, b, c)


def tetra(a=0, b=0, c=0, d=1):
    """Iterator ciągu Tetranacciego z warunkami początkowymi a, b, c, d.

    >>> t = tetra()
    >>> [next(t) for _ in range(10)]
    [0, 0, 0, 1, 1, 2, 4, 8, 15, 29]
    """
    return fib_general(a, b, c, d)


def fib_general(a, b, *args):
    """Generator uogólnionego ciągu k-Fibonacciego, k = 2 + len(args).

    >>> g = fib_general(0, 1)
    >>> [next(g) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> g = fib_general(0, 0, 1)
    >>> [next(g) for _ in range(10)]
    [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    >>> g = fib_general(1, 1, 1, 1, 1)
    >>> [next(g) for _ in range(10)]
    [1, 1, 1, 1, 1, 5, 9, 17, 33, 65]
    """
    while True:
        yield a
        a, b, *args = b, *args, a + b + sum(args)
