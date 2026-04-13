def euclid(a, b):
    """Zwraca krotkę (reszty, ilorazy) z algorytmu Euklidesa dla a i b > 0."""
    if b <= 0:
        raise ValueError("argument b musi być dodatni")
    reszty = [a, b]
    ilorazy = []
    # kolejne kroki: r1 = q * r2 + r3; kończymy gdy reszta = 0
    while reszty[-1] != 0:
        r1, r2 = reszty[-2], reszty[-1]
        ilorazy.append(r1 // r2)
        reszty.append(r1 % r2)
    return (reszty, ilorazy)


def gcd(a, b):
    """Zwraca największy wspólny dzielnik a i b (zawsze nieujemny)."""
    # klasyczny algorytm Euklidesa - O(log min(a,b)), działa dla ujemnych przez abs
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def to_float(seq):
    """Zwraca wartość ułamka łańcuchowego jako liczbę zmiennoprzecinkową."""
    if not seq:
        raise ValueError("sekwencja współczynników nie może być pusta")
    # rozwijamy od prawej: a_n, potem a_{n-1} + 1/wynik, ...
    wynik = seq[-1]
    for a in reversed(seq[:-1]):
        wynik = a + 1 / wynik
    return float(wynik)


def to_fraction(seq):
    """Zwraca wartość ułamka łańcuchowego jako krotkę (licznik, mianownik)."""
    if not seq:
        raise ValueError("sekwencja współczynników nie może być pusta")
    # rozwijamy od prawej: reprezentujemy wynik jako ułamek p/q
    # krok: a + 1/(p/q) = a + q/p = (a*p + q) / p
    p, q = seq[-1], 1
    for a in reversed(seq[:-1]):
        p, q = a * p + q, p
    return (p, q)


def continued_fraction(a, b):
    """Zwraca ułamek łańcuchowy dla a/b jako listę współczynników."""
    if b == 0:
        raise ZeroDivisionError("mianownik nie może być równy 0")
    # normalizujemy do b > 0 wymaganego przez euclid
    if b < 0:
        a, b = -a, -b
    _, ilorazy = euclid(a, b)
    return ilorazy


if __name__ == '__main__':
    # znajdź p/q z przedziału [1, 1000] x [1, 1000] o najdłuższym rozwinięciu
    najdłuższy = []
    najlepsze = (1, 1)
    for p in range(1, 1001):
        for q in range(1, 1001):
            cf = continued_fraction(p, q)
            if len(cf) > len(najdłuższy):
                najdłuższy = cf
                najlepsze = (p, q)
    p, q = najlepsze
    print(f"{p}/{q} = {najdłuższy}")
