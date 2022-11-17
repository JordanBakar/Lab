class Account:
    def __init__(self, name: str) -> None:
        """
        Constructor to create default states of an account's object.
        :param name: Account's name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit money into an account.
        :param amount: Amount sent to deposit.
        :return True if the deposit occurs and False if it can not.

        """
        if amount > 0:
            self.__account_balance += amount
            return True
        elif amount <= 0:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw from an account.
        :param amount: Amount sent to withdraw.
        :return True if the withdrawal occurs and False if it can not.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to get the balance of an account.
        :return: Account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get the name of an account.
        :return: Account name.
        """
        return self.__account_name
