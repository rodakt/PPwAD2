"""Moduł zawiera funkcję count_change() zwracającą liczbę możliwych kombinacji monet, 
którymi można wydać podaną kwotę.
"""

def count_change(amount, coins):
    """Zwraca liczbę możliwych kombinacji monet wydających podaną kwotę."""
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    else:
        return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)