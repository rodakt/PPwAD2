def is_arithmetic(seq):
    """Zwraca True, jeśli seq jest ciągiem arytmetycznym; w przeciwnym razie zwraca False.
    
    seq -- sekwencja liczb
    
    Przykłady:
    >>> is_arithmetic([])
    True
    >>> is_arithmetic([2])
    True
    >>> is_arithmetic([5, -1])
    True
    >>> is_arithmetic([1, 2, 3])
    True
    >>> is_arithmetic(range(100, -1000, -7))
    True
    >>> is_arithmetic((2, 5, 8, 10, 13))
    False
    >>> is_arithmetic([0.1, 0.2, 0.3])
    True
    """
    if len(seq) < 2:
        return True
    else:
        diff = seq[1] - seq[0]
        for i in range(2, len(seq)):
            if seq[i] - seq[i-1] != diff:
                return False
        return True
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)