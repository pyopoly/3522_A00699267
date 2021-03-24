# import abc
# from library_item import Book, DVD, Journal
#
#
# class Factory(abc.ABC):
#     @abc.abstractmethod
#     def create_library_item(self, **kwargs):
#         pass
#
#     def get_call_num_and_title(self):
#
#
# class BookFactory(Factory):
#     def create_library_item(self, d):
#         author = input("Enter Author Name: ")
#
#
# class DVDFactory(Factory):
#     def create_library_item(self, d):
#         author = input("Enter Author Name: ")
#
#
# class JournalFactory(Factory):
#     def create_library_item(self, d):
#         author = input("Enter Author Name: ")
#     # @classmethod
#     # def init_library_item(cls, call_num, title, num_copies):
#     #     """
#     #     Initializes a Book by prompting the user to add the author of the Book.
#     #     Author is a string
#     #     :param call_num: a string
#     #     :param title: a string
#     #     :param num_copies: an int
#     #     :precondition call_num: a unique identifier
#     #     :precondition num_copies: a positive integer
#     #     :return: a Book
#     #     """
#     #     return cls(call_num, title, num_copies, author)
