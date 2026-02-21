"""Moduł zawierający klasę OpenInterval reprezentującą przedziały otwarte na osi liczbowej."""
EMPTY_SET = "\u2205"


class OpenInterval:
    """Obiekty tej klasy reprezentują przedziały otwarte na osi liczbowej."""

    def __init__(self, start, end):
        if start >= end:
            start, end = 0, 0
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start

    def __bool__(self):
        return self.start < self.end

    def __repr__(self):
        return f"OpenInterval({self.start}, {self.end})"

    def __str__(self):
        if self:
            return f"({self.start}, {self.end})"
        return EMPTY_SET

    def __contains__(self, x):
        return self.start < x < self.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __and__(self, other):
        if not self or not other:
            return OpenInterval(0, 0)
        return OpenInterval(max(self.start, other.start), min(self.end, other.end))

    def __or__(self, other):
        if not self:
            return other
        if not other:
            return self
        if self & other:
            return OpenInterval(min(self.start, other.start), max(self.end, other.end))
        raise NotImplementedError("Przedziały nie zachodzą na siebie")
