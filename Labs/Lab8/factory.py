import abc
from library_item import Book, DVD, Journal


class Factory(abc.ABC):
    @abc.abstractmethod
    def create_library_item(self, call_number, title, num_copies):
        pass

    @staticmethod
    def get_title_and_num_copies():
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        return title, num_copies


class BookFactory(Factory):
    def create_library_item(self, call_number, title, num_copies):
        author = input("Enter Author Name: ")
        return Book(call_number, title, num_copies, author)


class DVDFactory(Factory):
    def create_library_item(self, call_number, title, num_copies):
        release_date = input("Enter release date: ")
        region_code = input("Enter region code (0 - 8): ")
        return DVD(call_number, title, num_copies, release_date, region_code)


class JournalFactory(Factory):
    def create_library_item(self, call_number, title, num_copies):
        issue_number = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return Journal(call_number, title, num_copies, issue_number, publisher)


class FactoryMapper:
    factory_mapper = {
        1: BookFactory,
        2: DVDFactory,
        3: JournalFactory
    }

    @classmethod
    def create_item(cls, call_num):
        """
        Helper method. Gets the user choice. valid_choice_list is a list of ints that user can choose from.
        Prints out the menu with the list of library item types. Append numbers to the valid_choice_list
        depending on how many items are in the cls._list_of_item_types.
        :param call_num: a string
        :precondition call_number: a unique identifier
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

