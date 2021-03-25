"""
library_item_generator module.
"""

__author__ = "Jack Shih"
__version__ = "Mar 2021"

import library_item


class LibraryItemGenerator:
    """
    LibraryItemGenerator  generates dummy data for the Library.
    """

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
