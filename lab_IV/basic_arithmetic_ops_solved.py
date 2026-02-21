"""Moduł zawiera funkcje realizujące podstawowe operacje arytmetyczne

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
    """Zwiększa wartość x o 1"""
    return x + 1


def decrement(x):
    """Zmniejsza wartość x o 1"""
    return x - 1


def change_sign(x):
    """Zmienia znak liczby x na przeciwny"""
    return -x


def add(x, y):
    """Zwraca sumę x i y"""
    if y < x:
        x, y = y, x
    if change_sign(y) <= x <= y:
        if 0 <= x:
            for _ in range(x):
                y = increment(y)
        else:
            for _ in range(change_sign(x)):
                y = decrement(y)
        return y
    else:
        return change_sign(add(change_sign(x), change_sign(y)))


def sub(x, y):
    """Zwraca różnicę x i y"""
    return add(x, change_sign(y))


def mul(x, y):
    """Zwraca iloczyn x i y"""
    sign_of_result = -1 if (x < 0 and y > 0) or (x > 0 and y < 0) else 1
    x = change_sign(x) if x < 0 else x
    y = change_sign(y) if y < 0 else y
    result = 0
    if y < x:
        x, y = y, x
    for _ in range(x):
        result = add(result, y)
    return change_sign(result) if sign_of_result < 0 else result


def int_div(x, y):
    """Zwraca wynik dzielenia całkowitego x przez y"""
    if y == 0:
        raise ValueError("Dzielenie przez zero")
    sign_of_result = -1 if (x < 0 and y > 0) or (x > 0 and y < 0) else 1
    x = change_sign(x) if x < 0 else x
    y = change_sign(y) if y < 0 else y
    result = 0
    while x >= y:
        x = sub(x, y)
        result = increment(result)
    return decrement(change_sign(result)) if sign_of_result < 0 else result
