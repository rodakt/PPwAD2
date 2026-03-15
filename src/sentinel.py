# src/sentinel.py
def min_strażnik(*wartości, strażnik=None):
    m = min(wartości)
    if strażnik is not None:
        return m if m >= strażnik else strażnik
    return m