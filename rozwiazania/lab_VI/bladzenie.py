import random

from logo_turtle import create_turtle, forward, right, to_csv

N = 1000
OBROTY = [0, 90, 180, 270]


def błądzenie(turtle, n):
    for _ in range(n):
        right(turtle, random.choice(OBROTY))
        forward(turtle, 1)


t1 = create_turtle(name="Bolek")
t2 = create_turtle(name="Lolek")
t3 = create_turtle(name="Tolek")

for t in [t1, t2, t3]:
    błądzenie(t, N)

to_csv(t1, t2, t3, filename="bladzenie.csv")
