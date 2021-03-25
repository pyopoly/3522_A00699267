"""
This module contains the UI classes, which handle printing and some logic related to printing and displaying
information to the user. There is only ConsoleUI in this module, which handles printing to console.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

import abc


class UI(abc.ABC):
    """
    Abstract UI class. UI manages how the information is displayed to the user.
    """

    @abc.abstractmethod
    def menu(self, *args):
        """
        Displays a menu for user to choose from. methods from the Store class are given as param.
        UI prints these methods out as options for the user, the user chooses one method and it is
        returned to Store to be run.
        :param args: methods
        :return: a method in methods
        """
        pass

    @abc.abstractmethod
    def print_order_process_status(self, order_number, item, stock_status, restock_amount, requested_amount):
        """
        Prints the status while processing each Product. The message depends on the stock_status of the Product.
        Message displayed is different for an item that is out of stock than in stock.
        :param order_number: int
        :param item: Product
        :param stock_status: string, the status of the Product
        :param restock_amount: int
        :param requested_amount: int
        """
        pass

    @abc.abstractmethod
    def print_inventory(self, number, product, stock, stock_status_msg):
        """
        Prints the item/product in the inventory in a formatted string.
        :param number: int, the index of the item
        :param product: Product
        :param stock: int, how much is still in stock
        :param stock_status_msg: string, the status of the stock
        :return: None
        """
        pass

    @abc.abstractmethod
    def pause(self):
        """ Pauses the program and prompts the user to continue. """
        pass

    @staticmethod
    def get_valid_input(prompt, num_of_choices):
        """
        Get input from User. Also valid the input and re-prompt the user if input is invalid.
        Number of choices is the desired number of choices required of the user. Anything that is
        not an int in the range of 1 to num_of_choices inclusive will be invalid.
        :param prompt: a string msg. To show the user to prompt for their input
        :param num_of_choices: int. Total number of choices expected from this prompt.
        :return: int, the user's choice
        """
        str_input = input(prompt)
        warning = f"Please enter a number (1-{num_of_choices}): "
        while True:
            if str_input.isnumeric():
                choice = int(str_input)
                if choice in range(1, num_of_choices + 1):
                    break
            str_input = input(warning)
        return choice

    @staticmethod
    def get_valid_string_input(prompt):
        """
        Gets string input from user, making sure input is not empty
        :param prompt: string prompt to show user
        :return: string that user entered
        """
        while True:
            string_input = input(prompt)
            if string_input.strip() == '':
                print("\n----Please do not leave this empty----")
            else:
                return string_input


class ConsoleUI(UI):
    """
    Handles printing to console and logic related to printing and displaying
    information to the user. UI callas
    """

    def menu(self, *args):
        """
        Displays the menu to the user. Menu choices are methods which are given by Store.
        The method names are printed for user to choose. The chosen method is returned back to Store.
        :param args: methods
        :return: one method in methods
        """
        print("-" * 25, "\nWelcome to the store", f"\n{'-' * 25}")
        for i, method in enumerate(args, start=1):
            method_name = method.__name__.replace("_", " ").title()
            print(i, method_name)
        prompt = "Enter your choice: "
        choice = UI.get_valid_input(prompt, 3)
        return args[choice - 1]

    def print_order_process_status(self, order_number, item, stock_status, restock_amount, requested_amount):
        """
        Prints the status while processing each Product. The message depends on the stock_status of the Product.
        Message displayed is different for an item that is out of stock than in stock.
        :param order_number: int
        :param item: string, the name of the item
        :param stock_status: string, the status of the Product
        :param restock_amount: int
        :param requested_amount: int
        :return: None
        """
        if stock_status == "NEW ITEM":
            print(f"{order_number:3}. {item:40} This is a new Item.  "
                  f"Stocking {restock_amount} and selling {requested_amount:2} of it")
        elif stock_status == "OUT OF STOCK":
            print(f"{order_number:3}. {item:40} Not enough in stock. "
                  f"{restock_amount} is restocked and then selling {requested_amount}")
        elif stock_status == "IN STOCK":
            print(f"{order_number:3}. {item:40} is requested. Stock reduced by {requested_amount}")
        elif stock_status == "FAILED":
            print(f"Order {order_number} could not be processed. See details in Report on Exit.")

    def print_inventory(self, number, product, stock, stock_status_msg):
        """
        Prints the item/product in the inventory in a formatted string.
        :param number: int, the index of the item
        :param product: Product
        :param stock: int, how much is still in stock
        :param stock_status_msg: string, the status of the stock
        :return: None
        """
        print("{:3}  {:50} stock: {:3}  {}".format(number, product, stock, stock_status_msg))

    def pause(self):
        """ Pause the program. """
        input("Press Enter to continue ")

    def print_report(self, string):
        if string == "":
            print("Nothing to report")
        else:
            print(string)
