# src/try_except_AE.py
try:
    x = int(input("Podaj liczbę: "))
    y = 1 / x
except (
    ArithmeticError
):  # Obsłuży ZeroDivisionError, gdyż jest to podklasa ArithmeticError
    print("Błąd obliczeniowy.")
except ValueError:
    print("To nie jest liczba całkowita.")
else:
    print("Wynik dzielenia to", y)
finally:
    print("Koniec.")
