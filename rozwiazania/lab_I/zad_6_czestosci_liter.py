def f_count(text):
    wynik = {}
    for znak in text.lower():
        if znak.isalpha():
            wynik[znak] = wynik.get(znak, 0) + 1
    return wynik


tekst = input("Podaj tekst: ")
czestosci = f_count(tekst)
for litera, liczba in sorted(czestosci.items()):
    print(f"{litera}: {liczba}")
