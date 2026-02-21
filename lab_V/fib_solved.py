"""Moduł zawierający funkcje obliczające wyrazy klasycznego ciągu Fibonacciego,
ciągu Tribonacciego oraz uogólnionego ciągu Fibonacciego z dowolną liczbą
wyrazów inicjujących.
"""


def fib_general(n, a, b, *c):
    """Oblicza n-ty wyraz ciągu Fibonacciego zdefiniowanego przez a, b i c."""
    if n < 0:
        raise NotImplementedError("Brak implementacji dla indeksów ujemnych")
    for _ in range(n):
        a, b, *c = b, *c, a + b + sum(c)
    return a


def fib(n, a=0, b=1):
    """Oblicza n-ty wyraz ciągu Fibonacciego zdefiniowanego przez a i b."""
    return fib_general(n, a, b)


def trib(n, a=0, b=0, c=1):
    """Oblicza n-ty wyraz ciągu Tribonacciego zdefiniowanego przez a, b i c."""
    return fib_general(n, a, b, c)


def tetra(n, a=0, b=0, c=0, d=1):
    """Oblicza n-ty wyraz ciągu Tetranacciego zdefiniowanego przez a, b, c i d."""
    return fib_general(n, a, b, c, d)
