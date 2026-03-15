# src/nwd.py
def nwd(a, b):
    """
    Zwraca największy wspólny dzielnik dwóch liczb.

    Argumenty:
        a, b (int): liczby całkowite
    Zwraca:
        int: nwd(a, b)
    """
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a