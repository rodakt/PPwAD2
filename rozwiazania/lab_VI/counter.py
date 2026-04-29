def create_counter(start=0):
    """Tworzy nowy licznik z wartością początkową start."""
    return {'count': start}


def increment(counter):
    """Zwiększa licznik counter o 1."""
    counter['count'] += 1


def reset(counter):
    """Zeruje licznik counter."""
    counter['count'] = 0


def get_count(counter):
    """Zwraca aktualną wartość licznika counter."""
    return counter['count']


if __name__ == '__main__':
    c1 = create_counter()
    c2 = create_counter(10)
    increment(c1)
    increment(c1)
    increment(c2)
    print(get_count(c1))  # 2
    print(get_count(c2))  # 11
