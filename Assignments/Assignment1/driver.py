"""
Driver for the F.A.M. (Family Appointed Moderator) Program.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Feb 2021"

from fam import FAM


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
