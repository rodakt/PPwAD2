"""Moduł implementujący wzorzec DSU (Decorate-Sort-Undecorate) przez dekoratory."""

from functools import wraps

def key_minmax(key=None):
    """Dekorator dla funkcji min/max implementujący wzorzec DSU."""
    def decorator(f):
        if key is None:
            return f
        
        @wraps(f)
        def wrapper(seq):
            # Decorate
            decorated = [(key(x), i, x) for i, x in enumerate(seq)]
            # Call
            result = f(decorated)
            # Undecorate
            return result[-1]
        return wrapper
    return decorator

def key_sort(key=None):
    """Dekorator dla funkcji sortujących implementujący wzorzec DSU."""
    def decorator(f):
        if key is None:
            return f
        
        @wraps(f)
        def wrapper(seq):
            # Decorate
            decorated = [(key(x), i, x) for i, x in enumerate(seq)]
            # Call
            result = f(decorated)
            # Undecorate
            return [x[-1] for x in result]
        return wrapper
    return decorator
