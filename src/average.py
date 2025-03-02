# src/average.py
def average(seq):
    """Funkcja zwraca średnią arytmetyczną elementów sekwencji."""
    if len(seq) == 0:
        raise ValueError("Sekwencja nie może być pusta.")
    return sum(seq) / len(seq)


seq = [1, 2, 3, 4, 5]
try:
    print(f"Średnia arytmetyczna: {average(seq)}")
except ValueError as e:
    print("Błąd:", e)
