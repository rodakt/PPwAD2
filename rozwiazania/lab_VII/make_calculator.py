def calculator(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            raise ValueError("Dzielenie przez zero")
        return x / y
    else:
        raise ValueError("Nieznana operacja")


def make_calculator(operation):
    """Zwraca kalkulator w postaci złożenia funkcji jednoparametrowych.

    make_calculator(operation)(x)(y) == calculator(x, y, operation)

    >>> make_calculator('+')(2)(3)
    5
    >>> make_calculator('-')(10)(4)
    6
    >>> make_calculator('*')(3)(7)
    21
    >>> make_calculator('/')(10)(4)
    2.5
    """
    def with_x(x):
        def with_y(y):
            if operation == '+':
                return x + y
            elif operation == '-':
                return x - y
            elif operation == '*':
                return x * y
            elif operation == '/':
                if y == 0:
                    raise ValueError("Dzielenie przez zero")
                return x / y
            else:
                raise ValueError("Nieznana operacja")
        return with_y
    return with_x


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
