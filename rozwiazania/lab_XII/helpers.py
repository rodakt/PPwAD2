def my_enumerate(it, start=0):
    """Odpowiednik wbudowanej funkcji `enumerate`.

    Zwraca generator par `(indeks, element)` dla kolejnych elementów `it`,
    gdzie indeks zaczyna się od `start` i rośnie o 1.

    >>> list(my_enumerate('abc'))
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> list(my_enumerate('abc', start=10))
    [(10, 'a'), (11, 'b'), (12, 'c')]
    >>> list(my_enumerate([]))
    []
    """
    i = start
    for element in it:
        yield i, element
        i += 1


def take(it, n):
    """Generator pierwszych `n` elementów z `it`.

    Jeśli `it` ma mniej niż `n` elementów, zwraca wszystkie.
    Odpowiednik `itertools.islice(it, n)`.

    >>> list(take(range(100), 5))
    [0, 1, 2, 3, 4]
    >>> list(take('abc', 10))
    ['a', 'b', 'c']
    >>> list(take('abc', 0))
    []
    """
    for i, element in my_enumerate(it):
        if i >= n:
            return
        yield element


def repeat_each(it, k):
    """Generator, w którym każdy element `it` powtórzony jest `k` razy.

    >>> list(repeat_each([1, 2, 3], 2))
    [1, 1, 2, 2, 3, 3]
    >>> list(repeat_each('ab', 3))
    ['a', 'a', 'a', 'b', 'b', 'b']
    >>> list(repeat_each([1, 2, 3], 1))
    [1, 2, 3]
    >>> list(repeat_each([1, 2, 3], 0))
    []
    """
    for element in it:
        for _ in range(k):
            yield element


def geometric(a, r):
    """Nieskończony generator ciągu geometrycznego: a, a*r, a*r**2, a*r**3, ...

    >>> g = geometric(1, 2)
    >>> [next(g) for _ in range(6)]
    [1, 2, 4, 8, 16, 32]
    >>> g = geometric(3, 10)
    >>> [next(g) for _ in range(4)]
    [3, 30, 300, 3000]
    """
    wartość = a
    while True:
        yield wartość
        wartość *= r
