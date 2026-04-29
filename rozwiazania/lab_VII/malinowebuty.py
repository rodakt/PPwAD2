"""Szyfr malinowe buty jako domknięcie."""


def create_key(s):
    """Zwraca słownik par wymian znaków dla klucza s.

    Prawidłowy klucz to niepusty łańcuch znaków o parzystej długości,
    w którym wszystkie znaki są różne. W przeciwnym razie zgłasza ValueError.
    """
    if not s or len(s) % 2 != 0 or len(set(s)) != len(s):
        raise ValueError("nieprawidłowy klucz.")
    klucz = {}
    for i in range(0, len(s), 2):
        klucz[s[i]] = s[i + 1]
        klucz[s[i + 1]] = s[i]
    return klucz


def create_encryptor(s='malinowebuty'):
    """Zwraca funkcję encryptor(text) szyfrującą tekst kluczem s."""
    key = create_key(s)

    def encryptor(text):
        return ''.join(key.get(c, c) for c in text)

    return encryptor
