"""Moduł zawierający dekorator do mierzenia czasu wykonania funkcji."""

import time
import statistics
from functools import wraps

def timed(repeat=5, timer=None):
    """Dekorator mierzący statystyczny czas wykonania funkcji."""
    clock = timer if timer is not None else time.perf_counter
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            times = []
            result = None
            for _ in range(repeat):
                start = clock()
                result = f(*args, **kwargs)
                end = clock()
                times.append(end - start)

            m = statistics.mean(times)
            s = statistics.stdev(times)

            print(f"{f.__name__} (repeat={repeat}): mean={m:.4f} s, stdev={s:.4f} s")

            return result
        return wrapper
    return decorator
