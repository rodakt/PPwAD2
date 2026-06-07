from itertools import permutations


def solve_cryptarithm(*words):
    """Brute force rozwiązań kryptarytmu: suma words[:-1] == words[-1].

    Każda litera oznacza inną cyfrę; litera wiodąca nie może być zerem.
    Zwraca listę krotek wartości liczbowych słów — po jednej na rozwiązanie.

    >>> solve_cryptarithm('A', 'A', 'B')        # A + A == B
    [(1, 1, 2), (2, 2, 4), (3, 3, 6), (4, 4, 8)]
    >>> len(solve_cryptarithm('SEND', 'MORE', 'MONEY'))
    1
    """
    litery = sorted(set(''.join(words)))
    wiodące = {w[0] for w in words}
    rozwiązania = []
    for perm in permutations(range(10), len(litery)):
        przyp = dict(zip(litery, perm))
        if any(przyp[l] == 0 for l in wiodące):
            continue
        wartości = []
        for słowo in words:
            liczba = 0
            for litera in słowo:
                liczba = liczba * 10 + przyp[litera]
            wartości.append(liczba)
        if sum(wartości[:-1]) == wartości[-1]:
            rozwiązania.append(tuple(wartości))
    return rozwiązania
