def is_ascii(s):
    """Zwraca True, jeśli s jest ciągiem znaków ASCII"""
    return all(ord(c) < 128 for c in s)


def rot13(s, use_ascii_only=False):
    """Szyfruje/dekoduje s szyfrem ROT13

    Jeśli use_ascii_only == True to s musi być ciągiem znaków ASCII.
    W przeciwnym razie zostanie zgłoszony wyjątek ValueError.
    """
    if use_ascii_only and not is_ascii(s):
        raise ValueError("znaleziono znak spoza zakresu ASCII")
    encrypted = []
    for c in s:
        if "a" <= c <= "z":
            c = chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
        elif "A" <= c <= "Z":
            c = chr((ord(c) - ord("A") + 13) % 26 + ord("A"))
        encrypted.append(c)
    return "".join(encrypted)


def rot47(s, use_ascii_only=False):
    """Szyfruje/dekoduje s szyfrem ROT47

    Jeśli use_ascii_only == True to s musi być ciągiem znaków ASCII.
    W przeciwnym razie zostanie zgłoszony wyjątek ValueError.
    """
    if use_ascii_only and not is_ascii(s):
        raise ValueError("znaleziono znak spoza zakresu ASCII")
    encrypted = []
    for c in s:
        if "!" <= c <= "~":
            c = chr((ord(c) - ord("!") + 47) % 94 + ord("!"))
        encrypted.append(c)
    return "".join(encrypted)
