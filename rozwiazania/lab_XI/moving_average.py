class RatioAccumulator:
    """Klasa bazowa: prowadzi dwie sumy bieżące i zwraca ich iloraz.

    >>> r = RatioAccumulator()
    >>> r.numerator, r.denominator
    (0, 0)
    >>> r.add(2, 1)
    2.0
    >>> r.add(4, 1)
    3.0
    >>> r.numerator, r.denominator
    (6, 2)
    >>> r.add(0, 2)
    1.5
    """

    def __init__(self):
        self.numerator = 0
        self.denominator = 0

    def add(self, a, b):
        self.numerator += a
        self.denominator += b
        return self.numerator / self.denominator


class MovingAverage(RatioAccumulator):
    """Średnia arytmetyczna kolejno dodawanych wartości.

    >>> m = MovingAverage()
    >>> m.add_value(10)
    10.0
    >>> m.add_value(20)
    15.0
    >>> m.add_value(30)
    20.0
    >>> m.numerator, m.denominator
    (60, 3)
    """

    def add_value(self, value):
        return self.add(value, 1)


class AverageSpeed(RatioAccumulator):
    """Prędkość średnia obliczana z kolejnych odcinków drogi i czasu.

    >>> v = AverageSpeed()
    >>> v.add_section(100, 2)
    50.0
    >>> v.add_section(200, 3)
    60.0
    >>> v.numerator, v.denominator
    (300, 5)
    """

    def add_section(self, distance, time):
        return self.add(distance, time)
