class CaesarCipher:
    """Szyfr Cezara o zadanym przesunięciu.

    >>> cipher = CaesarCipher(3)
    >>> cipher("ala ma kota")
    'dod pd nrwd'
    >>> cipher.decrypt("dod pd nrwd")
    'ala ma kota'
    >>> cipher
    CaesarCipher(3)
    >>> rot13 = CaesarCipher(13)
    >>> rot13(rot13("hello world"))         # ROT13 jest swoją własną odwrotnością
    'hello world'
    >>> binary = CaesarCipher(1, alphabet="01")
    >>> binary("01010 11")
    '10101 00'
    """

    def __init__(self, shift, alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.shift = shift
        self.alphabet = alphabet

    def _shift_text(self, text, by):
        n = len(self.alphabet)
        wynik = []
        for znak in text:
            if znak in self.alphabet:
                i = self.alphabet.index(znak)
                wynik.append(self.alphabet[(i + by) % n])
            else:
                wynik.append(znak)
        return "".join(wynik)

    def __call__(self, text):
        return self._shift_text(text, self.shift)

    def decrypt(self, text):
        return self._shift_text(text, -self.shift)

    def __repr__(self):
        return f"CaesarCipher({self.shift})"
