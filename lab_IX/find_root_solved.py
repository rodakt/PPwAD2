def find_root(f, a, b, abs_tol=1e-6):
    """
    Znajduje miejsce zerowe funkcji w zadanym przedziale.

    Parametry:
    f : funkcja, dla której szukamy miejsca zerowego.
    a : float, dolne ograniczenie przedziału.
    b : float, górne ograniczenie przedziału.
    abs_tol : float, opcjonalnie, tolerancja bezwzględna dla przybliżenia miejsca zerowego. Domyślnie 1e-6.

    Zwraca:
    float: Przybliżone miejsce zerowe funkcji w zadanym przedziale.

    Przykłady:
    >>> from math import cos, pi, isclose
    >>> abs_tol = 1e-6
    >>> f = lambda x: x
    >>> z = find_root(f, -100, 200)
    >>> isclose(z, 0, abs_tol=abs_tol)
    True

    >>> z = find_root(cos, 0, pi)
    >>> isclose(z, pi / 2, abs_tol=abs_tol)
    True

    >>> f = lambda x: x**3 - x - 2
    >>> z = find_root(f, 0, 2, abs_tol=1e-11)
    >>> isclose(z, 1.52137970680457, abs_tol=1e-11)
    True

    >>> f = lambda x: 1 + x**2
    >>> try:
    ...     find_root(f, 1, 100)
    ... except ValueError:
    ...     pass
    ... except Exception:
    ...     raise AssertionError("Nieprawidłowy rodzaj błędu.")
    ... else:
    ...     raise AssertionError("Brak wyjątku ValueError. Funkcja nie ma zera w przedziale.")
    """
    if f(a) * f(b) > 0:
        raise ValueError("Funkcja nie zmienia znaku na końcach przedziału.")

    while b - a > abs_tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


import doctest

doctest.testmod(verbose=True)
