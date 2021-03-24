"""
This module houses the library. The library uses a catalogue to manage its library items.
Currently, there are Books, DVDs, and Journals in the library. The library provides the interface for the user,
while the catalogue manages the Library_items.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

from catalogue import Catalogue
from ui import ConsoleUI
from library_item import LibraryItem


class Library:
    """
    The Library consists of a catalogue of items and provides an
    interface for users to check out, return and find items.
    """

    def __init__(self, catalogue_of_items):
        """
        Initialize the library with a catalogue of items.
        """
        self._ui = ConsoleUI()
        self._item_catalogue = catalogue_of_items

    def check_out_item(self):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        call_number = self._ui.get_call_num()
        item = self._item_catalogue.retrieve_item_by_call_number(call_number)
        if item.check_availability():
            status = self._item_catalogue.reduce_item_count(call_number)
            if status:
                print(f"Checkout complete for {type(item).__name__}: '{item.title}'!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """

        call_number = self._ui.get_call_num()
        status = self._item_catalogue.increment_item_count(call_number)
        if status:
            item = self._item_catalogue.retrieve_item_by_call_number(call_number)
            print(f"{type(item).__name__}: '{item.get_title()}' returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove a item.
        """
        while True:
            user_input = self._ui.main_menu()
            switch = {
                1: self.display_all_items,
                2: self.check_out_item,
                3: self.remove_item,
                4: self.find_item,
                5: self.add_item,
                6: self.remove_item,
                7: self.quit
            }
            switch.get(user_input, "Could not process the input. Please enter a number from 1 - 7.")()

    def display_all_items(self):
        items = self._item_catalogue.library_items
        self._ui.display_all_items(items)
        self._ui.pause()

    def find_item(self):
        title = self._ui.get_title()
        titles = self._item_catalogue.find_titles(title)
        if len(titles) > 0:
            print("We found the following: ")
            list(map(print, titles))
        else:
            print("Sorry! We found nothing with that title")
        self._ui.pause()

    def add_item(self):
        self._item_catalogue.add_item()

    def remove_item(self):
        call_number = self._ui.get_call_num()
        self._item_catalogue.remove_item(call_number)

    def quit(self):
        self._ui.good_bye_phrase()
        exit()


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
