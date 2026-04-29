def fib_general(n, a, b, *args):
    """Zwraca wyraz f_n ciagu k-Fibonacciego z warunkami poczatkowymi a, b, *args."""
    if n < 0:
        raise NotImplementedError("Brak implementacji dla indeksów ujemnych")

    for _ in range(n):
        a, b, *args = b, *args, a + b + sum(args)
    return a


def fib(n, a=0, b=1):
    """Zwraca wyraz f_n ciagu Fibonacciego."""
    return fib_general(n, a, b)


def trib(n, a=0, b=0, c=1):
    """Zwraca wyraz f_n ciagu Tribonacciego."""
    return fib_general(n, a, b, c)


def tetra(n, a=0, b=0, c=0, d=1):
    """Zwraca wyraz f_n ciagu Tetranacciego."""
    return fib_general(n, a, b, c, d)
