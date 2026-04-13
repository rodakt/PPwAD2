# b'...' to literał bajtowy - ciąg bajtów (typ bytes), nie znaków (str)
# \x89, \r, \n, \x1a to bajty zapisane szesnastkowo lub jako znaki specjalne
PNG_SYGNATURA = b'\x89PNG\r\n\x1a\n'  # 8 bajtów

ścieżka = input("Podaj ścieżkę do pliku: ")

try:
    # tryb 'rb' - odczyt binarny; plik.read() zwraca obiekt bytes, nie str
    with open(ścieżka, 'rb') as plik:
        zawartość = plik.read()
except FileNotFoundError:
    print(f"Brak pliku: {ścieżka}")
except OSError as e:
    print(f"Błąd odczytu pliku: {e}")
else:
    # bytes obsługuje indeksowanie i wycinki tak jak lista -
    # zawartość[:16] to pierwsze 16 bajtów jako nowy obiekt bytes
    pierwsze_16 = zawartość[:16]
    # iteracja po bytes daje kolejne bajty jako liczby całkowite 0–255
    # f'{b:02x}' formatuje liczbę jako dwucyfrową liczbę szesnastkową
    hex_zapis = ' '.join(f'{b:02x}' for b in pierwsze_16)
    # porównanie bytes == bytes sprawdza czy łańcuchy bajtów są identyczne
    jest_png = zawartość[:8] == PNG_SYGNATURA
    print(f"Rozmiar: {len(zawartość)} bajtów")
    print(f"Pierwsze 16 bajtów: {hex_zapis}")
    print(f"Sygnatura PNG: {'TAK' if jest_png else 'NIE'}")
