class Squares:
    """Klasa reprezentująca nieskończony ciąg kwadratów
    kolejnych nieujemnych liczb całkowitych.

    >>> s = Squares()
    >>> s.nxt()
    0
    >>> s.nxt()
    1
    >>> [s.nxt() for _ in range(5)]
    [4, 9, 16, 25, 36]
    >>> t = Squares()
    >>> t.nxt()
    0
    >>> s.nxt()
    49
    """

    def __init__(self):
        self.n = 0

    def nxt(self):
        wynik = self.n ** 2
        self.n += 1
        return wynik
