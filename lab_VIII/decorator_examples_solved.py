"""Przykłady dekoratorów."""

from functools import wraps

REGISTRY = {}


def register(func):
    """Dekorator rejestrujący funkcję w słowniku REGISTRY."""
    REGISTRY[func.__name__] = func
    return func


def register_in(dictionary):
    """Dekorator rejestrujący funkcję w słowniku dictionary."""

    def wrapper(func):
        dictionary[func.__name__] = func
        return func

    return wrapper


def pre_test(pred):
    """Dekorator sprawdzający warunek pred na argumentach funkcji przed jej wywołaniem."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pred(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def post_test(pred):
    """Dekorator sprawdzający warunek pred na wartości zwracanej przez funkcję."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            pred(result)
            return result

        return wrapper

    return decorator
