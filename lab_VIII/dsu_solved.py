"""Moduł DSU - Decorate-Sort-Undecorate.

Zawiera dekoratory wprowadzające mechanizm DSU do funkcji szukających
najmniejszego/największego elementu w sekwencji 
i do funkcji sortujących sekwencję.
"""

from functools import wraps


def key_minmax(key=None):
    """Dekorator wprowadzający klucz do funkcji min/max"""

    def decorator(minmax):
        if key is None:
            return minmax

        @wraps(minmax)
        def wrapper(seq):
            seq = [(key(x), i, x) for i, x in enumerate(seq)]
            _, _, result = minmax(seq)
            return result

        return wrapper

    return decorator


def key_sort(key=None):
    """Dekorator wprowadzający klucz do funkcji sort"""

    def decorator(sort_func):
        if key is None:
            return sort_func

        @wraps(sort_func)
        def wrapper(seq):
            seq = [(key(x), i, x) for i, x in enumerate(seq)]
            seq = [x for _, _, x in sort_func(seq)]
            return seq

        return wrapper

    return decorator
