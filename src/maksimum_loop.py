# src/maksimum_loop.py
def maksimum(seq):
    """Funkcja zwraca maksimum z sekwencji."""
    if len(seq) == 0:
        raise ValueError("Sekwencja nie może być pusta.")
    
    maks = seq[0]
    
    for x in seq[1:]:
        if x > maks:
            maks = x
    
    return maks