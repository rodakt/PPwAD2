def dzielniki(n):
    """Zwraca listę dodatnich dzielników n.

    Args:
        n (int): liczba całkowita

    >>> dzielniki(1)
    [1]
    >>> dzielniki(5)
    [1, 5]
    >>> dzielniki(-8)
    [1, 2, 4, 8]
    """

    n = n if n > 0 else -n
    return [d for d in range(1, n + 1) if n % d == 0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
