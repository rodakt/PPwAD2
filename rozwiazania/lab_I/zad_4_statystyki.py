def statystyki(dane):
    minimum = dane[0]
    maksimum = dane[0]
    suma = 0
    for x in dane:
        if x < minimum:
            minimum = x
        if x > maksimum:
            maksimum = x
        suma += x
    return minimum, maksimum, suma / len(dane)


dane = []
while True:
    wpis = input("Podaj liczbę (Enter aby zakończyć): ")
    if wpis == "":
        break
    dane.append(float(wpis))

minimum, maksimum, srednia = statystyki(dane)
print(f"Minimum: {minimum}, Maksimum: {maksimum}, Średnia: {srednia}")
