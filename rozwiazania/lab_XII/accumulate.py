def accumulate(it, func, *, initial=None):
    """Generator bieżących wartości akumulowanych operacją `func`.

    >>> from operator import add, mul
    >>> list(accumulate([1, 2, 3, 4], add))
    [1, 3, 6, 10]
    >>> list(accumulate([1, 2, 3, 4], add, initial=0))
    [0, 1, 3, 6, 10]
    >>> list(accumulate([1, 2, 3, 4], mul, initial=1))
    [1, 1, 2, 6, 24]
    >>> list(accumulate([1, 2, 3, 2, 0, 7], max))
    [1, 2, 3, 3, 3, 7]
    >>> list(accumulate([1, 2, 3, 2, 0, 7], min))
    [1, 1, 1, 1, 0, 0]
    >>> list(accumulate([], add))
    []
    >>> list(accumulate([], add, initial=0))
    [0]
    """
    it = iter(it)
    if initial is None:
        try:
            bieżąca = next(it)
        except StopIteration:
            return
    else:
        bieżąca = initial
    yield bieżąca
    for element in it:
        bieżąca = func(bieżąca, element)
        yield bieżąca
