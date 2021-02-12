from unittest import TestCase
from dictionary import Dictionary
from file_handler import InvalidFileTypeError
from dictionary import NoSuchWordError


class TestDictionary(TestCase):

    def test_load_dictionary_json(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        self.assertIsNotNone(dictionary._dictionary)

    def test_load_dictionary_txt(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.txt")
        self.assertIsNotNone(dictionary._dictionary)

    def test_load_dictionary_unsupported_extension(self):
        dictionary = Dictionary()
        self.assertRaises(InvalidFileTypeError, lambda: dictionary.load_dictionary("dictionary.py"))

    def test_load_dictionary_wrong_file(self):
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, lambda: dictionary.load_dictionary("data.bob"))

    def test_load_dictionary_no_file(self):
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, lambda: dictionary.load_dictionary(""))

    def test_query_definition_existent_word(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        definition = dictionary.query_definition("dog")
        self.assertTrue(definition)

    def test_query_definition_non_existent_word(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        definition = dictionary.query_definition("dddddd")
        self.assertFalse(definition)

    def test_find_matches_in_dictionary_match_found(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        matches = dictionary.find_matches_in_dictionary("dog")
        self.assertTrue(matches)

    def test_find_matches_in_dictionary_no_match(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        self.assertRaises(NoSuchWordError, lambda: dictionary.find_matches_in_dictionary(""))

    # def test_confirm_multiple_words(self):
    #     self.fail()
