"""Funkcje do rotacji sekwencji

Funkcje:
rotate(seq, n) -- Rotacja sekwencji w lewo lub w prawo
rotate_right(seq, n) -- Rotacja sekwencji w prawo o n miejsc
rotate_left(seq, n) -- Rotacja sekwencji w lewo o n miejsc
"""


def rotate(seq, n):
    """Zwraca sekwencję seq przesuniętą cyklicznie o n miejsc w lewo lub w prawo"""
    if not seq:
        return seq
    N = len(seq)  # Wiem, że teraz N > 0
    if n >= 0:
        n = n % N  # n należy do zakresu 0, 1, ..., N - 1
        return seq[N - n :] + seq[: N - n]
    else:
        return rotate(seq, n % N)


def rotate_left(seq, n):
    """Zwraca sekwencję seq przesuniętą cyklicznie o n miejsc w lewo"""
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    return rotate(seq, -n)


def rotate_right(seq, n):
    """Zwraca sekwencję seq przesuniętą cyklicznie o n miejsc w prawo"""
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    return rotate(seq, n)
