import random


def tura(max_rzutow):
    suma = 0
    for _ in range(max_rzutow):
        k1 = random.randint(1, 6)
        k2 = random.randint(1, 6)
        if k1 == 1 or k2 == 1:
            return 0
        suma += k1 + k2
    return suma


def alicja(konto_alicji, konto_piotra):
    if konto_piotra >= 100:
        print(f"Piotr wygrał! (Piotr: {konto_piotra}, Alicja: {konto_alicji})")
        return
    konto_alicji += tura(2)
    piotr(konto_piotra, konto_alicji)


def piotr(konto_piotra, konto_alicji):
    if konto_alicji >= 100:
        print(f"Alicja wygrała! (Alicja: {konto_alicji}, Piotr: {konto_piotra})")
        return
    konto_piotra += tura(3)
    alicja(konto_alicji, konto_piotra)
