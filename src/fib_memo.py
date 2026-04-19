# Path: src/fib_memo.py
"""
Memoizacja naiwnej rekurencji Fibonacciego:
- własny dekorator zapamiętujący (słownik w domknięciu),
- functools.lru_cache.

Sposób użycia:
python fib_memo.py
"""
from functools import wraps, lru_cache
from timeit import timeit


def zapamiętuj(f):
    """Dekorator zapamiętujący wyniki funkcji jednej zmiennej."""
    pamięć = {}

    @wraps(f)
    def wrapper(x):
        if x not in pamięć:
            pamięć[x] = f(x)
        return pamięć[x]

    return wrapper


@zapamiętuj
def fib_memo(n):
    """Wersja fib() z zapamiętywaniem (własny dekorator)."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


@lru_cache(maxsize=None)
def fib_lru(n):
    """Wersja fib() z zapamiętywaniem przez functools.lru_cache."""
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


def main():
    # Rozgrzewka — pierwsze wywołanie napełnia cache.
    fib_memo(100)
    fib_lru(100)

    for n in (30, 100, 500):
        t_memo = timeit(lambda: fib_memo(n), number=100_000) / 100_000
        t_lru = timeit(lambda: fib_lru(n), number=100_000) / 100_000
        print(f"n = {n:>3}  fib_memo: {t_memo:.2e} s   fib_lru: {t_lru:.2e} s")


if __name__ == "__main__":
    main()
