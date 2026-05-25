class Fib:
    """Klasa reprezentująca nieskończony ciąg Fibonacciego o zadanych
    wartościach początkowych.

    >>> fib = Fib()
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    55
    >>> fib(50)
    12586269025
    >>> fib(100)
    354224848179261915075
    >>> fib = Fib()
    >>> fib(5000) # test sprawdza, czy implementacja jest rekurencyjna  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded
    >>> lucas = Fib(F0=2, F1=1)
    >>> [lucas(n) for n in range(8)]
    [2, 1, 3, 4, 7, 11, 18, 29]
    """

    def __init__(self, F0=0, F1=1):
        self._cache = {0: F0, 1: F1}

    def __call__(self, n):
        if n not in self._cache:
            self._cache[n] = self(n - 1) + self(n - 2)
        return self._cache[n]
