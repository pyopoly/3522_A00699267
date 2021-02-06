"""
This module contains the Transaction class, which represents one transaction.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"


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
        return f"category: {self.budget_category}, amount: {self.amount}, " \
               f"vendor: {self.vendor_name}, transaction entered at: {self.timestamp}, "

    timestamp = property(get_timestamp, set_timestamp)
    amount = property(get_amount, set_amount)
    budget_category = property(get_budget_category)
    vendor_name = property(get_vendor_name, set_vendor_name)
