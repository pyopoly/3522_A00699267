"""
This module houses the FileHandler, the FileExtension Enum, and InvalidFileTypeError Exception. FileHandler handles
reading and writing to a external data file. FileExtension stores supported file types (txt and json), and
the InvalidFileTypeError is raised when the file extension is not in the FileExtension Enum.
"""

__author__ = "Jack Shih"
__version__ = "Feb 2021"

import enum
import pathlib
import json


class FileHandler:
    """
    Handles reading/loading data, and writing data.
    """
    @staticmethod
    def load_date(path, file_extension):
        """
        Implements how data is loaded, depending on the data types. The txt file needs to be in json format.
        :param path: string
        :param file_extension: FileExtension(Enum)
        :return: a dictionary
        """
        if not pathlib.Path(path).exists():
            raise FileNotFoundError

        if not isinstance(file_extension, FileExtensions):
            raise InvalidFileTypeError()

        if file_extension == FileExtensions["TXT"]:
            with open(path, mode='r', encoding='utf-8') as text_file:
                data = text_file.read()
                return json.loads(data)
        elif file_extension == FileExtensions["JSON"]:
            with open(path, mode='r', encoding='utf-8') as json_file:
                return json.load(json_file)

    @staticmethod
    def write_lines(path, lines):
        """
        Write to a external file. If file does not exist, it will be created.
        :param path: string for the name of the file
        :param lines: a list of strings
        :return: None
        """
        with open(path, mode='a', encoding='utf-8') as file:
            for line in lines:
                file.write(f"\n{line}")


class FileExtensions(enum.Enum):
    """
    Enum for the file extensions that are supported.
    """
    TXT = 1
    JSON = 2


class InvalidFileTypeError(OSError):
    """
    Exception which will be raised when the file extension of the data file does not match what is in the
    FileExtension Enum.
    """
    def __init__(self):
        super().__init__("This file extension is not supported. "
                         "Supported extension is a enum value in file_handler.FileExtensions")

