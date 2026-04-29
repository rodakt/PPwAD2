def make_counter(start=0, step=1):
    """
    Zwraca funkcję, która jest licznikiem. Funkcja ta, po każdym wywołaniu,
    zwraca kolejną liczbę, zaczynając od `start` z odstępem `step`.

    Parametry:
    start -- liczba, od której zaczynamy zliczać
    step -- liczba, o którą zmieniamy licznik po każdym wywołaniu

    Zwraca:
    funkcję, która zlicza od start do nieskończoności

    Przykłady:
    >>> counter = make_counter()
    >>> counter()
    0
    >>> counter()
    1
    >>> counter()
    2
    >>> new_counter = make_counter(10)
    >>> new_counter()
    10
    >>> new_counter()
    11
    >>> yet_another_counter = make_counter(10, 2)
    >>> yet_another_counter()
    10
    >>> yet_another_counter()
    12
    >>> yet_another_counter()
    14
    >>> counter()
    3
    >>> new_counter()
    12
    >>> float_counter = make_counter(0.5, -0.5)
    >>> float_counter()
    0.5
    >>> float_counter()
    0.0
    >>> float_counter()
    -0.5
    """
    n = start

    def increment():
        nonlocal n
        wynik = n
        n += step
        return wynik

    return increment


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
