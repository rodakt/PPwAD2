def rotate(seq, n):
    if not seq:
        return seq
    # Python: -4 % 10 == 6, więc ujemne n (lewo) sprowadza się do równoważnego
    # przesunięcia w prawo; nie trzeba rozróżniać kierunków
    n = n % len(seq)
    # wycinki zachowują typ: str->str, list->list, tuple->tuple
    return seq[-n:] + seq[:-n]


def rotate_left(seq, n):
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    return rotate(seq, -n)


def rotate_right(seq, n):
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    return rotate(seq, n)
