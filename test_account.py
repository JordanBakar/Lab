import pytest
from account import *

class Test:
    def setup_method(self):
        self.account_one = Account("101 - John Smith")


    def teardown_method(self):
        del self.account_one


    def test___init__(self):
        assert self.account_one.get_name() == "101 - John Smith"
        assert self.account_one.get_balance() == 0


    def test_deposit(self):
        assert self.account_one.deposit(20000) is True
        assert self.account_one.get_balance() == 20000
        assert self.account_one.deposit(-300) is False
        assert self.account_one.get_balance() == 20000
        assert self.account_one.deposit(0) is False
        assert self.account_one.get_balance() == 20000
        assert self.account_one.deposit(77.5) is True
        assert self.account_one.get_balance() == pytest.approx(20077.5, abs=0.001)

    def test_withdraw(self):
        assert self.account_one.withdraw(20000) is False
        assert self.account_one.get_balance() == 0
        assert self.account_one.withdraw(-300) is False
        assert self.account_one.get_balance() == 0
        assert self.account_one.withdraw(0) is False
        assert self.account_one.get_balance() == 0

        self.account_one.deposit(5000)
        assert self.account_one.withdraw(77.5) is True
        assert self.account_one.get_balance() == pytest.approx(4922.5, abs=0.001)







