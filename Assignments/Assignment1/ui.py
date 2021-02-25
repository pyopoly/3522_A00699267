"""
This module contains the UI class. UI prints out messages for the User to view, and obtains inputs from the user.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

import datetime
import time
from bank_account import Category


class UI:
    """
    UI prints out menus for the user, and gets the response from the user and calls the corresponding methods.
    Different menus can be displayed depending on user type.
    UI is used as a static class.
    """

    @staticmethod
    def greeting():
        """
        Displays a greeting message that signals the start of F.A.M.
        """
        print("\nWelcome to the F.A.M!")
        print("---------------------------")

    @staticmethod
    def start_menu():
        """
        Prints out the start menu, and returns the user's choice.
        :return: int, the user's choice
        """
        PROMPT = "\n1. Register new user\n" \
                 "2. login \n" \
                 "3. Exit\n" \
                 "Your choice: "

        return UI.get_valid_input(PROMPT, 3)

    @staticmethod
    def register_user_menu():
        """
        Prints out messages to the user to help them register a User.
        Returns a newly created User based on their input
        :return: User
        """
        user_types = 3

        print("\nLet's add a new user")
        print("---------------------------")
        name = UI.get_valid_string_input("What is the name of your child: ")
        while True:
            try:
                age = int(UI.get_valid_string_input('Age of your child: '))
                if age <= 0:
                    raise ValueError
            except ValueError:
                print("\n----Please enter a positive number----")
            else:
                break
        user_type_prompt = "1. Angel\n" \
                           "2. Troublemaker\n" \
                           "3. Rebel\n" \
                           "\nSelect a user type from 1-3: "
        user_type = UI.get_valid_input(user_type_prompt, user_types)

        budgets = None
        account_number = UI.get_valid_string_input("Account Number: ")
        while True:
            try:
                balance = round(float(input("Current balance: ")), 2)
            except ValueError:
                print("\n----Please enter a valid amount----")
            else:
                if balance <= 0:
                    print("\n----Please enter a positive amount----")
                else:
                    break

        bank_name = UI.get_valid_string_input("Name of your child's bank: ")

        child = {
            "name": name,
            "age": age,
            "user_type": user_type,
            "account_number": account_number,
            "balance": balance,
            "bank_name": bank_name,
            "budgets": budgets
        }
        return child

    @staticmethod
    def display_users(user_list):
        """
        Returns the user's selection as an int, from the list of users.
        Display the users in the user_list for user to choose which User to log in as.
        :param user_list: a list of User
        :return: an int, which is the index of the user_list that was chosen by the user.
        """
        x = 1
        for user in user_list:
            print(f"{x}. {user.name} ({user.get_user_type()})")
            x += 1
        print(f"{x}. Quit")
        choice = UI.get_valid_input("Please choose the user: ", len(user_list) + 1)
        if choice == x:
            UI.exit_program()
        index = choice - 1
        return index

    @staticmethod
    def main_menu(user):
        """
        Displays a menu for the user to choose from, and returns their choice as an int.
        :param user: User object
        :return: int, the choice of the user
        """
        print(f"\nYou are logged in as: "
              f"\n{user}")
        print("---------------------------")
        print("1. View Budgets")
        print("2. Record a Transaction")
        print("3. View Transaction by Budget")
        print("4. View Bank Account Details")
        print("5. Quit")
        print("---------------------------")
        choice = UI.get_valid_input("Please enter your choice: ", 5)
        return choice

    @staticmethod
    def view_budgets(user):
        """
        Views the budget information of the User.
        :param user: User object
        :return: None
        """
        print(f"\nyour budgets:")
        print("---------------------------")
        user.view_budgets()
        print(f"Number of budgets locked: {user.num_locked_budgets()}\n")
        input("Press Enter to continue ")

    @staticmethod
    def record_transactions(user):
        """
        Prints a menu and prompts User to enter Transactions.
        Records the transactions the users had and
        adds them to the BankAccount's list of Transactions.
        :param user: User object currently using the FAM
        :return: None
        """
        print(f"\nWhat's the category of this transaction?")

        category = UI.get_category_menu()
        multiple_transactions = True
        while multiple_transactions:
            # Makes sure amount is valid
            while True:
                try:
                    amount = round(float(input("The transaction amount: ")), 2)
                except ValueError:
                    print("----Please enter a valid amount----")
                else:
                    if amount > user.remaining_balance():
                        print("\n!!!!You do not have enough balance left!!!!")
                    elif amount <= 0:
                        print("\n----Please enter a positive amount----")
                    else:
                        break
            # Makes sure vendor name is not empty
            while True:
                vendor_name = input("Name of the shop/website the transaction took place: ")
                if vendor_name != "":
                    break
            timestamp = datetime.datetime.fromtimestamp(int(time.time()))
            transaction = user.record_transaction(timestamp, amount, category, vendor_name)
            print(f"\nTransaction entered: " + transaction)
            multiple_transactions = input("Enter more transactions? (Y/N) ").capitalize() == "Y"

    @staticmethod
    def view_transactions_by_budget(user):
        """
        Prints Transactions separated by their Category.
        :param user: User that the Transactions belong to
        :return: None
        """
        print("\nYour Transactions:")
        user.view_transactions_by_budget()
        input("Press Enter to continue ")

    @staticmethod
    def view_bank_account(user):
        """
        Prints the details of the User's BankAccount
        :param user: User that the BankAccount belongs to
        :return: None
        """
        print()
        print("Bank Account Details")
        user.view_bank_account()
        print()
        input("Press Enter to continue ")

    @staticmethod
    def exit_program():
        """ Exits Fam. Prints out a farewell greeting """
        print("Thank you for using F.A.M.")

    @staticmethod
    def get_category_menu():
        """
        Prints all budget categories, and ask the user to choose one Category,
        and returns that Category.
        :return: Enum category.Category
        """
        for category in Category:
            print(f"{category.value}. {category.name.replace('_', ' ')}")
        choice = UI.get_valid_input("Please choose a category: ", len(Category))
        category = Category(choice)
        return category

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
        user_input = None
        warning = f"\n----Please type a number between 1 and {num_of_choices}----"
        while user_input not in range(1, num_of_choices + 1):
            string_input = input(prompt)
            # handles user pressing only "enter" in menu
            if string_input == '':
                print(warning)
                continue
            if not string_input.isnumeric():
                print(warning)
                continue
            user_input = int(string_input)
        return user_input

    @staticmethod
    def get_valid_string_input(prompt):
        while True:
            string_input = input(prompt)
            if string_input.strip() == '':
                print("\n----Please do not leave this empty----")
            else:
                return string_input
