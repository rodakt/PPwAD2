from itertools import product


def sklej(liczby, operatory):
    """Skleja w `liczby` te sąsiednie wyrazy, między którymi operator to ''.

    Modyfikuje przekazane listy i zwraca je: po sklejeniu w `operatory`
    zostają już tylko '+' i '-', a `liczby` to napisy odpowiednich liczb.

    >>> sklej(['1', '2', '3'], ['+', ''])
    (['1', '23'], ['+'])
    >>> sklej(['1', '2', '3'], ['', ''])
    (['123'], [])
    """
    while "" in operatory:
        i = operatory.index("")
        liczby[i] = str(liczby[i]) + str(liczby[i + 1])
        del liczby[i + 1]
        del operatory[i]
    return liczby, operatory


def make_expressions(digits, target):
    """Lista napisów-wyrażeń złożonych z cyfr `digits` równych `target`.

    W każdą z przerw między cyframi wstawiamy '+', '-' lub ''
    (sklejenie sąsiednich cyfr w jedną liczbę).
    Wyrażenia w kolejności leksykograficznej.

    >>> make_expressions('12', 3)
    ['1+2']
    >>> make_expressions('12', -1)
    ['1-2']
    >>> make_expressions('123', 6)
    ['1+2+3']
    >>> '1+2+3-4+5+6+78+9' in make_expressions('123456789', 100)
    True
    """
    wyniki = []
    for operatory in product(['+', '-', ''], repeat=len(digits) - 1):
        liczby, znaki = sklej(list(digits), list(operatory))
        wartość = int(liczby[0])
        for znak, liczba in zip(znaki, liczby[1:]):
            if znak == '+':
                wartość += int(liczba)
            else:
                wartość -= int(liczba)
        if wartość == target:
            wyrażenie = liczby[0]
            for znak, liczba in zip(znaki, liczby[1:]):
                wyrażenie += znak + liczba
            wyniki.append(wyrażenie)
    return sorted(wyniki)
