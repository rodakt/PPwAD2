# Path: src/fib_naive.py
"""
Naiwna, bezpośrednio rekurencyjna implementacja ciągu Fibonacciego
oraz pomiar średniego czasu wykonania fib(n) dla rosnących n.

Sposób użycia:
python fib_naive.py
"""
from timeit import timeit


def fib(n):
    """Zwraca F_n, n >= 0, ciągu Fibonacciego."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def zmierz_czasy(n_start=10, n_stop=37):
    """Zwraca listę par (n, średni czas wykonania fib(n))."""
    wyniki = []
    for n in range(n_start, n_stop + 1):
        # Liczba powtórzeń maleje wraz ze wzrostem n, bo pojedyncze
        # wywołanie robi się coraz wolniejsze.
        if n < 25:
            powtórzeń = 1_000
        elif n < 33:
            powtórzeń = 10
        else:
            powtórzeń = 1
        czas = timeit(lambda: fib(n), number=powtórzeń) / powtórzeń
        wyniki.append((n, czas))
    return wyniki


def main():
    print(f"{'n':>3} | {'F_n':>12} | {'średni czas [s]':>18}")
    print("-" * 42)
    for n, czas in zmierz_czasy():
        print(f"{n:>3} | {fib(n):>12} | {czas:>18.6f}")


if __name__ == "__main__":
    main()
