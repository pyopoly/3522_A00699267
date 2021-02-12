from unittest import TestCase
from dictionary import Dictionary
from file_handler import FileExtensionNotSupported


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
        self.assertRaises(FileExtensionNotSupported, lambda: dictionary.load_dictionary("dictionary.py"))

    def test_load_dictionary_wrong_file(self):
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, lambda: dictionary.load_dictionary("data.bob"))

    def test_load_dictionary_no_file(self):
        dictionary = Dictionary()
        self.assertRaises(FileNotFoundError, lambda: dictionary.load_dictionary(""))

    def test_query_definition(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        dictionary.query_definition()
