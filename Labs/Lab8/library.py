"""
This module houses the library. The library uses a catalogue to manage its library items.
Currently, there are Books, DVDs, and Journals in the library. The library provides the interface for the user,
while the catalogue manages the Library_items.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

from catalogue import Catalogue
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
        self._item_catalogue = catalogue_of_items

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        item = self._item_catalogue.retrieve_item_by_call_number(call_number)
        if item.check_availability():
            status = self._item_catalogue.reduce_item_count(call_number)
            if status:
                print(f"Checkout complete for {type(item).__name__}: '{item.get_title()}'!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
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
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out a item")
            print("3. Return a item")
            print("4. Find a item")
            print("5. Add a item")
            print("6. Remove a item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7): ")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self._item_catalogue.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out. ")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return. ")
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item: ")
                found_titles = self._item_catalogue.find_items(input_title)
                print("We found the following: ")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._item_catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self._item_catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")


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
