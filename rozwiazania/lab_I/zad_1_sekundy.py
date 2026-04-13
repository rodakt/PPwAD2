sekundy = int(input("Podaj liczbę sekund: "))

dni = sekundy // 86400
pozostalo = sekundy % 86400
godziny = pozostalo // 3600
pozostalo %= 3600
minuty = pozostalo // 60
sek = pozostalo % 60

print(f"{dni} d, {godziny} h, {minuty} min, {sek} s")
