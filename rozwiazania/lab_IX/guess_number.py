def guess_number(a, b):
    """Rekurencyjnie zgaduje liczbę z zakresu [a, b] metodą połowienia."""
    if a == b:
        print(f"Zapisałeś liczbę {a}.")
        return
    mid = (a + b) // 2
    ans = input(f"Czy Twoja liczba jest większa od {mid} (T/n)? ")
    if ans == 'n':
        guess_number(a, mid)
    else:
        guess_number(mid + 1, b)

if __name__ == "__main__":
    print("Pomyśl liczbę z zakresu [0, 1000].")
    guess_number(0, 1000)