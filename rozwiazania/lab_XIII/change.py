from itertools import combinations_with_replacement


def make_change(amount, coins):
    """Wszystkie sposoby wydania kwoty `amount` monetami o nominałach `coins`.

    Każdy sposób to krotka użytych monet (rosnąco). Kolejność monet
    w sposobie nie ma znaczenia, każdego nominału można użyć dowolnie wiele razy.

    >>> make_change(5, [1, 2, 5])
    [(5,), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)]
    >>> len(make_change(5, [1, 2, 5]))
    4
    >>> make_change(4, [2, 5])
    [(2, 2)]
    """
    coins = sorted(coins)
    wynik = []
    for r in range(1, amount // min(coins) + 1):
        for kombinacja in combinations_with_replacement(coins, r):
            if sum(kombinacja) == amount:
                wynik.append(kombinacja)
    return wynik
