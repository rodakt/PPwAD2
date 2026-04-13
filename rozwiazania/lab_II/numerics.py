def parse_number(tekst):
    # najpierw próbujemy int - int("5.0") rzuca ValueError, więc "5.0" tu nie przejdzie;
    # kolejność ma znaczenie: float ma ograniczony zakres i dla bardzo dużych liczb
    # całkowitych daje inf, podczas gdy Python int ma dowolną precyzję
    try:
        return int(tekst)
    except ValueError:
        pass
    try:
        f = float(tekst)
    except ValueError:
        raise ValueError(f"'{tekst}' nie jest liczbą")
    # float o wartości całkowitej (np. "3.0") zwracamy jako int
    if f.is_integer():
        return int(f)
    return f


def silnia(n):
    # walidacja typu - funkcja nie wie, kto ją wywoła
    if not isinstance(n, int):
        raise TypeError("argument musi być liczbą całkowitą")
    if n < 0:
        raise ValueError(f"wymagane n >= 0, otrzymano n={n}")
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


def symbol_newtona(n, k):
    # walidacja typów - funkcja nie wie, kto ją wywoła
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("argument musi być liczbą całkowitą")
    # walidacja dziedziny przed wywołaniem silnia
    if n < 0:
        raise ValueError(f"wymagane n >= 0, otrzymano n={n}")
    if k < 0 or k > n:
        raise ValueError(f"wymagane 0 <= k <= n, otrzymano n={n}, k={k}")
    return silnia(n) // (silnia(k) * silnia(n - k))


if __name__ == "__main__":
    tekst_n = input("n: ")
    tekst_k = input("k: ")
    try:
        n = parse_number(tekst_n)
        k = parse_number(tekst_k)
        wynik = symbol_newtona(n, k)
    except TypeError as e:
        # float z parse_number trafi tu - symbol_newtona sprawdza typ przed silnia
        print(f"Błąd: {e}.")
    except ValueError as e:
        # ValueError może pochodzić z parse_number lub symbol_newtona
        print(f"Błąd: {e}.")
    else:
        print(f"C({n}, {k}) = {wynik}")
