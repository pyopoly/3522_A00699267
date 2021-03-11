# 3522_A00699267
BCIT_COMP3522_Projects_JackShih

BCIT Winter 2021\
Comp 3522\
author: Jack Shih

-------------------------------------------------
Lab1: \
Summary: A simple program that make calculations based on the user's selection. \
\
hypotenuse.py calculates contains one function that calculates the hypotenuse from two arguments.
calculator.py imports hypotenuse.py, and contains 4 additional calculation functions: addition, subtraction, multiplication, and division.
\
calculator.py prompts user to choose which calculation they want to perform, and asks for two inputs.
The answer is then calculated and printed out.

-------------------------------------------------
Lab2: \
Summary: Asteroids are created in a cube of 100 metres per side. Each asteroid has a randomly generated circumference, position, and velocity (metre/second). Controller contains a list of all asteroids and simulate their movements. \
\
vector.py : Helper class for asteroid.py. Vector contains attributes that represent x, y, z coordinates for an asteroid.\
asteroid.py : Asteroid moves every second. Each asteroid has a unique ID.\
controller.py : Controller contains all asteroids and runs the simulation.\
driver.py : Driver for the program.

-------------------------------------------------
Lab3: \
Summary: An implementation of a Library. User can view, check out, return, remove, add new library items. The point of this is to designate tasks to different classes based on OOP.
\
library.py : Main class. Represent the Library. Contains a simple user UI menu. Has a Catalogue. \
catalogue.py : Contains a list of LibraryItems. Performs backend work on managing the LibraryItems. \
library_item.py : Items in the Library. LibraryItem is the parent class. Book, DVD, and Journal are subclasses. \
library_item_generator.py : Helper class for Catalogue. Produces a menu for user to choose which type of LibraryItem to add.

-------------------------------------------------
Lab4: \
author: Tegvaran Sooch & Jack Shih

Summary: Lab4 is part 1 of assignment1. fam.py is the main class to start the program.
The program can: View Budget, Record transactions, View Transactions.\
View Transactions by Budget does not work yet. It only displays all transactions of the user.\
Users have no types yet.\
Budget has not been defined yet.

fam.py: Main class to start the program.\
ui.py: Menu selection for the user\
bank_account.py: Contains banking information including transactions.\

-------------------------------------------------
Lab5:\
Objective: To get familiar with writing and reading a file. Raise and catching exceptions, and unit test the code.\
Summary: Load a dictionary file and prompt the user to search a word in the dictionary file. Print the definition of that word and also save it in a query_history.txt file.

dictionary.py: \
Dictionary.start_dictionary() -> prompt user for a word -> find_matches_in_dictionary (return list of possible words) -> confirm_multiple_words (user picks one word in the list) -> query_definition (query the word in the dictionary) -> write_to_file -> print definition\
file_handler.py: \
contains methods related to reading and writing to a file. Json and Txt files are supported.

-------------------------------------------------
Lab6:\
Objective: To get familiar with the observer pattern. Use dictionary comprehension. Experiment with callable objects. \
Summary: Simulate an auction involving an auctioneer and bidders using the observer pattern.

auction_simulation.py: \
Auction: controller that starts the simulation.\
Auctioneer: manages the Bidders. The core in the observer pattern.\
Bidder: A callable object. The observer of the overser pattern.\

-------------------------------------------------
Lab7:\
Objective: To get familiar with the observer pattern. Use dictionary comprehension. Experiment with callable objects. \
Summary: Simulate an auction involving an auctioneer and bidders using the observer pattern.

book_analyzer_profiled.py:\
Problem:\
Two methods took the longest time. The method is_unique(). which was called 10001 times.\
And inside is_unique(), the word's str method .lower() is called 43525678 times. Took 17.73 seconds on my machine.

Changes made:
1. if word == a_word: on line 110: removed the .lower() for both strings.
2. temp_word = temp_word.replace(punctuation, '').lower() on line 95: added .lower() to the end.
Originally, words are popped off a list and compared with the remaining words in the list.
Each time a word is compared, every single word in the list is converted to lower case.
I changed the code so that the words were converted to lower case when the list was first made, so that the .lower()
method was only ever called for each word once.


book_analyzer_optimized.py:\
Changes made:\
1. Used generator expressions in read_data(self, src="House of Usher.txt").\
2. Used dictionary instead to store the words as keys in the dictionary, since keys must be unique,\
3. Deleted is_unique(word, word_list) as there is no need to check for unique words anymore.


-------------------------------------------------