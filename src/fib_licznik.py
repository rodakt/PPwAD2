# Path: src/fib_licznik.py
"""
Dekorator zliczający wywołania funkcji, zastosowany do naiwnej rekurencji
Fibonacciego.

Sposób użycia:
python fib_licznik.py
"""
from functools import wraps


def licz_wywołania(f):
    """Przechowuje liczbę wywołań f() w atrybucie licznik.liczba_wywołań."""
    @wraps(f)
    def licznik(*args, **kwargs):
        licznik.liczba_wywołań += 1
        return f(*args, **kwargs)
    licznik.liczba_wywołań = 0
    return licznik


@licz_wywołania
def fib(n):
    """Zwraca F_n, n >= 0, ciągu Fibonacciego."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    print(f"{'n':>3} | {'F_n':>12} | {'liczba wywołań':>16}")
    print("-" * 40)
    for n in range(0, 31):
        # Reset licznika przed każdym pomiarem.
        fib.liczba_wywołań = 0
        wartość = fib(n)
        print(f"{n:>3} | {wartość:>12} | {fib.liczba_wywołań:>16}")


if __name__ == "__main__":
    main()
