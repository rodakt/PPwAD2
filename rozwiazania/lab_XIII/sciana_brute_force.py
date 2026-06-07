import random
import time
import math
from route import shortest_route


def losowa_macierz(n, lo=1, hi=99):
    """Losowa symetryczna macierz n×n odległości całkowitych (zera na przekątnej)."""
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = random.randint(lo, hi)
            M[i][j] = d
            M[j][i] = d
    return M


print(f"{'n':>4}  {'(n-1)!':>12}  {'czas [s]':>10}")
print("-" * 32)

for n in range(5, 13):
    M = losowa_macierz(n)
    t0 = time.perf_counter()
    shortest_route(M)
    t1 = time.perf_counter()
    permutacji = math.factorial(n - 1)
    print(f"{n:>4}  {permutacji:>12}  {t1 - t0:>10.4f}")
