def integer_square_root(n):
    if n < 0:
        raise ValueError("argument musi być nieujemny")
    # szukamy największego x takiego, że x**2 <= n
    # przedział przeszukiwania: [a, b] - n jest górnym ograniczeniem pierwiastka
    a, b = 0, n
    while a < b:
        # +1 przesuwa x w górę, żeby uniknąć nieskończonej pętli gdy b = a + 1
        x = (a + b + 1) // 2
        if x ** 2 <= n:
            a = x
        else:
            b = x - 1
    return a


def integer_cubic_root(n):
    if n < 0:
        raise ValueError("argument musi być nieujemny")
    a, b = 0, n
    while a < b:
        x = (a + b + 1) // 2
        if x ** 3 <= n:
            a = x
        else:
            b = x - 1
    return a


def is_perfect_square(n):
    if n < 0:
        return False
    m = integer_square_root(n)
    return m ** 2 == n


def is_perfect_cube(n):
    if n < 0:
        # (-m)**3 == -(m**3), więc wystarczy sprawdzić -n
        return is_perfect_cube(-n)
    m = integer_cubic_root(n)
    return m ** 3 == n
