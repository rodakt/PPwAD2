class ZZ:
    """Reszta modulo m z arytmetyką modularną.

    >>> a = ZZ(5, 7)
    >>> b = ZZ(4, 7)
    >>> a
    ZZ(5, 7)
    >>> print(a)
    [5]_7
    >>> a + b
    ZZ(2, 7)
    >>> a - b
    ZZ(1, 7)
    >>> a * b
    ZZ(6, 7)
    >>> -a
    ZZ(2, 7)
    >>> a + (-a) == ZZ(0, 7)
    True
    >>> 3 * a
    ZZ(1, 7)
    >>> (-2) * a
    ZZ(4, 7)
    >>> a.inverse()
    ZZ(3, 7)
    >>> a * a.inverse() == ZZ(1, 7)
    True
    >>> ZZ(15, 7)                           # redukcja w inicjalizatorze
    ZZ(1, 7)
    >>> ZZ(-1, 7)                           # ujemne też redukowane
    ZZ(6, 7)
    >>> ZZ(2, 6).inverse()
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Element nie ma odwrotności
    >>> ZZ(3, 7) + ZZ(3, 5)
    Traceback (most recent call last):
        ...
    ValueError: Niezgodne modulusy
    >>> ZZ(0, 1)
    Traceback (most recent call last):
        ...
    ValueError: Modulus musi być >= 2
    """

    def __init__(self, value, modulus):
        if modulus < 2:
            raise ValueError("Modulus musi być >= 2")
        self.modulus = modulus
        self.value = value % modulus

    def __repr__(self):
        return f"ZZ({self.value}, {self.modulus})"

    def __str__(self):
        return f"[{self.value}]_{self.modulus}"

    def __eq__(self, other):
        return self.value == other.value and self.modulus == other.modulus

    def _sprawdz_modulusy(self, other):
        if self.modulus != other.modulus:
            raise ValueError("Niezgodne modulusy")

    def __add__(self, other):
        self._sprawdz_modulusy(other)
        return ZZ(self.value + other.value, self.modulus)

    def __sub__(self, other):
        self._sprawdz_modulusy(other)
        return ZZ(self.value - other.value, self.modulus)

    def __mul__(self, other):
        self._sprawdz_modulusy(other)
        return ZZ(self.value * other.value, self.modulus)

    def __neg__(self):
        return ZZ(-self.value, self.modulus)

    def __rmul__(self, k):
        return ZZ(k * self.value, self.modulus)

    def inverse(self):
        for b in range(1, self.modulus):
            if (self.value * b) % self.modulus == 1:
                return ZZ(b, self.modulus)
        raise ZeroDivisionError("Element nie ma odwrotności")
