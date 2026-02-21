def integer_square_root(n):
    """
    Given a non-negative integer n, return the biggest integer x such that x**2 <= n
    """
    if n < 0:
        raise ValueError("argument musi być nieujemny")

    if n in {0, 1}:
        return n

    left, right = 0, n
    while True:
        if right - left <= 1:
            return left
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid
        else:
            right = mid


def integer_cubic_root(n):
    """
    Given a non-negative integer n, return the biggest integer x such that x**3 <= n
    """
    if n < 0:
        raise ValueError("argument musi być nieujemny")

    if n in {0, 1}:
        return n

    left, right = 0, n
    while True:
        if right - left <= 1:
            return left
        mid = (left + right) // 2
        if mid * mid * mid <= n:
            left = mid
        else:
            right = mid


def is_perfect_square(n):
    """
    Given a non-negative integer n, return True if n is a perfect square, False otherwise
    """
    if n < 0:
        return False
    x = integer_square_root(n)
    return x * x == n


def is_perfect_cube(n):
    """
    Given a non-negative integer n, return True if n is a perfect cube, False otherwise
    """
    if n < 0:
        n = -n
    x = integer_cubic_root(n)
    return x * x * x == n
