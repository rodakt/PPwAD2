def count_change(amount, coins):
    """Zwraca liczbę sposobów wydania reszty amount mając do dyspozycji monety o nominałach coins.

    >>> count_change(0, [])
    1
    >>> count_change(0, [1, 2, 3])
    1
    >>> count_change(-1, [])
    0
    >>> count_change(-1, [1, 2, 3])
    0
    >>> count_change(5, [7, 9])
    0
    >>> count_change(5, [1])
    1
    >>> count_change(5, [1, 2])
    3
    >>> count_change(100, [1, 5, 10, 25, 50])  # SICP, Ćw. 2.19
    292
    """
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)
