"""Sortowanie i filtrowanie z wyrażeniami lambda."""

import doctest


def sort_by_second(pairs):
    """Sortuje listę krotek rosnąco po drugim elemencie.

    >>> sort_by_second([(1, 3), (2, 1), (3, 2)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_by_second([('a', 5), ('b', 2), ('c', 8)])
    [('b', 2), ('a', 5), ('c', 8)]
    """
    return sorted(pairs, key=lambda p: p[1])


def sort_words_by_last_char(words):
    """Sortuje listę słów alfabetycznie po ostatnim znaku.

    >>> sort_words_by_last_char(['python', 'java', 'rust', 'go'])
    ['java', 'python', 'go', 'rust']
    """
    return sorted(words, key=lambda w: w[-1])


def filter_long_words(words, min_length):
    """Zwraca listę słów o długości co najmniej min_length.

    >>> filter_long_words(['ala', 'ma', 'kota', 'i', 'psa'], 3)
    ['ala', 'kota', 'psa']
    >>> filter_long_words(['x', 'yy', 'zzz'], 4)
    []
    """
    return list(filter(lambda w: len(w) >= min_length, words))


if __name__ == "__main__":
    doctest.testmod(verbose=True)
