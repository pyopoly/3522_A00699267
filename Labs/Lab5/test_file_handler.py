from unittest import TestCase
from file_handler import FileHandler

class TestFileHandler(TestCase):
    def test_write_lines(self):
        lines = ["start", "test1", "test2", "test3", "end"]
        FileHandler.write_lines("test.txt", lines)
        with open("test.txt", mode='r', encoding="utf-8") as file:
            file = file.read().splitlines()
            file.reverse()
            lines.reverse()
            for i in range(0, len(lines)):
                self.assertEqual(file[i], lines[i])
