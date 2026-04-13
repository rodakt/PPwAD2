p = int(input("p = "))
q = int(input("q = "))

assert p > 0 and q > 0, "p i q muszą być większe od 0"

# Niezmiennik: jeśli rozwiązanie istnieje, leży w przedziale [a, b).
# Górne ograniczenie: x*p <= x^3+px = q, więc x <= q//p.
a, b = 0, q // p + 1

while a < b:
    x = (a + b) // 2
    lhs = x**3 + p*x
    if lhs == q:
        print(f"x = {x}")
        break
    elif lhs < q:
        a = x + 1   # x za małe, rozwiązanie w [x+1, b)
    else:
        b = x       # x za duże, rozwiązanie w [a, x)
else:
    # a == b: przedział pusty, brak rozwiązania
    print("Brak rozwiązania")
