# src/try_except_ZDE.py
try:
    x = int(input("Podaj liczbę: "))
    y = 1 / x
except ValueError:
    print("To nie jest liczba całkowita.")
except ZeroDivisionError:
    print("Nie dziel przez zero.")
else:
    print("Wynik dzielenia to", y)
finally:
    print("\nKoniec.")
