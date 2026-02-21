class Squares:
    """
    Klasa generująca kolejne kwadraty liczb naturalnych.

    Symuluje strumień danych.
    """

    def __init__(self):
        self.i = 0

    def nxt(self):
        """Zwraca kolejny kwadrat liczby naturalnej."""
        result = self.i**2
        self.i += 1
        return result


class Fib:
    """Klasa zwrająca liczby z ciągu Fibonacciego."""

    def __init__(self, a=0, b=1):
        self.mem = {0: a, 1: b}

    def idx(self, n):
        """
        Zwraca wartość ciągu Fibonacciego o podanym indeksie.

        Parametry:
        - n (int): indeks wyrazu ciągu Fibonacciego.

        Zwraca:
        - int: wartość ciągu Fibonacciego o podanym indeksie.
        """
        if n in self.mem:
            return self.mem[n]
        result = self.idx(n - 1) + self.idx(n - 2)
        self.mem[n] = result
        return result
