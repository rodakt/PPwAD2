def qsort(seq):
    """Zwraca nową listę wartości z seq posortowaną niemalejąco."""
    seq = list(seq)
    if len(seq) <= 1:
        return seq
    pivot = seq[-1]
    X = [x for x in seq if x < pivot]
    Y = [x for x in seq if x == pivot]
    Z = [x for x in seq if x > pivot]
    return qsort(X) + Y + qsort(Z)
