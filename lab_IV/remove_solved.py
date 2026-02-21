def remove_all(seq, value):
    """Removes all occurrences of value from seq.
    
    Raises ValueError if value is not present.
    
    Args:
        seq: a list or tuple
        value: an object
    Returns:
        new seq with all occurrences of value removed
    
    Example:
    >>> remove_all([1, 3, 2, 3, 4], 3)
    [1, 2, 4]
    >>> remove_all("hello", "l")
    'heo'
    >>> remove_all((2, 2, 2), 2)
    ()
    >>> remove_all((1, 2, 3), 4)
    Traceback (most recent call last):
        ...
    ValueError: 4 not in seq
    >>> remove_all(1_000_000*(1,), 1) # test wydajnościowy
    ()
    """
    if value not in seq:
        raise ValueError(f"{value} not in seq")
    
    idx = [i for i, x in enumerate(seq) if x == value]
    new_seq = seq[:idx[0]]
    i = idx[0] + 1

    for j in idx[1:]:
        new_seq += seq[i:j]
        i = j + 1

    new_seq += seq[i:]
    return new_seq
    
def remove_all_in_place(seq, value):
    """Removes all occurrences of value from seq.
    
    Raises ValueError if value is not present.
    
    Args:
        seq: a list
        value: an object
    Returns:
        None
    
    Example:
    >>> seq = [1, 3, 2, 3, 4]
    >>> remove_all_in_place(seq, 3)
    >>> seq
    [1, 2, 4]
    >>> seq = list("hello")
    >>> remove_all_in_place(seq, "l")
    >>> seq
    ['h', 'e', 'o']
    >>> seq = [2, 2, 2]
    >>> remove_all_in_place(seq, 2)
    >>> seq
    []
    >>> seq = bytearray(b"hello")
    >>> remove_all_in_place(seq, 108)
    >>> seq
    bytearray(b'heo')
    >>> seq = [1, 2, 3]
    >>> remove_all_in_place(seq, 4)
    Traceback (most recent call last):
        ...
    ValueError: 4 not in seq
    >>> seq = 1_000_000*[1] # test wydajnościowy
    >>> remove_all_in_place(seq, 1)
    >>> seq
    []
    """
    if value not in seq:
        raise ValueError(f"{value} not in seq")

    idx = [i for i, x in enumerate(seq) if x == value]

    for i in idx[::-1]:
        del seq[i]
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
