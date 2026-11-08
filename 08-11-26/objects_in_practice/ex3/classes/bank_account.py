class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            raise ValueError("not enough money")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    