# from book import Book
# from journal import Journal
# from dvd import DVD
import library_item

class LibraryItemGenerator:
    def __init__(self):
        self._list_of_item_types = ["Book", "DVD", "Journal"]

    def add_item(self, call_num):
        exit_num = len(self._list_of_item_types) + 1
        int_input = None
        print("What type of item would you like to add?")
        for i in range(len(self._list_of_item_types)):
            print(f"{i + 1}. {self._list_of_item_types[i]}")
        print(f"{exit_num}. Return")
        while int_input not in (1, 2, 3, exit_num):
            str_input = input("your choice: ")
            if not str_input.isnumeric():
                continue
            int_input = int(str_input)
        if int_input != exit_num:
            item_type = self._list_of_item_types[int_input - 1]
            print("item type: " + item_type)
            return self._add_library_item_by_type(item_type, call_num)

    def _add_library_item_by_type(self, item_type, call_num):
        if item_type not in self._list_of_item_types:
            print("This library does not have this item type.")
        else:
            new_item = library_item.LibraryItem.generate_library_item(item_type, call_num)
            return new_item

    @staticmethod
    def generate_test_items():
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
