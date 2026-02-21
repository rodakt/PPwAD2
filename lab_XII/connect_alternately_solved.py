"""Moduł zawiera funkcje connect_alternately() i connect_alternately2().

Funkcje te zwracają iteratory biegnące naprzemiennie po dwóch lub więcej
obiektach iterowalnych.
"""


def connect_alternately2(it1, it2):
    """
    Łączy dwa iteratory naprzemiennie, zwracając elementy z każdego z nich na przemian.

    Args:
        it1, it2: Obiekty iterowalne.

    Yields:
        Elementy z obu iteratorów na przemian.

    Raises:
        StopIteration: Po wyczerpaniu któregokolwiek z obiektów iterowalnych.
    """
    it1 = iter(it1)
    it2 = iter(it2)
    while True:
        try:
            yield next(it1)
        except StopIteration:
            break
        try:
            yield next(it2)
        except StopIteration:
            break


def connect_alternately(*its):
    """
    Łączy wiele obiektów iterowalnych naprzemiennie.

    Args:
        its: Obiekty iterowalne.

    Yields:
        Elementy z obiektów iterowalnych na przemian.

    Raises:
        StopIteration: Po wyczerpaniu któregokolwiek z obiektów iterowalnych.
    """
    its = [iter(it) for it in its]
    while True:
        for it in its:
            try:
                yield next(it)
            except StopIteration:
                return
