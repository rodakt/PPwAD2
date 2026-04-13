import doctest


def remove_all_in_place(lst, value):
    """Usuwa wszystkie wystąpienia value z lst, modyfikując ją w miejscu.

    Zgłasza ValueError, jeśli value nie występuje w lst.
    Zwraca None.

    >>> lst = [1, 3, 2, 3, 4]
    >>> remove_all_in_place(lst, 3)
    >>> lst
    [1, 2, 4]
    >>> lst = list("hello")
    >>> remove_all_in_place(lst, "l")
    >>> lst
    ['h', 'e', 'o']
    >>> lst = [2, 2, 2]
    >>> remove_all_in_place(lst, 2)
    >>> lst
    []
    >>> lst = [1, 2, 3]
    >>> remove_all_in_place(lst, 4)
    Traceback (most recent call last):
        ...
    ValueError: 4 not in lst
    >>> lst = 1_000_000 * [1]
    >>> remove_all_in_place(lst, 1)
    >>> lst
    []
    """
    if value not in lst:
        raise ValueError(f"{value} not in lst")
    # dwa indeksy: zapis wskazuje gdzie zapisać kolejny zachowany element
    # odczyt przebiega całą listę, zapis przesuwa się tylko dla elementów != value
    zapis = 0
    for odczyt in range(len(lst)):
        if lst[odczyt] != value:
            lst[zapis] = lst[odczyt]
            zapis += 1
    # usuwamy ogon jedną operacją - del lst[i:] jest O(1) względem usuniętych
    del lst[zapis:]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
