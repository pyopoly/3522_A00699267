"""
This module contains the BankAccount Class, which represents the financial information and history of the User.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

import datetime
import time
from transaction import Transaction


class BankAccount:
    """
    Represents the bank account of a user. The user's bank account holds information of his
    spending history (Transactions).
    """

    def __init__(self, account_number, balance, bank_name):
        """
        Initializes a BankAccount with the account number, remaining balance, and the name of the bank this BankAccount
        belongs to. Also instantiate an empty list of Transactions.
        :param account_number: a int
        :param balance: a double
        :param bank_name: a string
        :precondition account_number: a unique identifier
        """
        self._account_number = account_number
        self._balance = balance
        self._bank_name = bank_name
        self._transactions = []

    def get_balance(self):
        """
        Gets the balance of the bank account
        :return: double
        """
        return self._balance

    def get_account_number(self):
        """
        Gets the account number of the bank account
        :return: string
        """
        return self._account_number

    def get_bank_name(self):
        """
        Gets the name of the bank the
        account is in.
        :return: string
        """
        return self._bank_name

    def view_transactions(self):
        """
        Shows the transactions made by the user.
        """
        print("\nYour Transactions:")
        for transaction in self._transactions:
            print(transaction)

    def record_transaction_menu(self):
        """
        Prints a menu and prompts User to enter Transactions.
        Records the transactions the users had and
        adds them to the BankAccount's list of Transactions.
        """
        print(f"\nWhat's the category of this transaction?")
        budget_category = ("Games and Entertainment", "Clothing and Accessories", "Eating Out", "Miscellaneous")

        user_input = None
        multiple_transactions = True

        while user_input not in range(1, 6):
            print("1. Games and Entertainment")
            print("2. Clothing and Accessories")
            print("3. Eating Out")
            print("4. Miscellaneous")
            print("5. Quit")
            string_input = input("Please enter your choice (1-5): ")
            if string_input == '':
                continue
            user_input = int(string_input)

        while multiple_transactions and user_input != 5:
            amount = 0
            while amount <= 0:
                amount = round(float(input("The transaction amount: ")), 2)
            vendor_name = input("Name of the shop/website the transaction took place: ")
            timestamp = datetime.datetime.fromtimestamp(int(time.time()))

            transaction = Transaction(timestamp, amount, budget_category[user_input - 1], vendor_name)
            self._transactions.append(transaction)
            print(f"Transaction entered: {transaction}")
            multiple_transactions = input("Enter more transactions? (Y/N) ").capitalize() == "Y"

    def __str__(self):
        """
        A formatted toString.
        """
        return f"Bank Account: account number: {self.account_number}, balance: {self.balance}" \
               f"bank name: {self.bank_name}, total transactions: {len(self._transactions)}"

    balance = property(get_balance)
    account_number = property(get_account_number)
    bank_name = property(get_bank_name)
