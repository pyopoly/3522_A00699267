"""
This module contains the BankAccount Class, the Transaction Class, the Budget Class, and the Enum Category
for budget type.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

from enum import Enum
import random


class BankAccount:
    """
    Represents the bank account of a user, which represents the financial information and history of the User.
    The user's bank account contains a list of Transactions, a list of Budgets, remaining balance, account number,
    bank name, and the total balance of all transactions.
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
        self._budget_list = None
        self._transactions_total = 0

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

    def create_budgets(self):
        """
        Setting up the budgets for this BankAccount. Print a menu for the user and grab the amount is allowed
        for this budget.
        :return: None
        """
        budget_list = []
        print("\nNow let's talk about budgets ")
        input("Press Enter to continue ")
        for category in Category:
            print("-{0}-".format(category.name.replace("_", " ")))

            while True:
                try:
                    budget_amount = float(input("How much is allowed for this budget? "))
                except ValueError as e:
                    print("\n----Please enter a valid amount----")
                else:
                    if budget_amount < 0:
                        print("\n---Please enter a positive amount----")
                    else:
                        budget = Budget(category, budget_amount)
                        break
            budget_list.append(budget)
        self._budget_list = budget_list

    def view_budgets(self):
        """
        Print the budget information in this BankAccount.
        :return: None
        """
        for budget in self._budget_list:
            print(budget)

    def get_budget_list(self):
        """
        Gets the budget_list.
        return string
        """
        return self._budget_list

    def get_budget_by_category(self, category):
        """
        Returns a Budget in this BankAccount by matching the category of this Budget.
        :param category: Enum category.Category
        :return: Budget
        """
        for budget in self._budget_list:
            if category is budget.type:
                return budget

    def num_locked_budgets(self):
        """
        Returns a number for the number of locked budgets in this BankAccount.
        :return: a int, for the number of locked budgets
        """
        num_of_locked_budgets = 0
        for budget in self._budget_list:
            if budget.locked:
                num_of_locked_budgets += 1
        return num_of_locked_budgets

    def lock_all_budgets(self):
        """ Locks all Budgets in this BankAccount. """
        for budget in self._budget_list:
            budget.lock_budget()

    def view_transactions(self):
        """
        Shows the transactions made by the user.
        """
        print("\nYour Transactions:")
        for transaction in self._transactions:
            print(transaction)

    def view_transactions_by_budget(self):
        """
        Print Transactions in this BankAccount organized by their budget.
        Also Print the total balance of the transactions in each budget.
        :return: None
        """
        for budget in self._budget_list:
            print(f"{budget.name()}:")
            budget.print_all_transactions(self._transactions)
            budget.print_total()
            print()

    @classmethod
    def generate_dummy_bankAccount(cls):
        """
        Generate a dummy BankAccount for testing purposes.
        Bank number is a int in the range of 10000 and 99999 inclusive.
        Balance is chosen in the range of 1000.00 to 9999.99 inclusive.
        Bank name is chosen from hardcoded names.
        Budget are randomly generated automatically
        :return: BankAccount
        """
        account_number = random.randint(10000, 99999)
        balance = random.randint(100000, 999999) / 100
        bank_name = random.choice(("RBC", "Scotia Bank", "BMO", "TD", "HSBC"))
        dummy_account = cls(account_number, balance, bank_name)
        dummy_account.set_dummy_budgets()
        return dummy_account

    def set_dummy_budgets(self):
        """
        Generate dummy budgets for the BankAccount.
        The Budgets have randomly generated limit in the range of 10 to 1000 inclusive.
        :return: None
        """
        budgets = []
        for category in Category:
            budget = Budget(category, random.randint(10, 1000))
            budgets.append(budget)
        self._budget_list = budgets

    def record_transaction(self, timestamp, amount, category, vendor_name):
        """
        Record a Transaction. the Transaction is appended to the list of Transactions instance variable.
        The Transaction amount is added to the total balance of all transactions to date.
        The Transaction amount is also recorded in the corresponding budget category in the BankAccount.
        The recorded transaction is returned.
        :param timestamp: dateTime object
        :param amount: double
        :param category: Enum category.Category
        :param vendor_name: string
        :return: Transaction
        """
        transaction = Transaction(timestamp, amount, category, vendor_name)
        for budget in self._budget_list:
            if budget.type is transaction.budget_category:
                self._decrement_bank_balance(transaction.get_amount())
                budget.record_transaction(transaction)
        self._transactions.append(transaction)
        self._transactions_total += transaction.amount
        return transaction

    def _decrement_bank_balance(self, amount):
        """
        Decrements the money for each transaction made.
        :param amount: double
        :raise OutOfBalanceError: ValueError when balance is being decreased below zero
        :return: None
        """
        self._balance = round(self.balance - amount, 2)

    def view_details(self):
        """
        Print out BankAccount details. Including all BankAccount attributes and all Transactions to date, in ascending
        date order. BankAccount attributes include account_number, balance, and bank_name.
        :return: None
        """
        print(self)
        print("---------------------------")
        self.view_transactions()
        print(f"Total balance: ${self._balance}")

    def __str__(self):
        """
        A formatted toString.
        """
        return f" Account#: {self.account_number} \t Bank: {self.bank_name} " \
               f"\n Balance: ${self.balance} \t Total transactions: {len(self._transactions)}"

    balance = property(get_balance)
    account_number = property(get_account_number)
    bank_name = property(get_bank_name)


class Transaction:
    """
    Represents a transaction and the money going
    in and out of the bank account.
    """

    def __init__(self, timestamp, amount, budget_category, vendor_name):
        """
        Initializes the transaction.
        :param timestamp: dateTime
        :param amount: double
        :param budget_category: budgetCategory
        :param vendor_name: string
        """
        self._timestamp = timestamp
        self._amount = amount
        self._budget_category = budget_category
        self._vendor_name = vendor_name

    def get_timestamp(self):
        """
        Gets the timestamp of the transaction
        :return: dateTime
        """
        return self._timestamp

    def set_timestamp(self, new_timestamp):
        """
        Sets the new amount of the transactions.
        :param new_timestamp: datetime
        """
        self._timestamp = new_timestamp

    def get_amount(self):
        """
        Gets the amount of the transaction.
        :return: double
        """
        return self._amount

    def set_amount(self, new_amount):
        """
        Sets the new amount of the transactions.
        :param new_amount: double
        """
        if new_amount <= 0:
            print("Please enter an amount that is more than 0.")
        else:
            self._amount = new_amount

    def get_budget_category(self):
        """
        Gets the budget category of the transaction
        :return: budgetCategory
        """
        return self._budget_category

    def budget_category_name(self):
        """
        Returns the formatted name of this Budget.
        :return: string
        """
        return self._budget_category.name.replace("_", " ")

    def get_vendor_name(self):
        """
        Gets the name of the vendor where
        the purchase took place.
        :return: string
        """
        return self._vendor_name

    def set_vendor_name(self, new_vendor_name):
        """
        Sets the new vendor name.
        :param new_vendor_name: string
        """
        self._vendor_name = new_vendor_name

    def __str__(self):
        """ Formatted toString. """
        return f"\n==={self.budget_category_name()}=== \n\tamount: ${self.amount}, " \
               f"\n\tvendor: {self.vendor_name}, \n\ttransaction entered at: {self.timestamp}, " \
               f"\n================================================="

    timestamp = property(get_timestamp, set_timestamp)
    amount = property(get_amount, set_amount)
    budget_category = property(get_budget_category)
    vendor_name = property(get_vendor_name, set_vendor_name)


class Budget:
    """
    A Budget in a BankAccount. Budgets are meant to manage and track spending. Every Transaction belongs
    to a Budget, and once the spending in a budget is exceeded, the budget may be locked to prevent further
    spending. Each Budget has a budget type, the amount allowed, the amount spent, locked status.
    """
    default_amount_spent = 0
    default_locked_status = False

    def __init__(self, budget_type, amount_allowed):
        """
        Amount spent start from 0. Locked status starts with False. Balance for transactions start
        from 0.
        :param budget_type: Enum category.Category
        :param amount_allowed: int for the amount allowed for this budget
        """
        self._budget_type = budget_type
        self._amount_allowed = amount_allowed
        self._amount_spent = Budget.default_amount_spent
        self._locked_status = Budget.default_locked_status

    def name(self):
        """
        Returns the name of this budget.
        :return: a string
        """
        return self._budget_type.name.replace("_", " ")

    def print_all_transactions(self, transactions):
        """
        Prints the transaction in the list of Transactions that correspond to this budget.
        :param transactions: a list of Transactions
        :return: None
        """
        for transaction in transactions:
            if transaction.budget_category is self._budget_type:
                print(transaction)

    def print_total(self):
        """
        Prints the total/balance of all Transactions in this budget.
        :return: None
        """
        print(f"Transactions Total: ${self._amount_spent}")

    def record_transaction(self, transaction):
        """
        Record a transaction in this budget.
        The total amount spent is increased.
        The amount allowed, or amount still left to spent, is decreased.
        :param transaction: a Transaction
        :return: None
        """
        self._amount_spent += transaction.amount

    def budget_exceeded(self):
        """
        Checks if this budget has exceeded the allowed amount:
        amount spent is greater than amount allowed.
        :return: Boolean True if this Budget has exceeded the allowed limit
        """
        return self._amount_spent >= self._amount_allowed

    def lock_budget(self):
        """ Locks the budget. Setting the locked status to True. """
        self._locked_status = True

    def unlock(self):
        """ Unlocks the budget. Setting the locked status to False. """
        self._locked_status = False

    def get_budget_type(self):
        """ Getter for budget type. """
        return self._budget_type

    def get_amount_allowed(self):
        """ Getter for amount allowed. """
        return self._amount_allowed

    def get_amount_spent(self):
        """ Getter for amount spent. """
        return self._amount_spent

    def get_locked_status(self):
        """ Getter for current locked status. """
        return self._locked_status

    def get_amount_left(self):
        """ Getter for amount allowed. """
        return self._amount_allowed - self._amount_spent

    def __str__(self):
        """ A formatted toString. """
        status_locked = "Unlocked"
        if self.locked is True:
            status_locked = "Locked"
        return f"{self.name()}:\n \tallowed: ${self.allowed}, \tspent: ${self.spent}, \tStatus: {status_locked}" \
               f"\n---------------------------"

    type = property(get_budget_type)
    allowed = property(get_amount_allowed)
    spent = property(get_amount_spent)
    locked = property(get_locked_status)
    amount_left = property(get_amount_left)


class Category(Enum):
    """ Different type of Budget. """
    Games_and_Entertainment = 1
    Clothing_and_Accessories = 2
    Eating_Out = 3
    Miscellaneous = 4
