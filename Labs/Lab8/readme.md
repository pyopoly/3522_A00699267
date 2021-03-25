Changes made:/
- Made a UI class to delegate most of the print to this class.
- Used maps, generators and list comprehensions. 
- Used kwargs in __init__ of LibraryItem. Not in Book, DVD and Journal as I do not see the need for that, and I feel it clutters the code to use kwargs.
- Rewrote the main menu in Library to be a dictionary.
- Rewrote every method in the Library to better define responsibility.
- Used LibraryItemGenerator to create dummy data, and put it in library_item.py
- Factory pattern: FactoryMapper class for user to choose which Factory to use. Main LibraryFactory has helper method to ask for title and num_copies.