# src/file_size_v2.py
"""
Program oblicza rozmiar pliku w bajtach.

Sposób użycia:
python file_size_v2.py <nazwa_pliku>
"""
import sys


def file_size(file_name):
    """Funkcja zwraca rozmiar pliku w bajtach.

    Zwróci None, jeśli plik nie istnieje lub wystąpił inny błąd.
    """
    try:
        with open(file_name, "rb") as f:
            size = len(f.read())
    except FileNotFoundError:  # Plik nie istnieje.
        print(f"Plik {file_name} nie istnieje.")
    except OSError as e:  # Inny błąd systemowy.
        print(f"Wystąpił błąd systemowy: {e}")
    else:
        return size


def main():
    if len(sys.argv) != 2:  # Skrypt przyjmuje dokładnie jeden argument.
        print("Sposób użycia: python file_size.py <nazwa_pliku>")
    else:
        file_name = sys.argv[1]
        size = file_size(file_name)
        if size is not None:  # Jeśli brak pliku lub błąd systemowy, to size == None.
            print(f"Rozmiar pliku {file_name} to {size} bajtów.")
        else:
            print("Nie udało się obliczyć rozmiaru pliku.")


if __name__ == "__main__":
    main()
