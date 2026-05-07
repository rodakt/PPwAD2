def find_root(f, a, b, abs_tol=1e-6):
    """
    Znajduje miejsce zerowe funkcji w zadanym przedziale metodą bisekcji.

    Parametry:
    f : funkcja, dla której szukamy miejsca zerowego.
    a : float, dolne ograniczenie przedziału.
    b : float, górne ograniczenie przedziału.
    abs_tol : float, opcjonalnie, tolerancja bezwzględna. Domyślnie 1e-6.

    Zwraca:
    float: przybliżone miejsce zerowe funkcji w zadanym przedziale.

    Zgłasza:
    ValueError: gdy f(a) i f(b) mają ten sam znak.

    Przykłady:
    >>> from math import cos, pi, isclose
    >>> abs_tol = 1e-6

    >>> z = find_root(lambda x: x, -100, 200)
    >>> isclose(z, 0, abs_tol=abs_tol)
    True

    >>> z = find_root(cos, 0, pi)
    >>> isclose(z, pi / 2, abs_tol=abs_tol)
    True

    >>> z = find_root(lambda x: x**3 - x - 2, 0, 2, abs_tol=1e-11)
    >>> isclose(z, 1.52137970680457, abs_tol=1e-11)
    True

    >>> find_root(lambda x: 1 + x**2, 1, 100)
    Traceback (most recent call last):
        ...
    ValueError: f(a) i f(b) mają ten sam znak — nie można zagwarantować miejsca zerowego w przedziale.
    """
    if f(a) * f(b) > 0:
        raise ValueError(
            "f(a) i f(b) mają ten sam znak — nie można zagwarantować miejsca zerowego w przedziale."
        )
    c = (a + b) / 2
    if f(c) == 0 or b - a < abs_tol:
        return c
    elif f(a) * f(c) < 0:
        return find_root(f, a, c, abs_tol)
    else:
        return find_root(f, c, b, abs_tol)
