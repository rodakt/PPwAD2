"""Moduł zawierający dekoratory do sprawdzania kontraktów (warunków wstępnych i końcowych)."""

from functools import wraps

def pre_test(pred):
    """Dekorator sprawdzający warunek przed wywołaniem funkcji."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            pred(*args, **kwargs)
            return f(*args, **kwargs)
        return wrapper
    return decorator

def post_test(pred):
    """Dekorator sprawdzający warunek po wywołaniu funkcji na jej wyniku."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            pred(result)
            return result
        return wrapper
    return decorator
