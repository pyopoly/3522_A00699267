import difflib
# from item import item
from library_item import LibraryItem
from library_item_generator import LibraryItemGenerator


class Catalogue:
    def __init__(self, library_item_list):
        """
        Initialize the library with a list of library items.
        :param library_item_list: a sequence of library_item objects.
        """
        self._library_item_list = library_item_list
        self._library_item_generator = LibraryItemGenerator()

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_item in self._library_item_list:
            title_list.append(library_item.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new item to the library with a unique call number.
        """
        call_number = input("Enter Call Number: ")
        found_item = self.retrieve_item_by_call_number(call_number)
        if found_item:
            print(f"Could not add item with call number "
                  f"{found_item.call_number}. It already exists. ")
        else:
            new_item = self._library_item_generator.add_item(call_number)
            if new_item:
                self._library_item_list.append(new_item)
                print("item added successfully! item details:")
                print(new_item)
            else:
                print("item not added")

    def remove_item(self, call_number):
        """
        Remove an existing item from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self.retrieve_item_by_call_number(call_number)
        if found_item:
            self._library_item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")

    # ==========
    def retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for library_item in self._library_item_list:
            if library_item.call_number == call_number:
                found_item = library_item
                break
        return found_item

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("items List")
        print("--------------", end="\n\n")
        for library_item in self._library_item_list:
            print(library_item)
            print()

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

    def increment_item_count(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False

    def generate_test_items(self):
        """
        Return a list of items with dummy data.
        :return: a list
        """
        dummy_item_list = self._library_item_generator.generate_test_items()
        self._library_item_list = dummy_item_list
