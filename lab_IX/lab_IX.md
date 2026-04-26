---
title: Podstawy programowania (AD) 2
jupyter: python3
---

### Tomasz Rodak
## Lab IX

---

## Zadanie IX.1


Napisz moduł `simple_recurrence.py` zawierający funkcje:

1. `maximum_rec(seq)`, która znajduje największy element w sekwencji. Jeśli sekwencja jest pusta, funkcja powinna zgłosić wyjątek `ValueError` z komunikatem `sekwencja nie może być pusta`. Funkcja ma być zaimplementowana rekurencyjnie, a jej wywołanie powinno generować proces rekurencyjny, bez możliwości optymalizacji ogonowej.
2. `maximum_tail(seq, max_val=None)`, która znajduje największy element w sekwencji. Jeśli sekwencja jest pusta, funkcja powinna zgłosić wyjątek `ValueError` z komunikatem "sekwencja nie może być pusta". Funkcja ma być zaimplementowana rekurencyjnie, ale z akumulatorem, co pozwala na optymalizację ogonową.
3. `fib_tail(n, a=0, b=1)`, która zwraca wyraz $F_n$ ciągu Fibonacciego. Funkcja ma być zaimplementowana rekurencyjnie, ale z akumulatorem, co pozwala na optymalizację ogonową.

Testy: [`test_simple_recurrence.py`](https://github.com/rodakt/PPwAD2/blob/main/lab_IX/test_simple_recurrence.py)


## Zadanie IX.2

Na ile sposobów można wydać resztę 10 mając do dyspozycji monety o nominałach 1, 2 i 5? Oto proste rozwiązanie rekurencyjne z [SICP](https://web.mit.edu/6.001/6.037/sicp.pdf) $\S$1.2.2.

Liczba sposobów, na które można wydać resztę $a$ mając do dyspozycji $n$ monet, jest równa:

* liczbie sposobów, na które można wydać resztę $a$ mając do dyspozycji wszystkie monety poza pierwszą, plus

* liczbie sposobów, na które można wydać resztę $a-d$ mając do dyspozycji wszystkie $n$ monet, gdzie $d$ jest wartością pierwszej monety.

Dokończ definicję funkcji `count_change(amount, coins)`:

```python
def count_change(amount, coins):
    """Zwraca liczbę sposobów wydania reszty amount mając do dyspozycji monety o nominałach coins.

    >>> count_change(0, [])
    1
    >>> count_change(0, [1, 2, 3])
    1
    >>> count_change(-1, [])
    0
    >>> count_change(-1, [1, 2, 3])
    0
    >>> count_change(5, [7, 9])
    0
    >>> count_change(5, [1])
    1
    >>> count_change(5, [1, 2])
    3
    >>> count_change(100, [1, 5, 10, 25, 50]) # SICP, Ex 2.19
    292
    """
    pass
```

Sprawdź jak zmienia się czas wykonania, gdy zastosujesz zapamiętywanie wyników (dekorator `@lru_cache()` z modułu `functools`; w tym przypadku `monety` powinny być obiektem niezmiennym, np. krotką). Ile wywołań potrzeba, aby wyznaczyć liczbę sposobów wydania 200 z monetami 1, 2, 5, 10, 20, 50? Jak zmienia się wynik wraz ze zmianą funkcji z wersji oryginalnej do zapamiętującej? Kiedy zapamiętywanie jest bardziej pomocne: gdy monet jest więcej, czy gdy jest ich mniej?

## Zadanie IX.3

Celem tego zadania jest napisanie modułu `sort.py` zawierającego implementacje algorytmów [sortowania szybkiego](https://pl.wikipedia.org/wiki/Sortowanie_szybkie) i [sortowania przez scalanie](https://pl.wikipedia.org/wiki/Sortowanie_przez_scalanie). Są to rekurencyjne algorytmy sortowania wykorzystujące technikę dziel i zwyciężaj (*divide and conquer*). 

### Sortowanie szybkie

Algorytm sortowania szybkiego - wersja uproszczona wykorzystująca dodatkową pamięć i nie działająca w miejscu - może być zaimplementowana w następujący sposób:

```
qsort(A):
    zwróć A jeśli długość A jest < 1
    
    pivot <-- ostatni element A
    X <-- tablica tych elementów z A, które są < pivot
    Y <-- tablica tych elementów z A, które są == pivot
    Z <-- tablica tych elementów z A, które są > pivot
    zwróć konkatenację qsort(X), Y, qsort(Z)
```

Algorytm polega na:
* wybraniu pivota (w przykładzie powyżej jest to ostatni element tablicy),
* podziale tablicy na trzy części: elementy mniejsze od pivota, elementy równe pivotowi oraz elementy większe od pivota,
* rekurencyjnym posortowaniu elementów mniejszych i większych od pivota,
* złączeniu wyników w jedną tablicę.

Napisz funkcję `qsort(seq)`. Parametr `seq` jest sekwencją, funkcja zwraca listę wartości z `seq` posortowaną niemalejąco. Wykorzystaj podany wyżej algorytm. 

Testy: [`test_sort.py`](https://github.com/rodakt/PPwAD2/blob/main/lab_IX/test_sort.py)

### Sortowanie przez scalanie

Algorytm sortowania przez scalanie wygląda następująco:

```
mergesort(A, p, r)
  # A: lista do posortowania
  # p: indeks początkowy
  # r: indeks końcowy za ostatnim elementem

  if r is None:
    zdefiniuj r jako długość A

  if p < r - 1:
    q = (p + r) // 2  # Wyznacz indeks środkowy

    # Rekurencyjnie posortuj obie połówki
    mergesort(A, p, q)
    mergesort(A, q, r)

    # Scal posortowane połówki
    merge(A, p, q, r)
```

Działanie algorytmu polega na rekurencyjnym dzieleniu listy na połówki, aż do uzyskania list jednoelementowych, a następnie scalaniu ich w pary, aż do uzyskania jednej posortowanej listy. 

Funkcja scalająca `merge(A, p, q, r)` działa w miejscu i wygląda następująco:

```
merge(A, p, q, r)
  # A: lista do posortowania
  # p: indeks początkowy
  # q: indeks początkowy drugiej połówki
  # r: indeks końcowy za ostatnim elementem

  # test poprawności indeksów (opcjonalnie)
  if (0 <= p <= q <= r <= length(A)) then
    raise error("Incorrect indices")

  # Kopiuj podtablice
  L = A[p:q]  # podtablica od A[p] do A[q-1] (włącznie)
  R = A[q:r]  # podtablica od A[q] do A[r-1] (włącznie)
  
  # dodaj wartownika (dodatnią nieskończoność)
  append +infinity to L
  append +infinity to R

  i = 0  # indeks dla L
  j = 0  # indeks dla R
  k = p  # indeks dla A

  # Scalanie
  while k < r:
    if L[i] <= R[j]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1
    k = k + 1
```


Napisz funkcje:
* `merge(A, p, q, r)`. Parametr `A` jest listą, wartości `p`, `q`, `r` to liczby całkowite grające role indeksów.
* `mergesort(A, p=0, r=None)`. Parametr `A` jest listą, wartości `p`, `r` to liczby całkowite grające role indeksów. Zakładamy, że `0 <= p < r <= len(A)`. 

Obie funkcje działają w miejscu, tzn. modyfikują listę `A` przekazaną jako argument. Wykorzystaj podane wyżej algorytmy.

Testy: [`test_sort.py`](https://github.com/rodakt/PPwAD2/blob/main/lab_IX/test_sort.py)

## Zadanie IX.4

W grze w świnię biorą udział dwie osoby, jedynym potrzebnym rekwizytem są dwie zwykłe kości do gry. Gracz podczas ruchu rzuca obiema kościami naraz i sumuje wyniki, rzuty wykonuje aż do decyzji o wstrzymaniu swojej kolejki albo do momentu, gdy na jednej z kości wypadnie jedynka. Po wstrzymaniu kolejki suma uzyskanych oczek dodawana jest do punktów gracza. Jeśli wypadnie jedynka, to gracz nie zdobywa żadnych punktów. Gracze grają na przemian. Wygrywa ten, który jako pierwszy uzyska 100 lub więcej punktów.

Alicja i Piotr prowadzą grę w świnię. Alicja zaczyna. Strategia Alicji polega na tym, aby zawsze rzucać dwa razy, a strategia Piotra, aby zawsze rzucać trzy razy. Napisz wywołujące się nawzajem funkcje `alicja(konto_alicji, konto_piotra)`, `piotr(konto_piotra, konto_alicji)` symulujące przebieg rozgrywki. Zmienne `konto_*` przechowują aktualny stan konta obojga graczy. Wywołanie 
```python
alicja(konto_alicji, konto_piotra)
```
odpowiada zagraniu Alicji i wykonuje następujące akcje:
* sprawdza stan konta Piotra; jeśli jest `>= 100`, to Piotr wygrał, funkcja jest opuszczana z odpowiednim komunikatem; w przeciwnym razie
* wykonuje serię rzutów Alicji i aktualizuje jej konto;
* wywołuje `piotr(konto_piotra, konto_alicji)`.

Wywołanie
```python
piotr(konto_piotra, konto_alicji)
```
ma analogiczny przebieg.

Zaimplementuj symulację rozgrywki. Czyja strategia jest lepsza? Może wprowadzisz inne strategie?

## Zadanie IX.5

### Wyszukiwanie binarne

Załóżmy, że dana jest wartość `x` i tablica `A[1], A[2], ..., A[n]`. Problem polega na sprawdzeniu, czy `x` jest wartością w tablicy `A[]`. Proste rozwiązanie typu [*brute force*](https://en.wikipedia.org/wiki/Brute-force_search), to pętla przebiegająca tablicę, w której wykonuje się porównanie `x` i wartości z tablicy. Jeśli `x` nie jest wartością w `A[]`, to pętla ta musi przebiec przez całą tablicę. Ten algorytm może zostać znacznie poprawiony pod kątem wydajności czasowej, jeśli dodatkowo wiemy, że wartości w tablicy są posortowane. W tym przypadku możemy zastosować algorytm [**wyszukiwania binarnego**](https://pl.wikipedia.org/wiki/Wyszukiwanie_binarne). 

#### Zgadnij liczbę

Działa to tak. Wyobraź sobie, że Asia i Kasia grają w grę polegającą na tym, że jedna osoba zapisuje liczbę a druga ma ją odgadnąć zadając jak najmniejszą liczbę pytań pomocniczych. Pytania mają mieć ten charakter, że możliwa jest jedynia odpowiedź tak lub nie. Jeśli teraz Asia zapisze liczbę, powiedzmy że umówiony został zakres 1-100, to Kasia powinna zadać pytanie: Czy liczba jest większa od 50? Jeśli odpowiedź brzmi tak, to następnym pytaniem będzie, czy liczba jest większa od 75; w przeciwnym razie, czy liczba jest większa od 25, itd. Ten sposób wyszukiwania jest niezwykle szybki nawet dla bardzo szerokich zakresów, dla których nawet nie ma co myśleć o pętli po wszystkich dopuszczalnych wartościach. Na przykład, jeśli Asia zapisze liczbę z zakresu `1-10**100` i Kasia zna ten zakres, to wystarczą jej góra 333 pytania, aby do zapisanej liczby dotrzeć.

W przypadku omówionej gry przeszukiwana tablica to ciąg liczb całkowitych z umówionego zakresu. Napisz **rekurencyjną** funkcję `zgadnij_liczbę(a, b)`. Parametry `a`, `b` odpowiadają za zakres, w którym poszukiwana będzie liczba. Oto dwa przykładowe przebiegi wywołania, oba dla `zgadnij_liczbę(1, 1000)`:
```
Czy Twoja liczba jest większa od 500 (T/n)? 
Czy Twoja liczba jest większa od 750 (T/n)? n
Czy Twoja liczba jest większa od 625 (T/n)? n
Czy Twoja liczba jest większa od 563 (T/n)? n
Czy Twoja liczba jest większa od 532 (T/n)? n
Czy Twoja liczba jest większa od 516 (T/n)? 
Czy Twoja liczba jest większa od 524 (T/n)? n
Czy Twoja liczba jest większa od 520 (T/n)? n
Czy Twoja liczba jest większa od 518 (T/n)? 
Czy Twoja liczba jest większa od 519 (T/n)? 
Zapisałeś liczbę 520.

```
i drugie:
```
Czy Twoja liczba jest większa od 500 (T/n)? 
Czy Twoja liczba jest większa od 750 (T/n)? n
Czy Twoja liczba jest większa od 625 (T/n)? n
Czy Twoja liczba jest większa od 563 (T/n)? n
Czy Twoja liczba jest większa od 532 (T/n)? n
Czy Twoja liczba jest większa od 516 (T/n)? 
Czy Twoja liczba jest większa od 524 (T/n)? n
Czy Twoja liczba jest większa od 520 (T/n)? 
Czy Twoja liczba jest większa od 522 (T/n)? n
Czy Twoja liczba jest większa od 521 (T/n)? n
Zapisałeś liczbę 521.
```

#### Wyszukiwanie binarne w sekwencji

Dokończ definicję funkcji `binary_search(x, seq)`. Wykonaj testy zawarte w docstringu.

```python
def binary_search(x, seq):
    """
    Wykonuje rekurencyjne wyszukiwanie binarne w uporządkowanej sekwencji.

    Args:
        x (any): wartość do znalezienia.
        seq: uporządkowana sekwencja, w której szukamy.

    Returns:
        bool: True gdy x znajduje się w seq, False w przeciwnym przypadku.

    Przykłady:
        >>> binary_search(1, [])
        False

        >>> binary_search(1, [1])
        True

        >>> LICZBY = [1, 2]
        >>> all(binary_search(liczba, LICZBY) for liczba in LICZBY)
        True

        >>> any(binary_search(liczba, LICZBY) for liczba in [0, 3])
        False

        >>> LICZBY = [5, 7, 11]
        >>> all(binary_search(liczba, LICZBY) for liczba in LICZBY)
        True

        >>> any(binary_search(liczba, LICZBY) for liczba in [1, 6, 10, 12])
        False

        >>> LITERY = "abcdefghijklmnopqrstuvwxyz"
        >>> all(binary_search(litera, LITERY) for litera in LITERY)
        True

        >>> any(binary_search(znak, LITERY) for znak in "123%&")
        False
    """
    pass
```

#### Wyznaczanie miejsca zerowego funkcji wyszukiwaniem binarnym

Algorytm wyszukiwania binarnego pozwala na bardzo szybkie wyznaczanie miejsc zerowych funkcji. Wyobraź sobie, że masz daną funkcję ciągłą $y=f(x)$ określoną na przedziale $[a,b]$, która ma tę własność, że na krańcach przedziału przyjmuje wartości różnych znaków. Ponieważ funkcja jest ciągła i określona na całym przedziale $[a,b]$, więc jej wykres jest ciągłą krzywą łączącą punkty $(a,f(a))$ i $(b,f(b))$. Ponieważ jeden z tych punktów jest pod osią ox a drugi nad, więc wykres funkcji musi tę oś przeciąć, co oznacza, że w przedziale $(a, b)$ znajduje się miejsce zerowe funkcji. Weź teraz punkt $c$, który leży dokładnie w połowie przedziału:

$$
c = \frac{a + b}{2}
$$

Mamy dwie możliwości:
1. $f(c)=0$ -- znaleźliśmy miejsce zerowe, wyszukiwanie jest zakończone.
2. $f(c) \ne 0$ -- jeśli $f(a)\cdot f(c) <0$, to miejsce zerowe znajduje się w przedziale $[a, c]$; jeśli $f(b)\cdot f(c) < 0$ to miejsce zerowe znajduje się w przedziale $[c,b]$. Zauważ, że dla $f(c)\ne 0$ jeden z tych przypadków musi zachodzić.

W przypadku 2. powtarzamy powyższe postępowanie dla odpowiedniej połówki przedziału $[a,b]$. Postępujemy w ten sposób tak długo, aż albo trafimy na miejsce zerowe w środku przedziału (mało prawdopodobne), albo długość przedziału zrobi się mniejsza niż pewna ustalona z góry wartość dodatnia.

Dokończ definicję funkcji `find_root(f, a, b, abs_tol=1e-6)`. Wykonaj testy zawarte w docstringu.

```python
def find_root(f, a, b, abs_tol=1e-6):
    """
    Znajduje miejsce zerowe funkcji w zadanym przedziale.

    Parametry:
    f : funkcja, dla której szukamy miejsca zerowego.
    a : float, dolne ograniczenie przedziału.
    b : float, górne ograniczenie przedziału.
    abs_tol : float, opcjonalnie, tolerancja bezwzględna dla przybliżenia miejsca zerowego. Domyślnie 1e-6.

    Zwraca:
    float: Przybliżone miejsce zerowe funkcji w zadanym przedziale.

    Przykłady:
    >>> from math import cos, pi, isclose
    >>> abs_tol = 1e-6
    >>> f = lambda x: x
    >>> z = find_root(f, -100, 200)
    >>> isclose(z, 0, abs_tol=abs_tol)
    True

    >>> z = find_root(cos, 0, pi)
    >>> isclose(z, pi / 2, abs_tol=abs_tol)
    True

    >>> f = lambda x: x**3 - x - 2
    >>> z = find_root(f, 0, 2, abs_tol=1e-11)
    >>> isclose(z, 1.52137970680457, abs_tol=1e-11)
    True

    >>> f = lambda x: 1 + x**2
    >>> try:
    ...     find_root(f, 1, 100)
    ... except ValueError:
    ...     pass
    ... except Exception:
    ...     raise AssertionError("Nieprawidłowy rodzaj błędu.")
    ... else:
    ...     raise AssertionError("Brak wyjątku ValueError. Funkcja nie ma zera w przedziale.")
    """
    pass
```

