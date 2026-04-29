def compose(f, g):
    """
    Zwraca funkcję, która jest złożeniem funkcji f i g. Funkcja f jest
    wywoływana na wyniku funkcji g. Zwrócona funkcja przyjmuje takie same
    argumenty jak g.

    Parametry:
    f -- funkcja, która ma być wywołana na wyniku funkcji g
    g -- funkcja, która ma być wywołana jako pierwsza

    Zwraca:
    funkcję, która jest złożeniem f i g

    Przykłady:
    >>> def add_one(x):
    ...     return x + 1
    >>> def square(x):
    ...     return x * x
    >>> add_one_square = compose(add_one, square)
    >>> add_one_square(2)
    5
    >>> square_add_one = compose(square, add_one)
    >>> square_add_one(2)
    9
    >>> compose(str, pow)(2, 10)
    '1024'
    """
    def fg(*args, **kwargs):
        return f(g(*args, **kwargs))
    return fg


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
