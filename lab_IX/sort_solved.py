"""Funkcję sortujące."""

# qsort(A):
#     zwróć A jeśli długość A jest < 1

#     pivot <-- ostatni element A
#     X <-- tablica tych elementów z A, które są < pivot
#     Y <-- tablica tych elementów z A, które są == pivot
#     Z <-- tablica tych elementów z A, które są > pivot
#     zwróć konkatenację qsort(X), Y, qsort(Z)


def qsort(seq):
    """Sortuje niemalejąco sekwencję za pomocą quicksort.

    Parametry:
    seq -- sekwencja do posortowania
    Zwraca:
    posortowaną sekwencję seq w postaci listy
    """
    if len(seq) < 1:
        return list(seq)

    pivot = seq[-1]
    X = [x for x in seq if x < pivot]
    Y = [x for x in seq if x == pivot]
    Z = [x for x in seq if x > pivot]
    return qsort(X) + Y + qsort(Z)


def merge(A, p, q, r):
    """Łączy dwie posortowane części listy A.

    Funkcja wymagana przez algorytm sortowania przez scalanie.
    Zakładamy, że A[p:q] oraz A[q:r] są już posortowane.
    """
    assert 0 <= p <= q <= r <= len(A), "Niepoprawne indeksy w merge"
    L, R = A[p:q], A[q:r]  # skopiuj podlisty
    # dodaj wartownika na końcu każdej z nich
    L.append(None)
    R.append(None)
    i = j = 0  # indeksy do poruszania się po L i R
    for k in range(p, r):
        if L[i] is None:
            A[k] = R[j]
            j += 1
        elif R[j] is None:
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergesort(A, p=0, r=None):
    """Sortuje listę A rosnąco za pomocą sortowania przez scalanie.

    Parametry:
    A -- lista do posortowania
    p -- indeks początkowy (domyślnie 0)
    r -- indeks końcowy (domyślnie długość A)
    """
    if r is None:
        r = len(A)
    if p < r - 1:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q, r)
        merge(A, p, q, r)
