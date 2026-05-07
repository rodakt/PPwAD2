def binary_search(x, seq):
    """
    Wykonuje rekurencyjne wyszukiwanie binarne w uporządkowanej sekwencji.

    Args:
        x (any): wartość do znalezienia.
        seq: uporządkowana sekwencja, w której szukamy.

    Returns:
        bool: True gdy x znajduje się w seq, False w przeciwnym przypadku.

    Przykłady:
        >>> binary_search(1, [])
        False

        >>> binary_search(1, [1])
        True

        >>> LICZBY = [1, 2]
        >>> all(binary_search(liczba, LICZBY) for liczba in LICZBY)
        True

        >>> any(binary_search(liczba, LICZBY) for liczba in [0, 3])
        False

        >>> LICZBY = [5, 7, 11]
        >>> all(binary_search(liczba, LICZBY) for liczba in LICZBY)
        True

        >>> any(binary_search(liczba, LICZBY) for liczba in [1, 6, 10, 12])
        False

        >>> LITERY = "abcdefghijklmnopqrstuvwxyz"
        >>> all(binary_search(litera, LITERY) for litera in LITERY)
        True

        >>> any(binary_search(znak, LITERY) for znak in "123%&")
        False
    """
    if not seq:
        return False
    mid = len(seq) // 2
    if x == seq[mid]:
        return True
    elif x < seq[mid]:
        return binary_search(x, seq[:mid])
    else:
        return binary_search(x, seq[mid + 1:])
