# src/file_size_v1.py
"""
Program oblicza rozmiar pliku w bajtach.

Sposób użycia:
python file_size_v1.py <nazwa_pliku>
"""
import sys


def file_size(file_name):
    """Funkcja zwraca rozmiar pliku w bajtach.

    Zwróci None, jeśli plik nie istnieje lub wystąpił inny błąd.
    """
    try:
        f = open(file_name, "rb")
        size = len(f.read())
    except FileNotFoundError:  # Plik nie istnieje.
        print(f"Plik {file_name} nie istnieje.")
    except OSError as e:  # Inny błąd systemowy.
        print(f"Wystąpił błąd systemowy: {e}")
    else:
        return size
    finally:
        try:  # Próba zamknięcia pliku, na pewno zostanie podjęta.
            f.close()
        except (
            UnboundLocalError
        ):  # Zmienna f nie istnieje, bo nie udało się otworzyć pliku.
            pass


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
