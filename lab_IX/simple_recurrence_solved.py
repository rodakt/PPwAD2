"""Przykłady prostych rekurencji."""

def maximum_rec(seq):
    """Znajduje największy element w sekwencji.
    
    Implementacja rekurencyjna rozwijająca proces rekurencyjny.
    """
    if not seq:
        raise ValueError('sekwencja nie może być pusta')
    if len(seq) == 1:
        return seq[0]
    else:
        max_val = maximum_rec(seq[1:])
        return max_val if max_val > seq[0] else seq[0]

def maximum_tail(seq, max_val=None):
    """Znajduje największy element w sekwencji.
    
    Implementacja rekurencyjna z akumulatorem, proces iteracyjny.
    """
    if not seq:
        raise ValueError('sekwencja nie może być pusta')
    if max_val is None:
        max_val = seq[0]
    if len(seq) == 1:
        return max_val if max_val > seq[0] else seq[0]
    else:
        return maximum_tail(seq[1:], max_val if max_val > seq[0] else seq[0])


def fib_tail(n, a=0, b=1):
    """Zwraca n-ty element ciągu Fibonacciego.
    
    Implementacja rekurencyjna z akumulatorem, proces iteracyjny.
    """
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fib_tail(n-1, b, a+b)

