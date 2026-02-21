"""Program szyfruje plik tekstowy za pomocą szyfru podstawieniowego.

Obsługuje wyjątek:
- FileExistsError, gdy plik docelowy już istnieje
- FileNotFoundError, gdy plik wejściowy nie istnieje
"""

KEY = "malinowebuty"  # klucz szyfru


def encrypt(msg, key):
    """Funkcja szyfruje wiadomość msg za pomocą klucza key."""
    secret = ""
    for char in msg:
        if char in key:
            i = key.index(char)
            if i % 2 == 0:
                secret += key[i + 1]
            else:
                secret += key[i - 1]
        else:
            secret += char
    return secret


def main():
    """Funkcja główna programu.

    Wczytuje plik tekstowy, szyfruje go i zapisuje wynik w nowym pliku.
    """
    input_file = input("Plik do zaszyfrowania: ")
    try:
        with open(input_file, "rt") as f:
            public_msg = f.read()
    except FileNotFoundError:
        print(f"Brak pliku {input_file}")
        return

    output_file = input("Docelowy plik z szyfrem: ")
    try:
        with open(output_file, "xt") as f:
            f.write(encrypt(public_msg, key=KEY))
    except FileExistsError:
        # Plik wyjściowy istnieje. Czy chcesz go nadpisać? (t/n)
        print(f"Plik {output_file} już istnieje. Nadpisać? (t/n)")
        choice = input()
        if choice.lower() == "t":
            with open(output_file, "wt") as f:
                f.write(encrypt(public_msg, key=KEY))
        else:
            print("Operacja przerwana.")

if __name__ == "__main__":
    main()
