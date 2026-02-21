def max_subseq(seq, pred):
    """Return the maximum subsequence subseq of seq such that pred(subseq) is True."""
    if not pred(seq[0:0]):
        return None
    n = len(seq)
    maxlen = 0
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            subseq = seq[i:j]
            if not pred(subseq):
                break
            j += 1
        
            
    

for n in range(5, 10):
    for i in range(n - 5 + 1):
        seq = i * [0] + 5 * [1] + (n - 5 - i) * [0]
        print(seq)
