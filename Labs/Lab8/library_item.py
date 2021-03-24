""" library_item module contains the LibraryItem interface, and its subclasses Book, DVD, and Journal. """

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import abc


class LibraryItem(abc.ABC):
    """
    LibraryItem is an interface for all possible library items in the future.
    All library items must have a unique call number, title, and number of copies.
    """
    def __init__(self, **kwargs):
        """
        Initializes a LibraryItem with unique call number, title, and number of copies.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_number: a unique identifier
        :precondition num_copies: a positive number
        """
        self._call_num = kwargs["call_num"]
        self._title = kwargs["title"]
        self._num_copies = kwargs["num_copies"]

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

    @property
    def title(self):
        """
        Returns the title of the item
        :return: a string
        """
        return self._title.title()

    def __str__(self):
        return f"---- {self.__class__.__name__}: {self._title} ----\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n"


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
        super().__init__(call_num=call_num, title=title, num_copies=num_copies)
        self._author = author

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the Book's attributes.
        """
        return super().__str__() + f"Author: {self._author}"


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
        super().__init__(call_num=call_num, title=title, num_copies=num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the DVD's attributes.
        """
        return super().__str__() + f"Released: {self._release_date}\n" \
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
        super().__init__(call_num=call_num, title=title, num_copies=num_copies)
        self._issue_number = issue_number
        self._publisher = publisher

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the Journal's attributes.
        """
        return super().__str__() + f"Issue number: {self._issue_number}\n" \
                                   f"Publisher: {self._publisher}"
