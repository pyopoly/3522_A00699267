import abc


class LibraryItem(abc.ABC):
    def __init__(self, call_num, title, num_copies):
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    @classmethod
    def generate_library_item(cls, item_type, call_num):
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))

        switch = {
            "Book": Book.init_library_item(call_num, title, num_copies),
            "DVD": DVD.init_library_item(call_num, title, num_copies),
            "Journal": Journal.init_library_item(call_num, title, num_copies)
        }
        return switch.get(item_type, "no such item")

    @classmethod
    @abc.abstractmethod
    def init_library_item(cls, call_num, title, num_copies):
        print("no such item")

    def get_title(self):
        """
        Returns the title of the book
        :return: a string
        """
        return self._title.title()

    def increment_number_of_copies(self):
        """
        Set's the number of copies of an book
        :param value: a positive integer
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an book
        :param value: a positive integer
        """
        self._num_copies -= 1

    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific book.
        :return: an int
        """
        return self._num_copies

    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
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
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, author):
        """
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
        super().__init__(call_num, title, num_copies)
        author = input("Enter Author Name: ")
        return cls(call_num, title, num_copies, author)

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"


class DVD(LibraryItem):
    """
    Represents a single book in a library which is identified through
    it's call number.
    # from library_item import LibraryItem
# # DVD's have a release date, and a region code).

    """

    def __init__(self, call_num, title, num_copies, release_date, region_code):
        """
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    @classmethod
    def init_library_item(cls, call_num, title, num_copies):
        super().__init__(call_num, title, num_copies)
        release_date = input("Enter release date: ")
        region_code = input("Enter region code (0 - 8): ")
        return cls(call_num, title, num_copies, release_date, region_code)

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Released: {self._release_date}" \
               f"Region code: {self._region_code}"


class Journal(LibraryItem):
    """
    Represents a single book in a library which is identified through.
    it's call number.
    # from library_item import LibraryItem
    # Journals have names, issue number, and a publisher),

    """

    def __init__(self, call_num, title, num_copies, issue_number, publisher):
        """
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._issue_number = issue_number
        self._publisher = publisher

    @classmethod
    def init_library_item(cls, call_num, title, num_copies):
        super().__init__(call_num, title, num_copies)
        issue_number = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return cls(call_num, title, num_copies, issue_number, publisher)

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Issue number: {self._issue_number}" \
               f"Publisher: {self._publisher}"
