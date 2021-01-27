""" This module houses the library"""
from book import Book
from catalogue import Catalogue


class Library:
    """
    The Library consists of a catalogue of books and provides an
    interface for users to check out, return and find books.
    """

    def __init__(self, catalogue_of_books):
        """
        Initialize the library with a catalogue of books.
        :param catalogue_of_books: a catalogue that contains a list of Books.
        """
        self._book_catalogue = catalogue_of_books

    def check_out(self, call_number):
        """
        Check out an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_book = self._book_catalogue._retrieve_book_by_call_number(call_number)
        if library_book.check_availability():
            status = self._book_catalogue.reduce_book_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find book with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_book(self, call_number):
        """
        Return an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_book_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all books")
            print("2. Check Out a book")
            print("3. Return a book")
            print("4. Find a book")
            print("5. Add a book")
            print("6. Remove a book")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if (string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_books()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the book"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the book"
                                    " you wish to return.")
                self.return_book(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the book:")
                found_titles = self.find_books(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.add_book()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self.remove_book(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")






def generate_test_books():
    """
    Return a list of books with dummy data.
    :return: a list
    """
    book_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss")
    ]
    return book_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    book_list = generate_test_books()
    my_epic_library = Library(book_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
