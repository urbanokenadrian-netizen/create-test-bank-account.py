class BankAccount:

    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("refused")

        self._owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("refused")

        self._balance = self._balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("refused")

        if amount > self._balance:
            raise ValueError("refused")

        self._balance = self._balance - amount

    def __str__(self):
        return self._owner + ": " + format(self._balance, ".2f")
