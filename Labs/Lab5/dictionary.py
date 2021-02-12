"""
This module houses the Dictionary, and NoSuchWordError. Dictionary lets user search a word in a dictionary file for the
definition of that word.
"""

__author__ = "Jack Shih"
__version__ = "Feb 2021"


import difflib
import pathlib
from file_handler import FileHandler
from file_handler import FileExtensions
from file_handler import InvalidFileTypeError


class Dictionary:
    """
    Dictionary class that reads an dictionary file and searches for the definition, prints out the definition, and then
    saves the definition in query_history.txt.
    """
    def __init__(self):
        """
        Initializes a dictionary instance variable that will be loaded with the data from a dictionary file.
        """
        self._dictionary = None

    def load_dictionary(self, filepath):
        """
        Load a dictionary file. If no file is found, raises an FileNotFoundError. File types supported are defined in
        the FileExtensions Enum in file_handler.py, raises InvalidFileTypeError otherwise. So far only txt
        and json are accepted.
        :param filepath: a string for the name of the file
        :raise: InvalidFileTypeError
        :raise: FileNotFoundError
        :return: None
        """
        if not pathlib.Path(filepath).exists() or not filepath:
            raise FileNotFoundError
        # split file into segments to get the file extension
        file_segments = filepath.upper().split('.')
        try:
            extension = FileExtensions[file_segments[-1]]
        except KeyError:
            raise InvalidFileTypeError
        # load data if filepath and extension are both valid
        data = FileHandler.load_date(filepath, extension)
        self._dictionary = data

    def query_definition(self, word):
        """
        Given one word, searches the dictionary and returns the word plus its definitions as a list.
        If the word is not found in the dictionary, the KeyError exception will be thrown and caught.
        :param word: string
        :return: list of string
        """
        lines = [f"\n{word}"]
        try:
            for i, definition in enumerate(self._dictionary[word], start=1):
                lines.append(f"{i}. {definition}")
        except KeyError as e:
            print(f"No such word: {e}")
            return False
        return lines

    def write_to_file(self, lines):
        """
        Write the list of definitions into query_history.txt.
        :param lines: list of string
        :return: None
        """
        FileHandler.write_lines('query_history.txt', lines)

    def find_matches_in_dictionary(self, word):
        """
        Finds close matches in the dictionary. Joins two lists of matches in which the case does not
        matter for one and the other way around for the other. Returns the list of matches.
        :param word: a string
        :return: list of string
        """
        matches = difflib.get_close_matches(word.lower(), self._dictionary, cutoff=0.5)
        matches.extend(difflib.get_close_matches(word, self._dictionary, cutoff=0.5))
        if not matches:
            raise NoSuchWordError
        return matches

    def confirm_multiple_words(self, words):
        """
        Prints out a menu of words for the user to choose from. And takes that input and returns the chosen word.
        :param words: list of strings
        :return: string
        """
        num_of_words = len(words)
        if num_of_words == 1:
            return words[0]
        print(f"{len(words)} words are found:")
        for i, word in enumerate(words, start=1):
            print(f"{i}. {word}")

        while True:
            try:
                choice = int(input("which word is the correct choice? "))
            except ValueError:
                print(f"please choose from 1 to {num_of_words}")
            else:
                if choice in range(1, num_of_words + 1):
                    break
                else:
                    print(f"please choose from 1 to {num_of_words}")
        return words[choice - 1]

    def start_dictionary(self):
        """
        Starts the dictionary. Prompts the user to input a word. Dictionary finds matches. Matches are printed for user
        to select one word. The word and its definition are grabbed from the dictionary and saved to a list. Prints the
        list and saves the list in query_history.txt.
        :return: None
        """
        while True:
            word = input("\nEnter a word (exitprogram to quit): ")
            if word == "exitprogram":
                break
            try:
                matches = self.find_matches_in_dictionary(word)
            except NoSuchWordError as e:
                print(e)
            else:
                word = self.confirm_multiple_words(matches)
                definition = self.query_definition(word)
                self.write_to_file(definition)
                print(*definition, sep="\n")


class NoSuchWordError(ValueError):
    """
    Error that is raised when the word cannot be found in the dictionary.
    """
    def __init__(self):
        super().__init__("Word not found in the dictionary.")


def main():
    """
    Driver method.
    :return: None
    """
    dictionary = Dictionary()
    try:
        dictionary.load_dictionary("data.json")
    except InvalidFileTypeError as e:
        print(e)
    except FileNotFoundError:
        print("No such file was found")
    else:
        dictionary.start_dictionary()
    finally:
        print("\nGoodBye")


if __name__ == "__main__":
    main()
