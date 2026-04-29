import random


def draw_from_urn(number_of_draws=1, with_replacement=True, **balls):
    """Symuluje losowanie z urny zawierającej kule w różnych kolorach.

    number_of_draws - liczba losowan,
    with_replacement - czy kula wraca do urny po wylosowaniu,
    **balls - kolory kul i ich liczebnosci.

    Zwraca liste wylosowanych kolorow.
    """
    urna = []
    for kolor, liczba in balls.items():
        urna.extend(liczba * [kolor])
    if not with_replacement and number_of_draws > len(urna):
        raise ValueError("Liczba losowań bez zwracania przekracza liczbę kul w urnie.")
    wyniki = []
    for _ in range(number_of_draws):
        kula = random.choice(urna)
        wyniki.append(kula)
        if not with_replacement:
            urna.remove(kula)
    return wyniki
