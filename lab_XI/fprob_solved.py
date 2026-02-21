import random

class RandomBallMachine:
    """Klasa reprezentująca losowanie z urny."""
    
    def __init__(self, return_balls=True, **balls):
        """Inicjalizacja klasy Fprob.
        
        Parametry:
        - return_balls: bool - czy zwracać kule, domyślnie True,
        - **balls: dict - kule w urnie.
        """
        self.return_balls = return_balls
        self.balls = balls
        self.urn = []
        for k, v in self.balls.items():
            self.urn.extend([k] * v)
    
    def __call__(self):
        """Losowanie z urny."""
        if not self.urn:
            raise LookupError("urna jest pusta.")
        ball = random.choice(self.urn)
        if not self.return_balls:
            self.urn.remove(ball)
        return ball