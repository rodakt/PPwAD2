import csv
import math


def create_turtle(x=0, y=0, azimuth=0, name=""):
    """Tworzy żółwia w położeniu (x, y) patrzącego w kierunku azimuth stopni od wschodu."""
    return {
        'position': [(x, y)],
        'azimuth': azimuth,
        'name': name,
    }


def forward(turtle, r):
    """Przesuwa żółwia o dystans r w kierunku, w którym patrzy."""
    x, y = turtle['position'][-1]
    rad = math.radians(turtle['azimuth'])
    turtle['position'].append((x + r * math.cos(rad), y + r * math.sin(rad)))


def right(turtle, a):
    """Obraca żółwia o kąt a w prawo."""
    turtle['azimuth'] -= a


def left(turtle, a):
    """Obraca żółwia o kąt a w lewo."""
    turtle['azimuth'] += a


def to_csv(*turtles, filename):
    """Zapisuje historię położeń żółwi do pliku CSV (kolumny: x, y, name)."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y', 'name'])
        for turtle in turtles:
            for x, y in turtle['position']:
                writer.writerow([x, y, turtle['name']])
