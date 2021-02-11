from unittest import TestCase
from dictionary import Dictionary

class TestDictionary(TestCase):
    def test_load_dictionary(self):
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        self.assertIsNotNone(dictionary._dictionary)
