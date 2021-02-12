"""
Unit Testing to test methods in Dictionary.
"""

__author__ = "Jack Shih"
__version__ = "Feb 2021"

from unittest import TestCase
from unittest.mock import patch
from dictionary import Dictionary
from file_handler import InvalidFileTypeError
from dictionary import NoSuchWordError


class TestDictionary(TestCase):
    """
    Unit testing for dictionary.py. Methods tested are load_dictionary, query_definition, find_matches_in_dictionary,
    and confirm_multiple_words.
    """

    def test_load_dictionary_json(self):
        """ Test if json file is loaded successfully. """
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        self.assertIsNotNone(dictionary._dictionary)

    def test_load_dictionary_txt(self):
        """ Test if text file is loaded successfully. """
        dictionary = Dictionary()
        dictionary.load_dictionary("data.txt")
        self.assertIsNotNone(dictionary._dictionary)

    def test_load_dictionary_unsupported_extension(self):
        """ Test if unsupported file type throws the InvalidFileTypeError. """
        dictionary = Dictionary()
        self.assertRaises(InvalidFileTypeError, lambda: dictionary.load_dictionary("dictionary.py"))

    def test_load_dictionary_wrong_file(self):
        """ Test if FileNotFoundError is thrown if trying to read a non-existent file. """
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, lambda: dictionary.load_dictionary("data.bob"))

    def test_load_dictionary_no_file(self):
        """ Test if the file path is empty, that it will throw a FileNotFoundError. """
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, lambda: dictionary.load_dictionary(""))

    def test_query_definition_existent_word(self):
        """ Test if definition is returned when a word is being queried in the dictionary. """
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        definition = dictionary.query_definition("dog")
        self.assertTrue(definition)

    def test_query_definition_non_existent_word(self):
        """ Test if a non-existent word is being queried in the dictionary, then False is returned. """
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        definition = dictionary.query_definition("dddddd")
        self.assertFalse(definition)

    def test_find_matches_in_dictionary_match_found(self):
        """ Test if a list of some matches are returned when trying to find close matches in the dictionary."""
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        matches = dictionary.find_matches_in_dictionary("dog")
        self.assertTrue(matches)

    def test_find_matches_in_dictionary_no_match(self):
        """ Test if no matches can be found in the dictionary, a NoSuchWordError will be raised. """
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        self.assertRaises(NoSuchWordError, lambda: dictionary.find_matches_in_dictionary(""))

    @patch('dictionary.Dictionary.get_input', return_value="1")
    def test_confirm_multiple_words(self, get_input):
        """
        Test if the word the user hsa chosen via console is returned correctly.
        @patch emulates user input as "1". Therefore the first word in a list of words is the default word to be chosen.
        :param get_input: method as obj, Dictionary.get_input
        """
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        words = ["dog", "cat"]
        word = dictionary.confirm_multiple_words(words)
        self.assertEqual(word, "dog")
