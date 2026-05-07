def fib_tail(n, a=0, b=1):
    """Zwraca F_n, n-ty wyraz ciągu Fibonacciego, zaimplementowana
    rekurencją ogonową z dwoma akumulatorami a, b."""
    if n == 0:
        return a
    return fib_tail(n - 1, b, a + b)
