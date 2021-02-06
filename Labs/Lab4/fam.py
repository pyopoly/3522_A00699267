"""
This module contains the FAM class. Which is the main Class for this F.A.M. program.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

from user import User
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

    def load_test_user(self):
        """
        Generate 4 dummy Users for testing purposes.
        :return: None
        """
        # name, age, user_type, budget, account_number, balance, bank_name
        user1 = User.generate_user("John user1", 17, "Child", 10, 451, 100, "TD")
        user2 = User.generate_user("James user2", 15, "Child", 20, 598, 400, "RBC")
        user3 = User.generate_user("Jenny user3", 10, "Child", 30, 783, 50, "Scotia")
        user4 = User.generate_user("Becky user4", 13, "Child", 40, 999, 9844, "BMO")

        user_list = (user1, user2, user3, user4)
        self._user_list = user_list

    def start(self):
        """
        The starting method of the F.A.M. program.
        :return:
        """
        UI.start_menu()
        user_input = UI.user_selection_menu(self._user_list)
        current_user = self._user_list[user_input]
        UI.display_main_menu(current_user)


def main():
    """
    Start the F.A.M. program with some dummy data.
    """
    user_list = []
    fam = FAM(user_list)
    fam.load_test_user()
    fam.start()


if __name__ == '__main__':
    main()
