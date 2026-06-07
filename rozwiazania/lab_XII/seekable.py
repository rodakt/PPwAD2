class Seekable:
    """Iterator po sekwencji z możliwością swobodnego przesuwania się
    po pozycjach.

    >>> s = Seekable([10, 20, 30, 40, 50])
    >>> len(s)
    5
    >>> next(s)
    10
    >>> next(s)
    20
    >>> s.tell()
    2
    >>> s.peek()
    30
    >>> s.peek()
    30
    >>> s.tell()
    2
    >>> next(s)
    30
    >>> s.seek(0)
    >>> list(s)
    [10, 20, 30, 40, 50]
    >>> s.tell()
    5
    >>> next(s)
    Traceback (most recent call last):
        ...
    StopIteration
    >>> s.seek(3)
    >>> next(s)
    40
    >>> s.seek(5)
    >>> s.peek()
    Traceback (most recent call last):
        ...
    StopIteration
    >>> s.seek(-1)
    Traceback (most recent call last):
        ...
    IndexError: pozycja poza zakresem
    >>> s.seek(6)
    Traceback (most recent call last):
        ...
    IndexError: pozycja poza zakresem
    """

    def __init__(self, seq):
        self.seq = list(seq)
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.seq):
            raise StopIteration
        element = self.seq[self.pos]
        self.pos += 1
        return element

    def __len__(self):
        return len(self.seq)

    def tell(self):
        return self.pos

    def seek(self, i):
        if not 0 <= i <= len(self.seq):
            raise IndexError('pozycja poza zakresem')
        self.pos = i

    def peek(self):
        if self.pos >= len(self.seq):
            raise StopIteration
        return self.seq[self.pos]
