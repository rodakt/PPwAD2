def merge(A, p, q, r):
    if not (0 <= p <= q <= r <= len(A)):
        raise ValueError("Incorrect indices")
    L = A[p:q]
    R = A[q:r]
    i = j = 0
    for k in range(p, r):
        if i < len(L) and (j >= len(R) or L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergesort(A, p=0, r=None):
    if r is None:
        r = len(A)
    if p < r - 1:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q, r)
        merge(A, p, q, r)
