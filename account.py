class Account:
    def __init__(self, name=0) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        elif amount <= 0:
            return False

    def withdraw(self, amount):
        if amount > 0:
            self.__account_balance -= amount
            return True
        elif amount <= 0 or amount > self.__account_balance:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
