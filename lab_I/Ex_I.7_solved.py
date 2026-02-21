p = int(input("p = "))
q = int(input("q = "))

assert p > 0 and q > 0, "p i q muszą być większe od 0"

a, b = 0, int(q**(1/3)) + 1

while True:
    if b - a < 2: # przedział zawiera co najwyżej 1 liczbę
        if a**3 + p*a == q:
            print(f"x = {a}")
        elif b**3 + p*b == q:
            print(f"x = {b}")
        else:
            print("Brak rozwiązania")
        break
    x = (a + b) // 2 # środek przedziału
    lhs = x**3 + p*x # lewa strona równania
    if lhs == q: # znaleźliśmy rozwiązanie
        print(f"x = {x}")
        break
    elif lhs < q:
        a, b = x, b # x jest za małe
    else:
        a, b = a, x # x jest za duże
