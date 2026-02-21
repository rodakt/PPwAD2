"""Moduł zawierający funkcję symulującą losowanie z urny."""

import random


def draw_from_urn(number_of_draws=1, with_replacement=True, **balls):
    """Symulacja losowania z urny.

    Parametry:
        number_of_draws : int
            Liczba losowań.
        with_replacement : bool
            Jeśli True, to po każdym losowaniu kula jest zwracana do urny.
        **balls : int
            Słownik określający liczbę kul danego koloru w urnie.

    Zwraca:
        list
            Lista kolorów wylosowanych kul.
    """
    urn = []
    for ball, number in balls.items():
        urn.extend([ball] * number)
    if not with_replacement and number_of_draws > len(urn):
        raise ValueError("Liczba losowań bez zwracania przekracza liczbę kul w urnie.")
    bag = []
    for _ in range(number_of_draws):
        ball = random.choice(urn)
        bag.append(ball)
        if not with_replacement:
            urn.remove(ball)
    return bag
