"""Moduł zawierający dekoratory rejestrujące funkcje w słownikach."""

REGISTRY = {}

def register(f):
    """Dekorator bezparametrowy dodający funkcję do globalnego rejestru."""
    REGISTRY[f.__name__] = f
    return f

def register_in(dictionary):
    """Dekorator z parametrem dodający funkcję do podanego słownika."""
    def decorator(f):
        dictionary[f.__name__] = f
        return f
    return decorator
