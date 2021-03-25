""" This modile contains the ConsoleUI. """

__author__ = "Jack Shih"
__version__ = "Mar 2021"


class ConsoleUI:
    """
    ConsoleUI prints out information to the console for the user.
    """
    def get_call_num(self):
        """
        Gets the call number from the user.
        :precondition call_number: a unique identifier
        :return string
        """
        return input("Please enter the call number of the item: ")

    def get_title(self):
        """
        Gets the title of the LibraryItem from the user.
        :return string
        """
        return input("Please enter the title of the item: ")

    def pause(self):
        """ Pause the program """
        input("Press Enter to continue")

    def good_bye_phrase(self):
        """ Phrase for exiting the program. """
        print("Thank you for visiting the Library.")

    def main_menu(self):
        """ The main menu of the program. """
        print("\nWelcome to the Library!")
        print("-----------------------")
        print("1. Display all items")
        print("2. Check Out a item")
        print("3. Return a item")
        print("4. Find a item")
        print("5. Add a item")
        print("6. Remove a item")
        print("7. Quit")
        while True:
            string_input = input("Please enter your choice (1-7): ")
            if string_input != '':
                break
        return int(string_input)

    def display_all_items(self, items):
        """ Prints all items in the Catalogue. """
        print("items List \n--------------", end="\n")
        list(map(lambda item: print(item, "\n"), items))

    def print_check_out_result(self, result, call_number, item_type, title):
        """ Prints out the result of checking out an item from the Catalogue. """
        if result:
            print(f"Checkout complete for {item_type}: '{title}'!")
        elif result is False:
            print(f"No copies left for call number {call_number}. Checkout failed.")
        else:
            print(f"Could not find item with call number {call_number}. Checkout failed.")

    def print_return_item_result(self, result, call_number, item_type, title):
        """ Prints out the result of returning an item to the Catalogue. """
        if result:
            print(f"{item_type}: '{title}' returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}. Return failed.")

    def print_add_item_result(self, result, call_number, new_item):
        """ Prints out the result of adding an item to the Catalogue. """
        if result:
            print("item added successfully! item details:")
            print(new_item, "\n")
        elif result is False:
            print("item not added")
        elif result is None:
            print(f"Could not add item with call number: {call_number}. It already exists. ")

    def print_remove_item_result(self, result, call_number, title):
        """ Prints out the result of removing an item from the Catalogue. """
        if result:
            print(f"Successfully removed {title} with call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")


