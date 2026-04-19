# Path: src/fib_analiza.py
"""
Skrypt pomocniczy do wykładu VIII (rekurencja).

Mierzy czas wykonania i liczbę wywołań naiwnego fib(n), dopasowuje ciąg
geometryczny metodą regresji liniowej na log T oraz generuje cztery rysunki:

    img/fib_czas.png             — czas wykonania fib(n)
    img/fib_ilorazy_czasu.png    — stosunki czasu T(n+1)/T(n)
    img/fib_wywolania.png        — liczba wywołań fib(n)
    img/fib_ilorazy_wywolan.png  — stosunki liczby wywołań

Wymaga: numpy, matplotlib, statsmodels.

Sposób użycia:
python fib_analiza.py
"""
import os
from functools import wraps
from timeit import timeit

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


PHI = (1 + 5 ** 0.5) / 2
OUT_DIR = "img"


# --- Fibonacci ---------------------------------------------------------------

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def licz_wywołania(f):
    @wraps(f)
    def licznik(*args, **kwargs):
        licznik.liczba_wywołań += 1
        return f(*args, **kwargs)
    licznik.liczba_wywołań = 0
    return licznik


@licz_wywołania
def fib_z_licznikiem(n):
    if n < 2:
        return n
    return fib_z_licznikiem(n - 1) + fib_z_licznikiem(n - 2)


# --- Pomiary -----------------------------------------------------------------

def zmierz_czasy(n_start=10, n_stop=37):
    N, T = [], []
    for n in range(n_start, n_stop + 1):
        if n < 25:
            powtórzeń = 1_000
        elif n < 33:
            powtórzeń = 10
        else:
            powtórzeń = 1
        t = timeit(lambda: fib(n), number=powtórzeń) / powtórzeń
        N.append(n)
        T.append(t)
        print(f"  fib({n:>2}): {t:.6e} s")
    return np.array(N), np.array(T)


def zmierz_wywołania(n_start=0, n_stop=30):
    N, C = [], []
    for n in range(n_start, n_stop + 1):
        fib_z_licznikiem.liczba_wywołań = 0
        fib_z_licznikiem(n)
        N.append(n)
        C.append(fib_z_licznikiem.liczba_wywołań)
    return np.array(N), np.array(C)


# --- Regresja liniowa log T = log a + n * log q ------------------------------

def dopasuj_ciąg_geometryczny(N, T):
    logT = np.log(T)
    reg = sm.OLS(logT, sm.add_constant(N)).fit()
    log_a, log_q = reg.params
    a, q = np.exp(log_a), np.exp(log_q)
    print(f"\nDopasowanie T(n) ≈ a · q^n")
    print(f"  a = {a:.3e}")
    print(f"  q = {q:.6f}   (φ = {PHI:.6f})")
    return a, q


# --- Rysunki -----------------------------------------------------------------

def wykres_czasu(N, T, out_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N, T, "o-", label="zmierzony czas")
    ax.set_xlabel("n")
    ax.set_ylabel("średni czas wykonania fib(n)  [s]")
    ax.grid(True, linestyle=":")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def wykres_ilorazów(N, wartości, out_path, y_label):
    ilorazy = wartości[1:] / wartości[:-1]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N[1:], ilorazy, "o-", label="kolejne ilorazy")
    ax.axhline(PHI, color="red", linestyle="--",
               label=fr"$\varphi \approx {PHI:.4f}$")
    ax.set_xlabel("n + 1")
    ax.set_ylabel(y_label)
    ax.grid(True, linestyle=":")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def wykres_wywołań(N, C, out_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N, C, "o-", label="liczba wywołań fib(n)")
    ax.set_xlabel("n")
    ax.set_ylabel("liczba wywołań rekurencyjnych")
    ax.grid(True, linestyle=":")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# --- Główna ------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("== Pomiar czasu ==")
    N_t, T = zmierz_czasy()

    print("\n== Regresja liniowa na log T ==")
    dopasuj_ciąg_geometryczny(N_t, T)

    print("\n== Pomiar liczby wywołań ==")
    N_c, C = zmierz_wywołania()
    print(f"  T(30) = {C[30]}   (dokładnie 2 · F(31) - 1 = {2 * 1346269 - 1})")

    wykres_czasu(N_t, T,
                 os.path.join(OUT_DIR, "fib_czas.png"))
    wykres_ilorazów(N_t, T,
                    os.path.join(OUT_DIR, "fib_ilorazy_czasu.png"),
                    y_label="czas fib(n+1) / czas fib(n)")
    wykres_wywołań(N_c, C,
                   os.path.join(OUT_DIR, "fib_wywolania.png"))
    wykres_ilorazów(N_c, C,
                    os.path.join(OUT_DIR, "fib_ilorazy_wywolan.png"),
                    y_label="liczba wywołań fib(n+1) / liczba wywołań fib(n)")

    print(f"\nRysunki zapisane w katalogu {OUT_DIR}/")


if __name__ == "__main__":
    main()
