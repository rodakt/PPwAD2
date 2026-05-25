class BankAccount:
    """Klasa reprezentująca proste konto bankowe.

    >>> acc = BankAccount("Jan Kowalski", 100)
    >>> acc.get_balance()
    100
    >>> acc.deposit(50)
    >>> acc.get_balance()
    150
    >>> acc.withdraw(30)
    >>> acc.get_balance()
    120
    >>> acc.withdraw(200)
    Traceback (most recent call last):
        ...
    ValueError: Niewystarczające środki na koncie
    >>> acc.deposit(-10)
    Traceback (most recent call last):
        ...
    ValueError: Kwota wpłaty musi być nieujemna
    >>> acc.withdraw(-5)
    Traceback (most recent call last):
        ...
    ValueError: Kwota wypłaty musi być nieujemna
    >>> acc.get_balance()
    120
    """

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Kwota wpłaty musi być nieujemna")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Kwota wypłaty musi być nieujemna")
        if amount > self.balance:
            raise ValueError("Niewystarczające środki na koncie")
        self.balance -= amount

    def get_balance(self):
        return self.balance
