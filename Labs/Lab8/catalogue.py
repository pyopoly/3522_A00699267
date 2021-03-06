"""
Catalogue manages library items. It uses LibraryItemGenerator to prompt user with an UI to add
different types of library items.
"""

__author__ = "Jack Shih"
__version__ = "Mar 2021"

import difflib
from library_item import LibraryItemGenerator


class Catalogue:
    def __init__(self, library_item_list):
        """
        Initialize the library with a list of library items.
        :param library_item_list: a sequence of library_item objects.
        """
        self._library_item_list = library_item_list

    def find_titles(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: [strings]: a list of titles.
        """
        title_list = (library_item.title for library_item in self._library_item_list)
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self, new_item):
        """
        Add a brand new item to the library with a unique call number.
        Redirects user to the LibraryItemGenerator for an UI to add different
        library items. Calls LibraryItemGenerator's class method.
        """
        self._library_item_list.append(new_item)

    def remove_item(self, call_number):
        """
        Remove an existing item from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return boolean, True if item removed
        """
        found_item = self.retrieve_item_by_call_number(call_number)
        try:
            self._library_item_list.remove(found_item)
            return True, found_item.title
        except ValueError:
            return False, None

    def retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: item object if found, None otherwise
        """
        found_item = filter(lambda item: item.call_number == call_number, self._library_item_list)
        try:
            return next(found_item)
        except StopIteration:
            return None

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count decremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def return_item(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        item = self.retrieve_item_by_call_number(call_number)
        if item:
            item.increment_number_of_copies()
            return True, type(item).__name__, item.title
        else:
            return False, None, None

    def generate_test_items(self):
        """
        Returns a list of items with dummy data.
        Calls LibraryItemGenerator's static method.
        :return: a list
        """
        dummy_item_list = LibraryItemGenerator.generate_test_items()
        self._library_item_list = dummy_item_list

    def get_library_items(self):
        """
        Returns the items in the library.
        """
        return self._library_item_list

    library_items = property(get_library_items)
