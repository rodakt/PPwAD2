# src/traceback_example.py
def f():
    g()


def g():
    h()


def h():
    raise Exception("Błąd")


f()
