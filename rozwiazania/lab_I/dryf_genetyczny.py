# Symulacja dryfu genetycznego
# Autor: Tomasz Rodak
# Data: 2023-05-27
"""
Moduł zawiera funkcje do symulacji dryfu genetycznego w populacji diploidalnej.
"""

import random
import math
import csv

GENY = [["A", "a"], ["B", "b"], ["C", "c"], ["D", "d"]]

def czas_fiksacji_lub_utraty(N, p=1/2):
    """
    Oblicza przewidywany czas do fiksacji lub utraty allelu.
    Źródło: https://en.wikipedia.org/wiki/Genetic_drift#Time_to_fixation_or_loss

    :param N: liczba całkowita reprezentująca wielkość populacji
    :param p: liczba zmiennoprzecinkowa reprezentująca prawdopodobieństwo fiksacji lub utraty (domyślnie: 1/2)
    :return: liczba zmiennoprzecinkowa reprezentująca przewidywany czas do fiksacji lub utraty allelu.
    """
    return -4 * N * (1 - p) * math.log(1 - p) / p

def losuj_bez_zwracania(lista, n):
    """Losuje n elementów z listy bez zwracania."""
    assert len(lista) >= n
    indeksy = random.sample(range(len(lista)), n)
    losy = [lista[i] for i in indeksy]
    for i in sorted(indeksy, reverse=True):
        del lista[i]
    return losy


def realizacje_genów(geny):
    """Lista możliwych wersji genów."""
    wersje_genów = []
    for A, a in geny:
        g = [A + A, A + a, a + A, a + a]
        wersje_genów.append(g)
    return wersje_genów


def nowa_populacja(N, geny):
    """Losowa populacja osobników."""
    wersje_genów = realizacje_genów(geny)
    populacja = []
    for i in range(N):
        osobnik = []
        for g in wersje_genów:
            osobnik.append(random.choice(g))
        populacja.append(osobnik)
    return populacja


def losuj_parę(populacja):
    """Losuje parę osobników z populacji."""
    assert len(populacja) >= 2
    return losuj_bez_zwracania(populacja, 2)


def rozmnóż_parę(para):
    """Tworzy potomka z pary rodziców."""
    rodzic1, rodzic2 = para
    assert len(rodzic1) == len(rodzic2)
    potomek = []
    for i in range(len(rodzic1)):
        potomek.append(random.choice(rodzic1[i]) + random.choice(rodzic2[i]))
    return potomek


def populacja_potomna(populacja, rozrodczość=2):
    """Populacja potomna powstała z populacji rodzicielskiej."""
    populacja_kopiowana = populacja.copy()
    potomna = []
    while len(populacja_kopiowana) >= 2:
        para = losuj_parę(populacja_kopiowana)
        for _ in range(rozrodczość):
            potomek = rozmnóż_parę(para)
            potomna.append(potomek)
    return potomna


def statystyka(populacja, geny=GENY):
    """Zwraca częstość występowania genów w populacji."""
    dwa_N = 2 * len(populacja)
    allele = "".join("".join(g) for g in geny)
    allele_w_populacji = "".join("".join(g) for g in populacja)
    return dict(zip(allele, [allele_w_populacji.count(a) / dwa_N for a in allele]))


def dryf_genetyczny(liczba_osobników=100, liczba_pokoleń=1000):
    """Symulacja dryfu genetycznego."""
    populacja = nowa_populacja(liczba_osobników, GENY)
    wyniki = [statystyka(populacja)]
    for _ in range(liczba_pokoleń):
        populacja = populacja_potomna(populacja)
        wyniki.append(statystyka(populacja))
    return wyniki


def wyświetl_wyniki(wyniki, krok=10):
    """Wyświetla wyniki symulacji."""
    for i, w in enumerate(wyniki):
        if krok and i % krok == 0:
            print(f"{i:4d}", end=" ")
            print(w)

def zapisz_do_csv(wyniki, nazwa_pliku):
    """Zapisuje wyniki symulacji do pliku CSV."""
    with open(nazwa_pliku, "wt", encoding="utf8", newline="") as f:
        zapisywacz = csv.DictWriter(f, fieldnames=wyniki[0].keys())
        zapisywacz.writeheader()
        zapisywacz.writerows(wyniki)

if __name__ == "__main__":
    # liczba osobników
    N_OSOBNIKÓW = 500
    # liczba pokoleń
    L_POKOLEŃ = 1400
    wyniki_symulacji = dryf_genetyczny(liczba_osobników=N_OSOBNIKÓW, liczba_pokoleń=L_POKOLEŃ)
    wyświetl_wyniki(wyniki_symulacji, krok=100)
    print(f"Przewidywany czas do utrwalenia: {czas_fiksacji_lub_utraty(N_OSOBNIKÓW, 1/2)}")
    zapisz_do_csv(wyniki_symulacji, "wyniki.csv")
