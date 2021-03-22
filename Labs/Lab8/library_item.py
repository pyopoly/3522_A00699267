""" library_item module contains the LibraryItem interface, and its subclasses Book, DVD, and Journal. """

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import abc


class LibraryItem(abc.ABC):
    """
    LibraryItem is an interface for all possible library items in the future.
    All library items must have a unique call number, title, and number of copies.
    """
    def __init__(self, call_num, title, num_copies):
        """
        Initializes a LibraryItem with unique call number, title, and number of copies.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_number: a unique identifier
        :precondition num_copies: a positive number
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    @classmethod
    @abc.abstractmethod
    def init_library_item(cls, call_num, title, num_copies):
        """
        Abstract method for child classes so they can implement additional instance variables
        depending on the type of library item.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_number: a unique identifier
        :precondition num_copies: a positive number
        """
        pass

    def get_title(self):
        """
        Returns the title of the item
        :return: a string
        """
        return self._title.title()

    def increment_number_of_copies(self):
        """
        Set's the number of copies of an item
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an item
        """
        self._num_copies -= 1

    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific item.
        :return: an int
        """
        return self._num_copies

    def check_availability(self):
        """
        Returns True if the item is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_num


class Book(LibraryItem):
    """
    Represents a single book in a library which is identified through
    its call number. it also has an author.
    """
    def __init__(self, call_num, title, num_copies, author):
        """
        Initializes a Book.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._author = author

    @classmethod
    def init_library_item(cls, call_num, title, num_copies):
        """
        Initializes a Book by prompting the user to add the author of the Book.
        Author is a string
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        :return: a Book
        """
        author = input("Enter Author Name: ")
        return cls(call_num, title, num_copies, author)

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the Book's attributes.
        """
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"


class DVD(LibraryItem):
    """
    Represents a DVD in a library which is identified through
    it's call number. DVDs have a release date, and a region code.
    Region code is an int from 0 to 8.
    """
    def __init__(self, call_num, title, num_copies, release_date, region_code):
        """
        Initializes a DVD.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param release_date: a string
        :param region_code: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        :precondition region_code: a positive integer from 0 to 8
        """
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    @classmethod
    def init_library_item(cls, call_num, title, num_copies):
        """
        Initializes a DVD by prompting the user to add the release date and region code
        of the DVD. Release date is a string. Region code is an int from 0 to 8.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        :return: a DVD
        """
        release_date = input("Enter release date: ")
        region_code = input("Enter region code (0 - 8): ")
        return cls(call_num, title, num_copies, release_date, region_code)

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the DVD's attributes.
        """
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Released: {self._release_date}\n" \
               f"Region code: {self._region_code}"


class Journal(LibraryItem):
    """
    Represents a single Journal in a library which is identified through
    its call number. Journals have an issue number, and a publisher
    """
    def __init__(self, call_num, title, num_copies, issue_number, publisher):
        """
        Initializes a Journal.
        :param call_num: an int
        :param title: a string
        :param num_copies: an int
        :param issue_number: an int
        :param publisher: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        :precondition issue_number: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._issue_number = issue_number
        self._publisher = publisher

    @classmethod
    def init_library_item(cls, call_num, title, num_copies):
        """
        Initializes a Journal by prompting the user to add the issue number and publisher
        of the Journal. Issue number is an int, and publisher is a string,
        :param call_num: an int
        :param title: a string
        :param num_copies: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        :precondition issue_number: a positive integer
        :return: an Journal
        """
        issue_number = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return cls(call_num, title, num_copies, issue_number, publisher)

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the Journal's attributes.
        """
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Issue number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
