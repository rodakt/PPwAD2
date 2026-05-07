def maximum_rec(seq):
    if len(seq) == 0:
        raise ValueError("sekwencja nie może być pusta")
    if len(seq) == 1:
        return seq[0]
    return max(seq[0], maximum_rec(seq[1:]))


def _maximum_tail(seq, max_val):
    if len(seq) == 0:
        return max_val
    return _maximum_tail(seq[1:], max(seq[0], max_val))


def maximum_tail(seq):
    if len(seq) == 0:
        raise ValueError("sekwencja nie może być pusta")
    return _maximum_tail(seq[1:], seq[0])
