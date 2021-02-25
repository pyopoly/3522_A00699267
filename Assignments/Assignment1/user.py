"""This module houses the User Class, the subclass of User: Child Class, and Subclasses of Child:
Angel, TroubleMaker and Rebel. Angel, TroubleMaker, and Rebel do not have any methods, they merely have
the different default values. The User and Child classes are not meant to be instantiated. """

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

from bank_account import BankAccount


class User:
    """
    Represents a user.
    """
    def __init__(self, name, age, bank_account):
        """
        Initializes the User.
        """
        self._name = name
        self._age = age
        self._bank_account = bank_account

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
        return self.__class__.__name__

    def get_budget_by_category(self, category):
        """
        Returns a budget for this User by matching the Category.
        :param category: Enum category.Category
        :return: Budget
        """
        return self._bank_account.get_budget_by_category(category)

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

    def view_bank_account(self):
        """ Prints the current Bank Account details. """
        self._bank_account.view_details()

    def num_locked_budgets(self):
        """
        Returns the current total number of locked budgets.
        :return: int
        """
        return self._bank_account.num_locked_budgets()

    def lock_all_budgets(self):
        """ Locks all budgets for this User. """
        self._bank_account.lock_all_budgets()

    def record_transaction(self, timestamp, amount, category, vendor_name):
        """
        Record the transactions the user had made by prompting user to enter them.
        :param timestamp: dateTime object
        :param amount: double
        :param category: Enum category.Category
        :param vendor_name: string
        :return: string of the details of the Transaction
        """
        return f"{self._bank_account.record_transaction(timestamp, amount, category, vendor_name)}"

    def view_transactions(self):
        """
        View all transactions the user has recorded.
        :return: None
        """
        self._bank_account.view_transactions()

    def view_transactions_by_budget(self):
        """
        Display Transactions categorized by their budget type.
        :return: None
        """
        self._bank_account.view_transactions_by_budget()

    def view_budgets(self):
        """
        View the details of all the budgets for this User, including the amount spent, amount allowed,
        if it is locked.
        :return: None.
        """
        self._bank_account.view_budgets()

    def remaining_balance(self):
        """
        Returns the remaining balance the user has in the BankAccount
        :return: double
        """
        return self._bank_account.balance

    @classmethod
    def generate_user(cls, **kwargs):
        """
        Create a new user by passing in all user attributes including the BankAccount attributes.
        :param kwargs:
            name: string
            age: int
            user_type: Enum category.UserType
        :return:
        """
        name = kwargs["name"]
        age = kwargs["age"]
        account_number = kwargs["account_number"]
        balance = kwargs["balance"]
        bank_name = kwargs["bank_name"]
        bank_account = BankAccount(account_number, balance, bank_name)
        bank_account.create_budgets()
        return cls(name, age, bank_account)

    @classmethod
    def generate_dummy_user(cls, **kwargs):
        """
        Generate a dummy user for testing purposes. Bank account info is randomly generated automatically.
        What goes in the parameters are the name, age, and user type of the Dummy User.
        :param kwargs:
            name: a string
            age: a int
            user_type: Enum category.UserType
        :return: a User, randomly generated User
        """
        name = kwargs["name"]
        age = kwargs["age"]
        bank_account = BankAccount.generate_dummy_bankAccount()
        return cls(name, age, bank_account)

    def __str__(self):
        """
        Formatted string for the User.
        :return: a string
        """
        return f"Name: {self._name}, Age: {self.age} ({self.get_user_type()})"

    name = property(get_name, None, None, "property for name")
    age = property(get_age, None, None, "property for age")


class Child(User):
    """
    Child class represent a basic framework for Children classes. This class is the default Child, and
    not meant to be instantiated.
    """
    WARNING_PERCENT = 0
    LOCK_LIMIT = None
    LOCKED_ACCOUNTS_ALLOWED = 4

    REMINDER = "----You have exceeded a percentage of your budget: "
    EXCEEDED_MSG = "!!!!!!You exceeded 100% of your budget: "
    LOCK_MSG = "!!!!!!!!This budget is locked!!!!!!!!!!!!!"

    def record_transaction(self, timestamp, amount, category, vendor_name):
        """
        Record a Transaction. This method handles the logic for warning the Child about their budget status,
        and does not handle the actual recording of the transaction.
        :param timestamp:
        :param amount:
        :param category:
        :param vendor_name:
        :return:
        """
        budget = self.get_budget_by_category(category)
        if not budget.locked:
            recorded_transaction = super().record_transaction(timestamp, amount, category, vendor_name)
        else:
            return "!!!!!!!Your account is locked!!!!!!!!!!"
        if budget.budget_exceeded():
            self.budget_exceeded_reminder(budget)
            if self.LOCK_LIMIT:
                self.lock_account(budget)
        else:
            self.budget_percentage_exceeded_reminder(budget)
        return recorded_transaction

    def budget_percentage_exceeded_reminder(self, budget):
        """
        Checks if the budget exceeded the Warning Percentage, and prints out the reminder msg.
        :param budget: Budget of the user, from user's BankAccount
        :return: None
        """
        if budget.spent >= budget.allowed * self.WARNING_PERCENT:
            print(self.REMINDER + budget.name())

    def budget_exceeded_reminder(self, budget):
        """
        Prints out the Budget limit exceeded msg.
        :param budget: Budget of the user, from user's BankAccount
        :return: None
        """
        print(self.EXCEEDED_MSG + budget.name())

    def lock_account(self, budget):
        """
         Locks the account according to the status of the Child User.
         Checks if Lock limit is exceeded, if it is, lock the budget.
         Then checks if total number of locked budgets exceeded the allowed limit,
         if so, lock all budgets.
        :param budget: Budget of the user, from user's BankAccount
        :return: None
        """
        if budget.spent >= budget.allowed * self.LOCK_LIMIT:
            budget.lock_budget()
            print(self.LOCK_MSG, budget.name())
            if self.num_locked_budgets() >= self.LOCKED_ACCOUNTS_ALLOWED:
                print("!!!!YOU ARE LOCKED OUT OF EVERY THING!!!")
                self.lock_all_budgets()


class Angel(Child):
    """
    Never gets locked out of a budget category. No LOCK_LIMIT.
    They can continue spending money even if they exceed the budget in question.
    Gets politely notified if they exceed a budget category.
    Gets a warning if they exceed more than 90% of a budget. WARNING_PERCENT = 0.9
    """
    WARNING_PERCENT = 0.9
    LOCK_LIMIT = None
    REMINDER = "\nYou have exceeded more than 90% of your budget for: "
    EXCEEDED_MSG = "\nYou have exceeded your budget for: "


class Troublemaker(Child):
    """
    Gets a warning if they exceed more than 75% of a budget category. WARNING_PERCENT = 0.75
    Gets politely notified iIf they exceed a budget category.
    Gets locked out of conducting transactions in a budget category if they exceed it by
    120% of the amount assigned to the budget in question. LOCK_LIMIT = 1.2
    """
    WARNING_PERCENT = 0.75
    LOCK_LIMIT = 1.2
    REMINDER = "\n----You have exceeded more than 75% of your budget for: "
    EXCEEDED_MSG = "\n!!!You have exceeded your budget for: "
    LOCK_MSG = "\n!!!!!!!You have reached the lock limit of 120%!!!!!!!\n" \
               "!!!!!!!THIS BUDGET TYPE IS LOCKED: "


class Rebel(Child):
    """
    They get a warning for every transaction after exceeding 50% of a budget. WARNING_LIMIT = 0.5
    Gets ruthlessly notified if they exceed a budget category.
    Gets locked out of conducting transactions in a budget category if they exceed it by
    100% of the amount assigned to the budget in question. LOCK_LIMIT = 1
    If they exceed their budget in 2 or more categories then they get locked out of their account completely.
    LOCKED_ACCOUNTS_ALLOWED = 2
    """
    WARNING_LIMIT = 0.5
    LOCK_LIMIT = 1
    LOCKED_ACCOUNTS_ALLOWED = 2
    REMINDER = "\nYou have exceeded more than 50% of your budget for: "
    EXCEEDED_MSG = "\nYou have exceeded your budget for :"
    LOCK_MSG = "!!!!!!!You have reached the lock limit of 100%!!!!!!!\n" \
               "!!!!!!!THIS BUDGET TYPE IS LOCKED: "



