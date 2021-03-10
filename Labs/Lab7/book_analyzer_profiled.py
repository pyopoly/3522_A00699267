"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""
__author__ = "Jack Shih"
__version__ = "Jan 2021"


"""
Problem:
Two methods took the longest time. The method is_unique(). which was called 10001 times.
And inside is_unique(), the word's str method .lower() is called 43525678 times. Took 17.73 seconds on my machine.

Changes made:
1. if word == a_word: on line 107: removed the .lower() for both strings
2. temp_word = temp_word.replace(punctuation, '').lower() on line 92: added .lower() to the end.
Originally, words are popped off a list and compared with the remaining words in the list.
Each time a word is compared, every single word in the list is converted to lower case.
I changed the code so that the words were converted to lower case when the list was first made, so that the .lower()
method was only ever called for each word once.
"""

import pstats, cProfile, io


def profile(fnc):
    """
    An implementation of a function decorator that wraps a function in
    a code that profiles it.
    """

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()

        # wrapped function starts
        retval = fnc(*args, **kwargs)  # fnc is whatever function has the @profile tag
        # wrapped function ends

        pr.disable()
        s = io.StringIO()
        sortby = pstats.SortKey.CALLS
        ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    # @profile
    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        # remove common punctuation from words
        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, '').lower()
            temp_text.append(temp_word)

        self.text = temp_text

    @staticmethod
    def is_unique(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is case in-sensitive.
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """
        for a_word in word_list:
            if word == a_word:
                return False
        return True

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text
        unique_words = []
        while temp_text:
            word = temp_text.pop()
            if self.is_unique(word, temp_text):
                unique_words.append(word)
        return unique_words


@profile
def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for word in unique_words:
        print(word)
    print("-" * 50)


if __name__ == '__main__':
    main()
