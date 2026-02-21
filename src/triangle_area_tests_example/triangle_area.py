"""Moduł zawierający funkcje do obliczania pola trójkąta"""

from math import sqrt


def is_triangle(a, b, c):
    """Sprawdza, czy z boków a, b, c można zbudować trójkąt."""
    return a + b >= c and b + c >= a and c + a >= b


def triangle_area(a, b, c):
    """Oblicza pole trójkąta o bokach a, b, c za pomocą wzoru Herona."""
    if not is_triangle(a, b, c):
        raise ValueError(f"Nie można zbudować trójkąta o bokach {a}, {b}, {c}")
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def main():
    print("Witaj w programie do obliczania pola trójkąta.")
    a = float(input("Podaj długość pierwszego boku: "))
    b = float(input("Podaj długość drugiego boku: "))
    c = float(input("Podaj długość trzeciego boku: "))
    try:
        area = triangle_area(a, b, c)
    except ValueError as e:
        print(e)
    else:
        print(f"Pole trójkąta wynosi {area}")


if __name__ == "__main__":
    main()
