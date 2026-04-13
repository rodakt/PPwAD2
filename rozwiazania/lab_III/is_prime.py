def is_prime(n):
    if n < 0:
        raise ValueError("argument musi być nieujemny")
    if n < 2:
        # 0 i 1 nie są liczbami pierwszymi z definicji
        return False
    # sprawdzamy dzielniki od 2 do sqrt(n) włącznie
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
