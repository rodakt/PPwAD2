import random


class RandomBallMachine:
    """Symuluje losowanie kul z urny.

    >>> machine = RandomBallMachine(red=3, blue=2)
    >>> len(machine)
    5
    >>> isinstance(machine(), str)          # losowanie ze zwracaniem
    True
    >>> len(machine)                        # skład bez zmian
    5
    >>> wyniki = [machine() for _ in range(1000)]
    >>> wyniki.count('red') > wyniki.count('blue')   # 3:2, prawie pewne
    True
    >>> machine = RandomBallMachine(red=2, blue=3)
    >>> wyniki = [machine() for _ in range(1000)]
    >>> wyniki.count('blue') > wyniki.count('red')   # odwrócone proporcje
    True
    >>> machine = RandomBallMachine(return_balls=False, red=2, blue=1)
    >>> sorted(machine() for _ in range(3))
    ['blue', 'red', 'red']
    >>> len(machine)
    0
    >>> machine()
    Traceback (most recent call last):
        ...
    LookupError: urna jest pusta.
    """

    def __init__(self, return_balls=True, **balls):
        self.balls = dict(balls)
        self.return_balls = return_balls

    def __call__(self):
        urn = []
        for kolor, liczba in self.balls.items():
            urn.extend([kolor] * liczba)
        if not urn:
            raise LookupError("urna jest pusta.")
        wynik = random.choice(urn)
        if not self.return_balls:
            self.balls[wynik] -= 1
        return wynik

    def __len__(self):
        return sum(self.balls.values())
