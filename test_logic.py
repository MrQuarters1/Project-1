import pytest
from gui import *

class Test:
    saving_window = False
    saving_balance = 100
    balance = 0
    def test_init(self) -> None:
        """
        :param self: Referenced object
        tests the init function
        :return None:
        """
        assert self.balance == 0
        assert self.saving_balance == 100
        assert self.saving_window == False
    def test_deposit(self) -> None:
        """
        :param self: Referenced object
        tests the deposit function
        :return None:
        """
        amount_input = 100
        self.balance = deposit(self.balance, amount_input)
        assert self.balance == 100
        amount_input = 50
        self.balance = deposit(self.balance, amount_input)
        assert self.balance == 150
        amount_input = "One-Hundred"
        self.balance = deposit(self.balance, amount_input)
        assert self.balance == ValueError
        amount_input = -10
        self.balance = deposit(self.balance, amount_input)
        assert self.balance == TypeError
    def test_withdraw(self) -> None:
        """
        :param self: Referenced object
        tests the withdraw function
        :return None:
        """
        self.balance = 500
        amount_input = 100
        self.balance = withdraw(self.balance, amount_input)
        assert self.balance == 400
        amount_input = "One-Hundred"
        self.balance = withdraw(self.balance, amount_input)
        assert self.balance == ValueError
        amount_input = -10
        self.balance = withdraw(self.balance, amount_input)
        assert self.balance == ValueError
        amount_input = 500
        self.balance = 400
        self.balance = withdraw(self.balance, amount_input)
        assert self.balance == TypeError

    def test_saving_withdraw(self) -> None:
        """
        :param self: Referenced object
        tests the saving_withdraw function
        :return None:
        """
        self.saving_balance = 500
        amount_input = 100
        self.saving_balance = saving_withdraw(self.saving_balance, amount_input)
        assert self.saving_balance == 400
        amount_input = "One-Hundred"
        self.saving_balance = saving_withdraw(self.saving_balance, amount_input)
        assert self.saving_balance == ValueError
        amount_input = -10
        self.saving_balance = saving_withdraw(self.saving_balance, amount_input)
        assert self.saving_balance == ValueError
        amount_input = 301
        self.saving_balance = 400
        self.saving_balance = saving_withdraw(self.saving_balance, amount_input)
        assert self.saving_balance == TypeError

