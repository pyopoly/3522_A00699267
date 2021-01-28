"""
library_item_generator module manages LibraryItem types, such as DVD, Book, or Journal.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import library_item


class LibraryItemGenerator:
    """
    LibraryItemGenerator prompts user with an UI to select the type of library they want,
    and then add that item. Used as a static class by Catalogue. It contains Classes of Book,
    DVD, and Journals, but not instances of them.
    It also generates dummy data for the Library.
    """
    _list_of_item_types = [library_item.Book, library_item.DVD, library_item.Journal]

    @classmethod
    def add_item(cls, call_num):
        """
        Add a LibraryItem based on user's choice. Uses the types in cls._list_of_item_types.
        :param call_num: a string
        :precondition call_number: a unique identifier
        :return: a type of LibraryItem
        """
        # exit number for the UI menu is one number higher than the total number of library item type
        exit_num = len(cls._list_of_item_types) + 1
        valid_choice_list = [exit_num]

        cls._print_menu(valid_choice_list)
        # Lets user return to main Library menu
        print(f"{exit_num}. Return")

        int_input = cls._get_valid_user_input(valid_choice_list)
        # obtain LibraryItem that the user chose and store it in item_type, exit if input == exit_num
        if int_input != exit_num:
            item_type = cls._list_of_item_types[int_input - 1]
            print("item type: " + item_type.__name__)
            title = input("Enter title: ")
            num_copies = int(input("Enter number of copies "
                                   "(positive number): "))

            # instantiate and return the LibraryItem depending on the type of LibraryItem
            return item_type.init_library_item(call_num, title, num_copies)

    @classmethod
    def _print_menu(cls, valid_choice_list):
        """
        Helper method. Gets the user choice. valid_choice_list is a list of ints that user can choose from.
        Prints out the menu with the list of library item types. Append numbers to the valid_choice_list
        depending on how many items are in the cls._list_of_item_types.
        :param valid_choice_list: list of ints
        """
        print("What type of item would you like to add?")
        for i in range(len(cls._list_of_item_types)):
            name = cls._list_of_item_types[i].__name__
            print(f"{i + 1}. {name}")
            valid_choice_list.append(i + 1)

    @classmethod
    def _get_valid_user_input(cls, valid_choice_list):
        """
        Helper method. Ensures that the user's choice is valid, that it is an int, and that it is
        in the valid_choice list.
        :param valid_choice_list: list of int
        :return: an int, the user's choice
        """
        int_input = None
        while int_input not in valid_choice_list:
            str_input = input("your choice: ")
            if not str_input.isnumeric():  # Ensure user input is an int
                continue
            int_input = int(str_input)
        return int_input

    @staticmethod
    def generate_test_items():
        """
        Generate dummy data for the Library
        :return: a list of Dummy LibraryItem
        """
        book = library_item.Book
        dvd = library_item.DVD
        journal = library_item.Journal
        dummy_item_list = [
            book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
            book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
            book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
            book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
            dvd("001.222.333", "Life of Pi", 2, "Jan 2, 2007", 6),
            journal("21.12.321", "Medical journal", 3, 4, "Public Library of Science")
        ]
        return dummy_item_list
