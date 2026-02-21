from fractions import Fraction as F
from logo_turtle import create_turtle, left, right, forward, to_csv


def polygon(turtle, a, r):
    if not isinstance(a, int) and not isinstance(a, F):
        raise TypeError("kąt musi być liczbą całkowitą lub wymierną")
    if a % 360 == 0:
        raise ValueError("kąt musi być liczbą wymierną nie będącą wielokrotnością 360")
    total_angle, counter = 0, 0
    while True:
        forward(turtle, r)
        right(turtle, a)
        counter += 1
        total_angle += a
        if total_angle % 360 == 0:
            return counter


def regular_polygon(turtle, n, r):
    a = F(360, n)
    polygon(turtle, a, r)


tolek = create_turtle(name="Tolek")
franklin = create_turtle(name="Franklin")
polygon(tolek, 135, 1)
regular_polygon(franklin, 5, 1)
to_csv(franklin, filename="/tmp/polygon.csv")

t = create_turtle()
polygon(t, 90, 1)
print(t["position"])
