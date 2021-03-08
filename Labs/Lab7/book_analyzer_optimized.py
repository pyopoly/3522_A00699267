"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""

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
            text = book_file.readlines()
        # strip out empty lines and lower all letters
        stripped_text = (line.lower().split() for line in text if line != "\n")
        # extract words from lists as a result of split()
        words = (word for temp_list in stripped_text for word in temp_list)

        temp_text = {}
        for word in words:
            for punctuation in self.COMMON_PUNCTUATION:
                if punctuation in word:
                    word = word.replace(punctuation, '')
            temp_text[word] = None

        self.text = temp_text

    # @staticmethod
    # def is_unique(word, word_list):
    #     """
    #     Checks to see if the given word appears in the provided sequence.
    #     This check is case in-sensitive.
    #     :param word: a string
    #     :param word_list: a sequence of words
    #     :return: True if not found, false otherwise
    #     """
    #     for a_word in word_list:
    #         if word == a_word:
    #             return False
    #     return True

    # @profile
    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text
        return list(unique_word for unique_word in temp_text.keys())


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
