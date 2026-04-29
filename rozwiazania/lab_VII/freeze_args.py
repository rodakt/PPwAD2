"""Zamrażanie argumentów funkcji."""


def freeze_args(f, *args, **kwargs):
    """Zwraca funkcję zachowującą się jak f z zamrożonymi argumentami.

    >>> def add(a, b):
    ...     return a + b
    >>> add5 = freeze_args(add, 5)
    >>> add5(3)
    8
    >>> add5(10)
    15
    >>> power_of_2 = freeze_args(pow, 2)
    >>> power_of_2(10)
    1024
    >>> power_of_2(8)
    256
    >>> say_hello = freeze_args(print, "Hello", sep=", ")
    >>> say_hello("World")
    Hello, World
    >>> say_hello("Python")
    Hello, Python
    """
    def frozen(*extra_args, **extra_kwargs):
        return f(*args, *extra_args, **kwargs, **extra_kwargs)
    return frozen

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)