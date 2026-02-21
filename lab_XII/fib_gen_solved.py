"""
Moduł zawierający funkcje generatora dla ciągów Fibonacciego, Tribonacciego
oraz uogólnionego ciągu Fibonacciego z dowolną liczbą początkowych wyrazów.
"""


def fib(a=0, b=1):
    """
    Funkcja generatora dla ciągu Fibonacciego.

    Args:
        a (int, optional): Pierwszy wyraz ciągu. Domyślnie 0.
        b (int, optional): Drugi wyraz ciągu. Domyślnie 1.

    Yields:
        int: Następny wyraz ciągu.
    """
    return fib_general(a, b)


def trib(a=0, b=0, c=1):
    """
    Funkcja generatora dla ciągu Tribonacciego.

    Args:
        a (int, optional): Pierwszy wyraz ciągu. Domyślnie 0.
        b (int, optional): Drugi wyraz ciągu. Domyślnie 0.
        c (int, optional): Trzeci wyraz ciągu. Domyślnie 1.

    Yields:
        int: Następny wyraz ciągu.
    """
    return fib_general(a, b, c)

def tetra(a=0, b=0, c=0, d=1):
    """
    Funkcja generatora dla ciągu Tetranacciego.

    Args:
        a (int, optional): Pierwszy wyraz ciągu. Domyślnie 0.
        b (int, optional): Drugi wyraz ciągu. Domyślnie 0.
        c (int, optional): Trzeci wyraz ciągu. Domyślnie 0.
        d (int, optional): Czwarty wyraz ciągu. Domyślnie 1.

    Yields:
        int: Następny wyraz ciągu.
    """
    return fib_general(a, b, c, d)


def fib_general(a, b, *args):
    """
    Funkcja generatora dla ciągu Fibonacciego z dowolną (>=2) liczbą początkowych wyrazów.

    Args:
        a (int): Pierwszy wyraz ciągu.
        b (int): Drugi wyraz ciągu.
        *args (int): Pozostałe wyrazy ciągu.

    Yields:
        int: Następny wyraz ciągu.
    """
    while True:
        yield a
        a, b, *args = b, *args, a + b + sum(args)
