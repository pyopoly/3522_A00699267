"""This module houses the User."""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

from bank_account import BankAccount


class User:
    """
    Represents a user.
    """

    def __init__(self, name, age, user_type, bank_account, budget):
        """
        Initializes the User.
        """
        self._name = name
        self._age = age
        self._user_type = user_type
        self._bank_account = bank_account
        self._budget = budget

    def get_name(self):
        """
        Gets the name of the child user.
        :return a string
        """
        return self._name

    def get_age(self):
        """
        Gets the age of the user.
        :return an int
        """
        return self._age

    def set_age(self, new_age):
        """
        Sets the new age of the user.
        :param new_age: an int
        """
        self._age = new_age

    def get_user_type(self):
        """
        Gets the user type of this user.
        :return a UserType
        """
        return self._user_type

    def set_user_type(self, new_user_type):
        """
        Sets the new user type of the user
        :param new_user_type: as an user type
        """
        self._user_type = new_user_type

    def get_bank_account(self):
        """
        Gets the Bank account number of the user.
        :return: a string
        """
        return self._bank_account

    def set_bank_account(self, new_bank_account):
        """
        Sets the new bank account number of the user.
        :param new_bank_account: a string
        """
        self._bank_account = new_bank_account

    def get_budget(self):
        """
        Gets the budget of the user.
        :return: a string
        """
        return self._budget

    def set_budget(self, new_budget):
        """
        Sets the new budget of the user.
        :param new_budget: a string
        """
        self._budget = new_budget

    def record_transactions(self):
        """
        Record the transactions the user had made by prompting user to enter them.
        """
        self._bank_account.record_transaction_menu()

    def view_transactions(self):
        """
        View all transactions the user has recorded.
        :return:
        """
        self._bank_account.view_transactions()

    @classmethod
    def generate_user(cls, name, age, user_type, budget, account_number, balance, bank_name):
        """
        Instantiate a User object.
        :param name: a string
        :param age: a int
        :param user_type: a string
        :param budget: a int
        :param account_number: a int
        :param balance: a double
        :param bank_name: a string
        :return: User object
        """
        bank_account = BankAccount(account_number, balance, bank_name)
        return cls(name, age, user_type, bank_account, budget)

    def __str__(self):
        """
        Formatted string for the User.
        :return: a string
        """
        return f"Name: {self.name}, Age: {self.age}"

    name = property(get_name, None, None, "property for name")
    budget = property(get_budget, set_budget, None, "property for budget")
    age = property(get_age, None, None, "property for age")
