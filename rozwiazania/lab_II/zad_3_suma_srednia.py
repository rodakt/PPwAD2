for próba in range(1, 4):
    tekst = input(f"Liczby (próba {próba}/3): ")
    try:
        liczby = [int(x) for x in tekst.split()]
    except ValueError:
        print("Błąd: nieprawidłowe dane.")
    else:
        # else wykonuje się tylko gdy nie wystąpił wyjątek
        suma = sum(liczby)
        if liczby:
            print(f"Suma: {suma}, Średnia: {suma / len(liczby)}")
        else:
            # split() pustego łańcucha zwraca [], średnia jest niezdefiniowana
            print(f"Suma: {suma}, Średnia: niezdefiniowana")
        break
else:
    # else pętli for wykonuje się gdy pętla zakończyła się bez break
    print("Przekroczono liczbę prób.")
