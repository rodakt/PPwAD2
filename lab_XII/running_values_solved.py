"""Moduł zawierający funkcje generujące iteratory bieżących wartości."""


def running_total(it):
    """Iterator bieżącej sumy elementów z obiektu iterowalnego it."""
    it = iter(it)
    total = 0
    yield total

    for value in it:
        total += value
        yield total


def running_product(it):
    """Iterator bieżącego iloczynu elementów z obiektu iterowalnego it."""
    it = iter(it)
    product = 1
    yield product

    for value in it:
        product *= value
        yield product


def running_max(it, key=lambda x: x):
    """
    Iterator bieżącego maksimum elementów z obiektu iterowalnego it.

    Zwraca wartość, gdy maksimum jest aktualizowane.
    """
    it = iter(it)
    max_value = None

    for value in it:
        if max_value is None or key(value) > key(max_value):
            max_value = value
            yield max_value


def running_min(it, key=lambda x: x):
    """
    Iterator bieżącego minimum elementów z obiektu iterowalnego it.

    Zwraca wartość, gdy minimum jest aktualizowane.
    """
    it = iter(it)
    min_value = None

    for value in it:
        if min_value is None or key(value) < key(min_value):
            min_value = value
            yield min_value


def running_extremum(it, key=lambda x: x):
    """
    Iterator bieżących wartości ekstremalnych z obiektu iterowalnego it.

    Zwraca wartość, gdy jedno z ekstremów jest aktualizowane.
    """
    it = iter(it)
    max_value, min_value = None, None

    for value in it:
        if max_value is None or key(value) > key(max_value):
            max_value = value
            yield max_value
        elif min_value is None or key(value) < key(min_value):
            min_value = value
            yield min_value
