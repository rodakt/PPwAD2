"""Moduł zawiera funkcje realizujące podstawowe operacje arytmetyczne.

Funkcje:
    increment(x) - zwraca wartość x zwiększoną o 1
    decrement(x) - zwraca wartość x zmniejszoną o 1
    change_sign(x) - zwraca wartość x ze zmienionym znakiem
    add(x, y) - zwraca sumę x i y
    sub(x, y) - zwraca różnicę x i y
    mul(x, y) - zwraca iloczyn x i y
    int_div(x, y) - zwraca wynik dzielenia całkowitego x przez y

Funkcje add(), sub(), mul() i int_div() działają jedynie za pośrednictwem
funkcji increment(), decrement() i change_sign() (bezpośrednio lub pośrednio).
Nie korzystają z operatorów +, -, * i //.
"""


def increment(x):
    """Zwiększa wartość x o 1."""
    return x + 1


def decrement(x):
    """Zmniejsza wartość x o 1."""
    return x - 1


def change_sign(x):
    """Zmienia znak liczby x na przeciwny."""
    return -x


def add(x, y):
    # pętla po argumencie o mniejszej wartości bezwzględnej - kluczowe dla wydajności;
    # add(10**8, 1) wykona 1 iterację, nie 10**8
    if abs(x) < abs(y):
        x, y = y, x
    if y > 0:
        for _ in range(y):
            x = increment(x)
    elif y < 0:
        for _ in range(change_sign(y)):
            x = decrement(x)
    return x


def sub(x, y):
    return add(x, change_sign(y))


def mul(x, y):
    ax, ay = abs(x), abs(y)
    # pętla po mniejszym czynniku, dodajemy większy
    if ax <= ay:
        mały, duży = ax, ay
    else:
        mały, duży = ay, ax
    wynik = 0
    for _ in range(mały):
        wynik = add(wynik, duży)
    # korekta znaku: wynik ujemny gdy dokładnie jeden argument jest ujemny
    if (x < 0) != (y < 0):
        wynik = change_sign(wynik)
    return wynik


def int_div(x, y):
    if y == 0:
        raise ValueError("Dzielenie przez zero")
    # pracujemy na wartościach bezwzględnych, znak korygujemy na końcu
    ujemny = (x < 0) != (y < 0)
    ax, ay = abs(x), abs(y)
    wynik = 0
    while ax >= ay:
        ax = sub(ax, ay)
        wynik = increment(wynik)
    # semantyka podłogowa: jeśli wynik ujemny i jest reszta, zaokrąglamy w dół
    if ujemny and ax > 0:
        wynik = increment(wynik)
    if ujemny:
        wynik = change_sign(wynik)
    return wynik
