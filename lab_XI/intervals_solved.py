from itertools import combinations

from open_interval import OpenInterval

CUP = "\u222A"
EMPTY_SET = "\u2205"


def merge_intervals(list_of_intervals):
    """
    Zwraca sumę przedziałów otwartych na osi liczbowej.

    Parametry:
    list_of_intervals -- lista przedziałów otwartych (obiektów klasy OpenInterval)

    Zwraca:
    lista niezachodzących na siebie przedziałów otwartych (obiektów klasy OpenInterval)
    """
    for A, B in combinations(list_of_intervals, 2):
        if (A & B) or (not A) or (not B):
            list_of_intervals.remove(A)
            list_of_intervals.remove(B)
            list_of_intervals.append(A | B)
            return merge_intervals(list_of_intervals)
    return list_of_intervals


class Intervals:
    """Obiekty tej klasy reprezentują sumy przedziałów otwartych na osi liczbowej."""

    def __init__(self, *intervals):
        if not intervals:
            self.intervals = [OpenInterval(0, 0)]
        else:
            intervals = [
                (
                    interval
                    if isinstance(interval, OpenInterval)
                    else OpenInterval(*interval)
                )
                for interval in intervals
            ]
            intervals = merge_intervals(intervals)
            self.intervals = sorted(intervals, key=lambda x: x.start)

    def __len__(self):
        return sum(map(len, self.intervals))

    def __bool__(self):
        return bool(len(self))

    def __repr__(self):
        return f"Intervals({', '.join(map(repr, self.intervals))})"

    def __str__(self):
        return f" {CUP} ".join(map(str, self.intervals))

    def __contains__(self, x):
        return any(x in interval for interval in self.intervals)

    def __eq__(self, other):
        return self.intervals == other.intervals

    def __and__(self, other):
        return Intervals(
            *[A & B for A in self.intervals for B in other.intervals if A & B]
        )

    def __or__(self, other):
        return Intervals(*self.intervals, *other.intervals)
