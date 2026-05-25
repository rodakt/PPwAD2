from itertools import combinations

from open_interval import OpenInterval


def _merge(intervals):
    while True:
        scalono = False
        for a, b in combinations(intervals, 2):
            if a & b:
                intervals.remove(a)
                intervals.remove(b)
                intervals.append(a | b)
                scalono = True
                break
        if not scalono:
            return intervals


class Intervals:
    """Skończona suma przedziałów otwartych na osi liczbowej.

    >>> i1 = Intervals((1, 5))
    >>> i2 = Intervals((3, 7))
    >>> i3 = Intervals((5, 9))
    >>> i4 = Intervals((6, 7))
    >>> i5 = Intervals((8, 9))
    >>> i6 = Intervals((10, 20))
    >>> i1
    Intervals(OpenInterval(1, 5))
    >>> print(i1)
    (1, 5)
    >>> i1 & i2
    Intervals(OpenInterval(3, 5))
    >>> i1 | i2
    Intervals(OpenInterval(1, 7))
    >>> 4 in (i1 | i3)
    True
    >>> 5 in (i1 | i3)
    False
    >>> bool(i1 | i6)
    True
    >>> bool(i1 & i6)
    False
    >>> i1 & i2 | i3
    Intervals(OpenInterval(3, 5), OpenInterval(5, 9))
    >>> (i1 | i5) & (i2 | i4)
    Intervals(OpenInterval(3, 5))
    >>> (i1 | i5) & (i2 | i4) == (i1 & i2) | (i1 & i4) | (i5 & i2) | (i5 & i4)
    True
    >>> Intervals((1, 3), (3, 5))
    Intervals(OpenInterval(1, 3), OpenInterval(3, 5))
    >>> 3 in Intervals((1, 3), (3, 5))
    False
    >>> Intervals()
    Intervals(OpenInterval(0, 0))
    >>> print(Intervals())
    ∅
    """

    def __init__(self, *intervals):
        lista = []
        for i in intervals:
            if isinstance(i, tuple):
                lista.append(OpenInterval(*i))
            else:
                lista.append(i)
        lista = [i for i in lista if i]
        if not lista:
            self.intervals = [OpenInterval(0, 0)]
        else:
            self.intervals = sorted(_merge(lista), key=lambda i: i.start)

    def length(self):
        return sum(i.length() for i in self.intervals)

    def __bool__(self):
        return any(self.intervals)

    def __repr__(self):
        return f"Intervals({', '.join(repr(i) for i in self.intervals)})"

    def __str__(self):
        if not self:
            return "\u2205"
        return " \u222a ".join(str(i) for i in self.intervals)

    def __contains__(self, x):
        return any(x in i for i in self.intervals)

    def __eq__(self, other):
        return self.intervals == other.intervals

    def __and__(self, other):
        przeciecia = [a & b for a in self.intervals for b in other.intervals if a & b]
        return Intervals(*przeciecia) if przeciecia else Intervals()

    def __or__(self, other):
        return Intervals(*self.intervals, *other.intervals)
