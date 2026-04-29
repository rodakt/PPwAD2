"""Potok funkcji."""

import doctest


def pipeline(*functions):
    """Zwraca złożenie funkcji stosowanych od lewej do prawej.

    pipeline()(x) zwraca x.
    pipeline(f)(x) zwraca f(x).
    pipeline(f, g)(x) zwraca g(f(x)).
    pipeline(f, g, h)(x) zwraca h(g(f(x))).

    >>> pipeline()(5)
    5
    >>> pipeline(abs)(-3)
    3
    >>> def double(x):
    ...     return 2 * x
    >>> def add_one(x):
    ...     return x + 1
    >>> pipeline(abs, double, add_one)(-3)
    7
    >>> pipeline(add_one, double)(-3)
    -4
    >>> pipeline(double, add_one)(-3)
    -5
    """
    def composed(x):
        wynik = x
        for f in functions:
            wynik = f(wynik)
        return wynik
    return composed


if __name__ == "__main__":
    doctest.testmod(verbose=True)
