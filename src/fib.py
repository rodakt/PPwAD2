def fib_iter(n):
    """Iteracyjna wersja ciągu Fibonacciego

    Argumenty:
        n (int): liczba całkowita

    Zwraca:
        int: f_n - wartość ciągu o indeksie n
    """
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
