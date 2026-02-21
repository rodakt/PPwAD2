class AverageSpeed:
    """Klasa do obliczania kroczącej prędkości średniej"""

    def __init__(self):
        self.distance = 0
        self.time = 0

    def add_section(self, distance, time):
        """Dodaje nowy odcinek trasy"""
        self.distance += distance
        self.time += time
        self.average_speed = self.distance / self.time


class MovingAverage:

    def __init__(self):
        self.total = 0
        self.count = 0

    def add_value(self, value):
        self.total += value
        self.count += 1
        return self.total / self.count
