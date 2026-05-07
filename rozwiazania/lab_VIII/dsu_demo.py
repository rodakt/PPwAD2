from dsu import key_minmax, key_sort

def my_max(seq):
    '''Zwraca największy element sekwencji seq.'''
    if not seq:
        raise ValueError('argument seq musi być niepusty.')
    mx = seq[0]
    for a in seq[1:]:
        if a > mx:
            mx = a
    return mx

def my_min(seq):
    '''Zwraca najmniejszy element sekwencji seq.'''
    if not seq:
        raise ValueError('argument seq musi być niepusty.')
    mn = seq[0]
    for a in seq[1:]:
        if a < mn:
            mn = a
    return mn

def selection_sort(seq):
    '''Zwraca posortowaną rosnąco listę elementów seq (sortowanie przez wybieranie).'''
    result = list(seq)
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result

pracownicy = [
    {'imię': 'Ala',    'pensja': 5000},
    {'imię': 'Bartek', 'pensja': 7000},
    {'imię': 'Cela',   'pensja': 6500},
    {'imię': 'Darek',  'pensja': 5500},
]

# Dekorujemy funkcje tak, aby obsługiwały klucz 'pensja'
get_max_salary = key_minmax(key=lambda p: p['pensja'])(my_max)
get_min_salary = key_minmax(key=lambda p: p['pensja'])(my_min)
sort_by_salary = key_sort(key=lambda p: p['pensja'])(selection_sort)

print("Najbogatszy pracownik:", get_max_salary(pracownicy))
print("Najbiedniejszy pracownik:", get_min_salary(pracownicy))

print("\nPracownicy posortowani rosnąco według pensji:")
for p in sort_by_salary(pracownicy):
    print(p)
