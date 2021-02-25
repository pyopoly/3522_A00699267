"""
This module contains the FAM class. Which is the main Class for this F.A.M. program.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

from user import Angel, Troublemaker, Rebel
from ui import UI


class FAM:
    """
    FAM calls the UI class as a static class to display menus to the user, and the UI gets the user's selection.
    FAM is the control centre and gateway to the F.A.M program, and stores a list of all Users.
    """

    def __init__(self, user_list):
        """
        Initializes the F.A.M. Program. Contains a list of Users
        :param user_list: list of Users
        """
        self._user_list = user_list

    def start(self):
        """
        The starting method of the F.A.M. program.
        :return: None
        """
        UI.greeting()
        user_input = UI.start_menu()
        {
            1: self._register_user,
            2: self._login_user,
            3: self._quit
        }.get(user_input)()

    def _quit(self):
        """ Quit the FAM Program. """
        UI.exit_program()
        exit()

    def _register_user(self):
        """
        Register a User into the list of Users. Displays the menu to grab information and sets
        up the User, and add that User to the list of Users.
        :return: None
        """
        user = None
        user_info = UI.register_user_menu()
        if user_info.get("user_type") == 1:
            user = Angel.generate_user(**user_info)
        elif user_info.get("user_type") == 2:
            user = Troublemaker.generate_user(**user_info)
        elif user_info.get("user_type") == 3:
            user = Rebel.generate_user(**user_info)
        self._user_list.append(user)
        self.start()

    def _login_user(self):
        """
        Logs in the user by display a list of all users, and return
        the User that is chosen via console input.
        :return: User object
        """
        index = UI.display_users(self._user_list)
        current_user = self._user_list[index]
        self._start_fam_for_user(current_user)

    def _start_fam_for_user(self, user):
        """
        Starts the FAM program for the User object.
        :param user: User
        :return: None
        """
        while True:
            choice = UI.main_menu(user)
            if choice == 5:
                self._quit()
            switch = {
                1: UI.view_budgets,
                2: UI.record_transactions,
                3: UI.view_transactions_by_budget,
                4: UI.view_bank_account
            }
            switch.get(choice, "Could not process the input. Please enter a number from 1 - 5.")(user)

    def load_test_user(self):
        """
        Generate 4 dummy Users for testing purposes.
        :return None
        """
        user1 = Angel.generate_dummy_user(name="John user1", age=17)
        user2 = Troublemaker.generate_dummy_user(name="James user2", age=15)
        user3 = Rebel.generate_dummy_user(name="Jenny user3", age=18)
        user4 = Rebel.generate_dummy_user(name="Becky user4", age=8)

        user_list = [user1, user2, user3, user4]
        self._user_list = user_list

