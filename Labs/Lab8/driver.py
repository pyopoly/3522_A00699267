""" Driver for the Library Program. """

__author__ = "Jack Shih"
__version__ = "Mar 2021"

from library import Library
from catalogue import Catalogue


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = []
    catalogue = Catalogue(item_list)
    catalogue.generate_test_items()
    my_epic_library = Library(catalogue)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
