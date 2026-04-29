import doctest


def call_and_log(f, *args, verbose=False, **kwargs):
    """Wywołuje f(*args, **kwargs) i zwraca wynik.

    Jeśli verbose jest True, wypisuje informację o wywołaniu
    i wyniku w formacie: nazwa(argumenty) -> wynik.

    >>> def add(a, b):
    ...     return a + b
    >>> call_and_log(add, 2, 3)
    5
    >>> call_and_log(add, 2, 3, verbose=True)
    add(2, 3) -> 5
    5
    >>> call_and_log(pow, 2, 10, verbose=True)
    pow(2, 10) -> 1024
    1024
    >>> call_and_log(add, a=2, b=3, verbose=True)
    add(a=2, b=3) -> 5
    5
    """
    wynik = f(*args, **kwargs)
    if verbose:
        # repr() daje czytelna reprezentacje; kwargs formatujemy jako klucz=wartość
        części = [repr(a) for a in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()]
        print(f"{f.__name__}({', '.join(części)}) -> {wynik}")
    return wynik


def apply_n(f, n, x):
    """Zwraca wynik n-krotnego zastosowania f do x.

    apply_n(f, 0, x) zwraca x.
    apply_n(f, n, x) zwraca f(f(...f(x)...)), gdzie f występuje n razy.

    >>> apply_n(abs, 0, -5)
    -5
    >>> apply_n(abs, 1, -5)
    5
    >>> from math import sqrt
    >>> apply_n(sqrt, 0, 16)
    16
    >>> apply_n(sqrt, 1, 16)
    4.0
    >>> apply_n(sqrt, 2, 16)
    2.0
    """
    for _ in range(n):
        x = f(x)
    return x


if __name__ == '__main__':
    doctest.testmod(verbose=True)
