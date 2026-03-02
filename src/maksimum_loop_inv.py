# src/maksimum_loop_inv.py
def maksimum_inv(seq):
    """Funkcja zwraca maksimum z sekwencji."""
    if len(seq) == 0:
        raise ValueError("Sekwencja nie może być pusta.")
    
    maks = seq[0]
    
    # Przed rozpoczęciem pętli maks jest równe maksimum z pierwszego elementu sekwencji.
    assert maks == max(seq[:1]), "Niezmiennik pętli fałszywy przed rozpoczęciem pętli."
    
    for i, x in enumerate(seq[1:], 1):
        if x > maks:
            maks = x
        # W i-tej iteracji pętli maks jest równe maksimum z seq[:i+1].
        assert maks == max(seq[:i+1]), f"Niezmiennik pętli fałszywy w {i}-tej iteracji pętli."
    
    # Po zakończeniu pętli maks jest równe maksimum z całej sekwencji.
    assert maks == max(seq), "Niezmiennik pętli fałszywy po zakończeniu pętli."
    
    return maks