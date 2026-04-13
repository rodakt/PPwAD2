ścieżka = input("Podaj ścieżkę do pliku: ")

try:
    with open(ścieżka, encoding='utf-8') as plik:
        wiersze = plik.readlines()
except FileNotFoundError:
    print(f"Brak pliku: {ścieżka}")
except OSError as e:
    print(f"Błąd odczytu pliku: {e}")
else:
    liczba_wierszy = len(wiersze)
    liczba_słów = sum(len(w.split()) for w in wiersze)
    liczba_znaków = sum(len(w) for w in wiersze)
    print(f"Wiersze: {liczba_wierszy}")
    print(f"Słowa:   {liczba_słów}")
    print(f"Znaki:   {liczba_znaków}")
