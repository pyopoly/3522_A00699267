""" This module contains factories that create LibraryItems. """

__author__ = "Jack Shih"
__version__ = "Mar 2021"

import abc
from library_item import LibraryItem, Book, DVD, Journal


class Factory(abc.ABC):
    """
    The abstract Factory. Creates a library item. All LibraryItems have a call number, title, and number of
    copies. This class also has a method to get the title and number of copies from the user.
    """
    @abc.abstractmethod
    def create_library_item(self, call_number, title, num_copies) -> LibraryItem:
        """
        Creates a LibraryItem.
        :param call_number: an int
        :param title: a string
        :param num_copies: an int
        :return: LibraryItem
        """
        pass

    @staticmethod
    def get_title_and_num_copies():
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        return title, num_copies


class BookFactory(Factory):
    """
    Factory that creates a Book.
    """
    def create_library_item(self, call_number, title, num_copies) -> Book:
        """
        Books have an author.
        :param call_number: an int
        :param title: a string
        :param num_copies: an int
        :return: Book
        """
        author = input("Enter Author Name: ")
        return Book(call_number, title, num_copies, author)


class DVDFactory(Factory):
    """
    Factory that creates a DVD.
    """
    def create_library_item(self, call_number, title, num_copies) -> DVD:
        """
        DVDs have the release_date:string and region_code:int.
        :param call_number: an int
        :param title: a string
        :param num_copies: an int
        :return: DVD
        """
        release_date = input("Enter release date: ")
        region_code = input("Enter region code (0 - 8): ")
        return DVD(call_number, title, num_copies, release_date, region_code)


class JournalFactory(Factory):
    """
    Factory that creates a Journal.
    """
    def create_library_item(self, call_number, title, num_copies) -> Journal:
        """
        Journals have the issue_number: int and publisher: string.
        :param call_number: an int
        :param title: a string
        :param num_copies: an int
        :return: Journal
        """
        issue_number = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return Journal(call_number, title, num_copies, issue_number, publisher)


class FactoryMapper:
    """
    Maps the corresponding Factory to an LibraryItem during creation. The user is prompted for the choice of
    which Item they would like to create
    """
    factory_mapper = {
        1: BookFactory,
        2: DVDFactory,
        3: JournalFactory
    }

    @classmethod
    def create_item(cls, call_num):
        """
        User is prompted with the choice of which LibraryItem they would like to create. Then the corresponding
        factory is called to created the item.
        :param call_num: a string
        :precondition call_number: a unique identifier
        :return: LibraryItem
        """
        print("What type of item would you like to add?")
        print("1. Book\n"
              "2. DVD\n"
              "3. Journal\n"
              "4. Return")
        while True:
            string_input = input("Please enter your choice (1-4): ")
            if string_input == '4':
                return None
            if string_input != '':
                break
        int_input = int(string_input)
        title, num_copies = Factory.get_title_and_num_copies()
        factory = cls.factory_mapper[int_input]()
        item = factory.create_library_item(call_num, title, num_copies)
        return item

