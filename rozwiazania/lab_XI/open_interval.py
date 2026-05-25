class OpenInterval:
    """Przedział otwarty na osi liczbowej.

    >>> i1 = OpenInterval(1, 3)
    >>> i2 = OpenInterval(2, 4)
    >>> i1
    OpenInterval(1, 3)
    >>> print(i1)
    (1, 3)
    >>> i1.length()
    2
    >>> i1 & i2
    OpenInterval(2, 3)
    >>> i1 | i2
    OpenInterval(1, 4)
    >>> 2 in i1
    True
    >>> 4 in i1
    False
    >>> bool(i1)
    True
    >>> i1 == i2
    False
    >>> (i1 | i2) == OpenInterval(1, 4)
    True
    >>> empty = OpenInterval(5, 3)
    >>> empty
    OpenInterval(0, 0)
    >>> bool(empty)
    False
    >>> print(empty)
    ∅
    >>> empty.length()
    0
    >>> empty == OpenInterval(7, 7)
    True
    >>> i1 | OpenInterval(4, 5)             # rozłączne
    Traceback (most recent call last):
        ...
    NotImplementedError: Suma nie jest przedziałem otwartym
    >>> OpenInterval(1, 3) | OpenInterval(3, 5)   # dotykają się końcami
    Traceback (most recent call last):
        ...
    NotImplementedError: Suma nie jest przedziałem otwartym
    """

    def __init__(self, start, end):
        if start >= end:
            self.start = 0
            self.end = 0
        else:
            self.start = start
            self.end = end

    def length(self):
        return self.end - self.start

    def __bool__(self):
        return self.start < self.end

    def __repr__(self):
        return f"OpenInterval({self.start}, {self.end})"

    def __str__(self):
        if not self:
            return "\u2205"
        return f"({self.start}, {self.end})"

    def __contains__(self, x):
        return self.start < x < self.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __and__(self, other):
        return OpenInterval(max(self.start, other.start), min(self.end, other.end))

    def __or__(self, other):
        if not self:
            return other
        if not other:
            return self
        if self & other:
            return OpenInterval(min(self.start, other.start), max(self.end, other.end))
        raise NotImplementedError("Suma nie jest przedziałem otwartym")
