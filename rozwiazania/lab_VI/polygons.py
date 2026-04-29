from fractions import Fraction

from logo_turtle import forward, right


def polygon(turtle, a, r):
    """Rysuje wielokąt żółwiowy o boku r i kącie obrotu a; zwraca liczbę boków.

    Kąt a musi być typu int lub Fraction i nie może być wielokrotnością 360.
    """
    if not isinstance(a, (int, Fraction)):
        raise TypeError("kąt musi być liczbą całkowitą lub wymierną")
    a_frac = Fraction(a)
    if a_frac % 360 == 0:
        raise ValueError("kąt musi być liczbą wymierną nie będącą wielokrotnością 360")
    # sumujemy obroty; gdy suma jest wielokrotnością 360, wielokąt się zamknął
    total = Fraction(0)
    n = 0
    while True:
        forward(turtle, r)
        right(turtle, a)
        total += a_frac
        n += 1
        if total % 360 == 0:
            break
    return n


def regular_polygon(turtle, n, r):
    """Rysuje n-kąt foremny o boku r."""
    polygon(turtle, Fraction(360, n), r)
