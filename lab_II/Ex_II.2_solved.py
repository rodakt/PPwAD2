"""Program wczytuje w jednej linii ciąg liczb całkowitych
rozdzielonych białymi znakami, następnie oblicza ich sumę
i średnią arytmetyczną. 

Obsługuje wyjątek:
- ValueError, gdy nie można przekształcić wartości wiersza na typ int
"""


def input_integers_from_string(msg):
    """Funkcja pobiera od użytkownika ciąg liczb całkowitych"""
    numbers = input(msg).split()
    try:
        numbers = [int(number) for number in numbers]
    except ValueError:
        raise ValueError("Nie można przekształcić wartości wiersza na typ int")
    return numbers


def main():
    """Funkcja główna programu."""
    while True:
        try:
            numbers = input_integers_from_string(
                "\nLiczby (wartości rozdziel białymi znakami): "
            )
            break
        except ValueError as e:
            print(e)
            print("Spróbuj ponownie.")
    total = sum(numbers)
    print(f"Suma: {total}")
    if numbers:
        print(f"Średnia: {total / len(numbers)}")
    else:
        print("Ciąg pusty, brak średniej.")


if __name__ == "__main__":
    main()
