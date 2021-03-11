lab7
Jack Shih
A00699267
Mar 2021

---------------------------
book_analyzer_profiled.py:
---------------------------
Problem:
Two methods took the longest time. The method is_unique(). which was called 10001 times,
and inside is_unique(), the word's str method .lower() is called 43525678 times. Took 17.73 seconds on my machine.

Changes made:
1. if word == a_word: on line 110: removed the .lower() for both strings
2. temp_word = temp_word.replace(punctuation, '').lower() on line 95: added .lower() to the end.
Originally, words are popped off a list and compared with the remaining words in the list.
Each time a word is compared, every single word in the list is converted to lower case.
I changed the code so that the words were converted to lower case when the list was first made, so that the .lower()
method was only ever called for each word once.


---------------------------
book_analyzer_optimized.py:
---------------------------
Changes made:
Used generator expressions in read_data(self, src="House of Usher.txt").
Used dictionary instead to store the words as keys in the dictionary, since keys must be unique,
Deleted is_unique(word, word_list) as there is no need to check for unique words anymore.
