"""Moduł zawierający funkcje do obliczania ułamków łańcuchowych"""


def to_fraction(seq):
    """Oblicza wartość ułamka łańcuchowego z sekwencji współczynników seq.

    Zwraca krotkę (licznik, mianownik).

    Zgłasza wyjątek ValueError, jeśli seq jest puste.
    """
    if not seq:
        raise ValueError("sekwencja współczynników nie może być pusta")
    numerator, denominator = seq[-1], 1
    for a in seq[-2::-1]:
        numerator, denominator = a * numerator + denominator, numerator
    return numerator, denominator


def to_float(seq):
    """Oblicza wartość ułamka łańcuchowego z sekwencji współczynników seq.

    Zwraca wartość ułamka jako liczbę zmiennoprzecinkową.

    Zgłasza wyjątek ValueError, jeśli seq jest puste.
    """
    a, b = to_fraction(seq)
    return a / b


def euclid(a, b):
    """Algorytm Euklidesa: zwraca reszty i ilorazy w dwóch listach.

    Args:
        a, b: liczby całkowite, b > 0.

    Zgłasza wyjątek ValueError, jeśli b <= 0.
    """
    if b <= 0:
        raise ValueError("argument b musi być dodatni")

    remainders = [a, b]
    quotients = []
    while b != 0:
        quotient, remainder = a // b, a % b
        quotients.append(quotient)
        remainders.append(remainder)
        a, b = remainders[-2], remainders[-1]
    return remainders, quotients


def continued_fraction(a, b):
    """Oblicza ułamek łańcuchowy z ułamka zwykłego a/b

    Args:
        a, b: liczby całkowite, b != 0.

    Zgłasza wyjątek ZeroDivisionError, jeśli b == 0.

    >>> continued_fraction(0, 1)
    [0]
    >>> continued_fraction(23, 1)
    [23]
    >>> continued_fraction(4, 7)
    [0, 1, 1, 3]
    """
    if b == 0:
        raise ZeroDivisionError("mianownik nie może być równy 0")
    if b < 0:
        a, b = -a, -b
    _, quotients = euclid(a, b)
    return quotients


def gcd(a, b):
    """Oblicza największy wspólny dzielnik dwóch liczb a i b"""
    if a * b == 0:
        return max(abs(a), abs(b))
    if b < 0:
        b = -b
    remainders, _ = euclid(a, b)
    return remainders[-2]
