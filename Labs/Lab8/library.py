"""
This module houses the library. The library uses a catalogue to manage its library items.
Currently, there are Books, DVDs, and Journals in the library. The library provides the interface for the user,
while the catalogue manages the Library_items.
"""

__author__ = "Jack Shih"
__version__ = "Mar 2021"

from ui import ConsoleUI
from factory import FactoryMapper


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
        """
        call_number = self._ui.get_call_num()
        item = self._item_catalogue.retrieve_item_by_call_number(call_number)
        if item:
            title = item.title
            if item.check_availability():
                result = self._item_catalogue.reduce_item_count(call_number)
            else:
                result = False
        else:
            result = None
            title = None
        self._ui.print_check_out_result(result, call_number, type(item).__name__, title)

    def return_item(self):
        """
        Return an item with the given call number from the library.
        :precondition call_number: a unique identifier
        """
        call_number = self._ui.get_call_num()
        status, item_type, title = self._item_catalogue.return_item(call_number)
        self._ui.print_return_item_result(status, call_number, item_type, title)

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
                3: self.return_item,
                4: self.find_item,
                5: self.add_item,
                6: self.remove_item,
                7: self.quit
            }
            switch.get(user_input, "Could not process the input. Please enter a number from 1 - 7.")()

    def display_all_items(self):
        """ Display all LibraryItems in the Catalogue. """
        items = self._item_catalogue.library_items
        self._ui.display_all_items(items)
        self._ui.pause()

    def find_item(self):
        """ Find LibraryItems with similar titles in the Catalogue. """
        title = self._ui.get_title()
        titles = self._item_catalogue.find_titles(title)
        if len(titles) > 0:
            print("We found the following: ")
            list(map(print, titles))
        else:
            print("Sorry! We found nothing with that title")
        self._ui.pause()

    def add_item(self):
        """ Adds a LibraryItem to the Catalogue. The result is printed by UI. """
        call_number = self._ui.get_call_num()
        found_item = self._item_catalogue.retrieve_item_by_call_number(call_number)
        if found_item:
            result, new_item = None, None
        else:
            new_item = FactoryMapper.create_item(call_number)
            if new_item:
                self._item_catalogue.add_item(new_item)
                result = True
            else:
                result = False
        self._ui.print_add_item_result(result, call_number, new_item)
        self._ui.pause()

    def remove_item(self):
        """ Removes an LibraryItem from the Catalogue using the call number. """
        call_number = self._ui.get_call_num()
        result, title = self._item_catalogue.remove_item(call_number)
        self._ui.print_remove_item_result(result, call_number, title)

    def quit(self):
        """ Quites the program. """
        self._ui.good_bye_phrase()
        exit()

