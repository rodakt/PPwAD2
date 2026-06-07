from itertools import combinations


def subsets_with_sum(numbers, target):
    """Wszystkie niepuste podzbiory `numbers` o sumie równej `target`.

    >>> subsets_with_sum([2, 3, 5, 7], 10)
    [(3, 7), (2, 3, 5)]
    >>> subsets_with_sum([1, 2, 3, 4, 5], 5)
    [(5,), (1, 4), (2, 3)]
    >>> subsets_with_sum([1, 2, 3], 100)
    []
    """
    wyniki = []
    for r in range(1, len(numbers) + 1):
        for podzbiór in combinations(numbers, r):
            if sum(podzbiór) == target:
                wyniki.append(podzbiór)
    return wyniki
