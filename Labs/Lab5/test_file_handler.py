from unittest import TestCase
from file_handler import FileHandler

class TestFileHandler(TestCase):
    def test_write_lines(self):
        lines = ["start", "test1", "test2", "test3", "end"]
        FileHandler.write_lines("test.txt", lines)
        with open("test.txt", mode='r', encoding="utf-8") as file:
            file = file.read().splitlines()
            self.assertEqual(file[-5:], lines)
