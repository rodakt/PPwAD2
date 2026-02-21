"""Program pobiera od użytkownika dwie liczby całkowite a i b, 
następnie dzieli a przez b i wyświetla wynik.

Obsługuje wyjątki:
- ValueError, gdy a lub b nie są liczbami całkowitymi
- ZeroDivisionError, gdy b == 0
"""


def input_int(msg):
    """Funkcja pobiera od użytkownika liczbę całkowitą.

    msg - komunikat wyświetlany użytkownikowi
    """
    a = input(msg)
    try:
        a = int(a)
    except ValueError:
        raise ValueError(f"{a} nie jest liczbą całkowitą")
    return a


def main():
    """Funkcja główna programu."""
    try:
        a = input_int("a = ")
        b = input_int("b = ")
    except ValueError as e:
        print(e)
        return
    try:
        wynik = a / b
    except ZeroDivisionError:
        print("Próbujesz dzielić przez 0")
        return
    print(f"{a} / {b} == {wynik}")


if __name__ == "__main__":
    main()
