def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def rot13(s, use_ascii_only=False):
    if use_ascii_only and not is_ascii(s):
        raise ValueError("znaleziono znak spoza zakresu ASCII")
    wynik = []
    for c in s:
        if 'a' <= c <= 'z':
            # przesunięcie o 13 w obrębie małych liter, zawijanie modulo 26
            wynik.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            wynik.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
        else:
            # znaki spoza alfabetu łacińskiego (w tym polskie) - bez zmian
            wynik.append(c)
    return ''.join(wynik)


def rot47(s, use_ascii_only=False):
    if use_ascii_only and not is_ascii(s):
        raise ValueError("znaleziono znak spoza zakresu ASCII")
    wynik = []
    for c in s:
        if 33 <= ord(c) <= 126:
            # zakres [33, 126] ma 94 znaki; przesunięcie o 47 z zawijaniem modulo 94
            wynik.append(chr(33 + (ord(c) - 33 + 47) % 94))
        else:
            wynik.append(c)
    return ''.join(wynik)
