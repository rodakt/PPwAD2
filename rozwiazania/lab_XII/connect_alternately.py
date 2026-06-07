def connect_alternately2(it1, it2):
    """Naprzemiennie łączy dwa iteratory.

    >>> list(connect_alternately2([1, 2, 3], 'abc'))
    [1, 'a', 2, 'b', 3, 'c']
    >>> list(connect_alternately2([1, 2, 3, 4, 5], 'ab'))
    [1, 'a', 2, 'b', 3]
    >>> list(connect_alternately2([], 'abc'))
    []
    """
    it1, it2 = iter(it1), iter(it2)
    while True:
        try:
            yield next(it1)
            yield next(it2)
        except StopIteration:
            return


def connect_alternately(*its):
    """Naprzemiennie łączy dowolną liczbę iteratorów.

    >>> list(connect_alternately([1, 2, 3], 'abc', [10, 20, 30]))
    [1, 'a', 10, 2, 'b', 20, 3, 'c', 30]
    >>> list(connect_alternately([1, 2], 'abc', [10, 20, 30]))
    [1, 'a', 10, 2, 'b', 20]
    >>> list(connect_alternately())
    []
    >>> list(connect_alternately('abc'))
    ['a', 'b', 'c']
    """
    if not its:
        return
    its = [iter(it) for it in its]
    while True:
        for it in its:
            try:
                yield next(it)
            except StopIteration:
                return
