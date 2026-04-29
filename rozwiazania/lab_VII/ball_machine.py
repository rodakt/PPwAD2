"""Automat losujący kule z urny."""

import random


def random_ball_machine(return_balls=True, **balls):
    """Zwraca bezparametrową funkcję machine() symulującą losowanie kul z urny.

    Parametry:
        return_balls - True (domyślnie) oznacza losowanie ze zwracaniem,
                       False oznacza losowanie bez zwracania.
        **balls      - argumenty postaci color=quantity, gdzie color to kolor kuli,
                       a quantity to liczba całkowita nieujemna określająca liczbę kul.

    Zwracana funkcja machine() przy każdym wywołaniu losuje kulę z urny i zwraca jej kolor.
    Jeśli urna jest pusta, machine() zgłasza wyjątek LookupError z komunikatem 'urna jest pusta.'
    """
    urna = [kolor for kolor, liczba in balls.items() for _ in range(liczba)]

    def machine():
        if not urna:
            raise LookupError("urna jest pusta.")
        kula = random.choice(urna)
        if not return_balls:
            urna.remove(kula)
        return kula

    return machine
