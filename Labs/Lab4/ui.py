"""
This module contains the UI class. UI prints out messages for the User to view, and obtains inputs from the user.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"


class UI:
    """
    UI prints out menus for the user, and gets the response from the user and calls the corresponding methods.
    Different menus can be displayed depending on user type.
    UI is used as a static class.
    """

    @staticmethod
    def user_selection_menu(user_list):
        """
        Returns the user's selection as an int, from the list of users.
        Display the users in the user_list for user to choose which User to log in as.
        :param user_list: a list of User
        :return: an int, which is the index of the user_list that was chosen by the user.
        """
        user_input = None
        size = len(user_list)

        while user_input not in range(1, size + 1):
            x = 1
            for user in user_list:
                print(f"{x}. {user.name}")
                x += 1
            print(f"{x}. Quit")
            string_input = input("Please choose the user: ")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)
        return user_input - 1

    @staticmethod
    def start_menu():
        """
        Displays a greeting message that signals the start of F.A.M.
        """
        print("\nWelcome to the F.A.M!")
        print("-----------------------")

    @staticmethod
    def display_main_menu(user):
        """
        Display the main menu allowing the user to view their budget, record a transaction,
        view transactions by budget, or view bank account details.
        """
        # current_user = self.user_selection_menu()
        self = UI()
        print(f"\nYou are logged in: {user}")
        user_input = None
        while user_input != 5:
            print("\n1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transaction by Budget")
            print("4. View Bank Account Details")
            print("5. Quit")
            string_input = input("Please enter your choice: ")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            # View Budgets
            if user_input == 1:
                print(f"your budget: {user.budget}")
                user_input = input("Press Enter to continue")
            # Record a Transaction
            elif user_input == 2:
                user.record_transactions()
            # View Transaction by Budget
            elif user_input == 3:
                user.view_transactions()
            # View Bank Account Details
            elif user_input == 4:
                print("feature under construction")
            # Quit
            elif user_input == 5:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")

        print("Thank you for using F.A.M.")
