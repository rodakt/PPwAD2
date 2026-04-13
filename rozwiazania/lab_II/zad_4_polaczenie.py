import time
import random


def connect(addr):
    print(f"Łączenie z {addr}...")
    t = random.random()
    try:
        time.sleep(t)
        if t > 0.6:
            raise RuntimeError("Przekroczono limit czasu")
        print(f"Połączono z {addr}.")
    finally:
        # finally wykonuje się zawsze — nawet gdy wyjątek nie jest tu obsługiwany
        # dlatego "Zamknięto połączenie" pojawi się PRZED komunikatem o błędzie
        print(f"Zamknięto połączenie z {addr}.")


for i in range(10):
    addr = f"192.168.0.{i}"
    try:
        connect(addr)
    except RuntimeError as e:
        print(f"Błąd: {e}")
    print("-" * 30)
