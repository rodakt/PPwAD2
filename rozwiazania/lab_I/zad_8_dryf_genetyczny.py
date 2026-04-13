import random
import math


def nowa_populacja(n):
    """Losowa populacja n osobników diploidalnych z allelami A i a."""
    allele = ["A", "a"]
    return [random.choice(allele) + random.choice(allele) for _ in range(n)]


def rozmnóż_parę(rodzic1, rodzic2):
    """Tworzy potomka — losuje po jednym allelu od każdego rodzica."""
    return random.choice(rodzic1) + random.choice(rodzic2)


def populacja_potomna(populacja):
    """Nowe pokolenie: losowe pary rodziców, każda para daje 2 potomków."""
    pula = populacja.copy()
    random.shuffle(pula)
    potomna = []
    for i in range(0, len(pula) - 1, 2):
        for _ in range(2):
            potomna.append(rozmnóż_parę(pula[i], pula[i + 1]))
    return potomna


def częstość_A(populacja):
    """Częstość allelu A w populacji."""
    wszystkie_allele = "".join(populacja)
    return wszystkie_allele.count("A") / len(wszystkie_allele)


if __name__ == "__main__":
    N = 100
    L_POKOLEŃ = 1000

    populacja = nowa_populacja(N)
    p0 = częstość_A(populacja)
    print(f"Pokolenie    0: częstość A = {p0:.3f}")

    for i in range(1, L_POKOLEŃ + 1):
        populacja = populacja_potomna(populacja)
        if i % 100 == 0:
            print(f"Pokolenie {i:4d}: częstość A = {częstość_A(populacja):.3f}")

    # Przewidywany czas do utrwalenia allelu A (warunkowy na utrwalenie):
    # T = -4N(1-p)ln(1-p)/p  (źródło: en.wikipedia.org/wiki/Genetic_drift)
    t_utrwalenia = -4 * N * (1 - p0) * math.log(1 - p0) / p0
    print(f"\nPrzewidywany czas do utrwalenia (p0 = {p0:.3f}): {t_utrwalenia:.1f} pokoleń")
