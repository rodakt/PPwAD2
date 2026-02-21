# src/try_except_even_odd.py
"""
Program testuje, czy podana liczba całkowita jest parzysta czy nieparzysta.
Wymusza na użytkowniku podanie liczby całkowitej.
"""


while True:
    try:  # blok, w którym może powstać wyjątek; staramy się, aby był jak najkrótszy
        x = int(input("Podaj liczbę: "))
        break  # Jeśli udało się wczytać liczbę, to przerywamy pętlę.
    except ValueError:
        print("To nie jest liczba całkowita.")
        print("Spróbuj jeszcze raz.")

if x % 2 == 0:
    print(f"Liczba {x} jest parzysta.")
else:
    print(f"Liczba {x} jest nieparzysta.")
