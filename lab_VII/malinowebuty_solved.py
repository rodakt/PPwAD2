def create_key(s):
    if not s or len(s) != len(set(s)) or len(s) % 2 != 0:
        raise ValueError("nieprawidłowy klucz.")
    d = {}
    for i, c in enumerate(s):
        if i % 2 == 0:
            d[c] = s[i + 1]
        else:
            d[c] = s[i - 1]
    return d


def create_encryptor(s="malinowebuty"):
    key = create_key(s)

    def encryptor(text):
        return "".join(key.get(c, c) for c in text)

    return encryptor
