"""
Unit Testing to test methods in FileHandler.
"""

__author__ = "Jack Shih"
__version__ = "Feb 2021"

from unittest import TestCase
from file_handler import FileHandler
from file_handler import FileExtensions
from file_handler import InvalidFileTypeError


class TestFileHandler(TestCase):
    """
    Unit Testing for file_handler.py. Methods test are load_data and write_lines.
    """
    def test_load_date_json(self):
        """ Test if some data is returned (True) when data.json is loaded/read. """
        self.assertTrue(FileHandler.load_date('data.json', FileExtensions['JSON']))

    def test_load_date_txt(self):
        """ Test if some data is returned (True) when data.txt is loaded/read. """
        self.assertTrue(FileHandler.load_date('data.txt', FileExtensions['TXT']))

    def test_load_date_wrong_extension(self):
        """ Test if InvalidFileTypeError is raised when file type is not supported. """
        self.assertRaises(InvalidFileTypeError, lambda: FileHandler.load_date('dictionary.py', "test"))

    def test_load_date_no_file(self):
        """ Test if FileNotFoundError is raised when no file can be found. """
        self.assertRaises(FileNotFoundError, lambda: FileHandler.load_date('', FileExtensions['JSON']))

    def test_write_lines(self):
        """
        Test if lines are written by appending to test.txt text file successfully.
        File is read and split into a list by lines.
        """
        lines = ["start", "test1", "test2", "test3", "end"]
        FileHandler.write_lines("test.txt", lines)
        with open("test.txt", mode='r', encoding="utf-8") as file:
            file = file.read().splitlines()
            self.assertEqual(file[-5:], lines)
