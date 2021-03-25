""" This module contains the FileHandler classes. """

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

import abc
import pathlib
import pandas


class FileHandler:
    @staticmethod
    def read_order(filepath):
        """
        Read an order from the filepath. Chooses the child FileHandler class responsible for reading different
        file types.
        :param filepath:
        :raises: FileNotFoundError
        :return: generator for a list of dictionaries representing order details
        """
        if not pathlib.Path(filepath).exists():
            raise FileNotFoundError

        if filepath.endswith("xlsx"):
            return ExcelFileSource().read_file(filepath)

    @staticmethod
    def write_order(filepath, lines):
        """
        Writes to a file named filepath. Chooses the child FileHandler class responsible for writing different
        file types.
        :param filepath: string
        :param lines: string
        """
        if filepath.endswith("txt"):
            return TxtFileSource().write_file(filepath, lines)


class ReadableFileSource(abc.ABC):
    """
    Reads an order request file. Abstract parent class that will decides which child FileHandler class is needed
    to read the File.
    """
    @abc.abstractmethod
    def read_file(self, filepath) -> list[dict]:
        """ Reads an file. Must return a list of multiple dictionaries. Each dictionary represents one Order. """
        pass


class WritableFileSource(abc.ABC):
    @abc.abstractmethod
    def write_file(self, filepath, lines):
        """
        Writing given lines to a .txt file.
        :param filepath: path of the file as string
        :param lines: as string.
        """
        pass


class ExcelFileSource(ReadableFileSource):
    """
    Reads an Excel File.
    """
    def read_file(self, filepath):
        """
        Read an xlsx excel file that contains orders and their details. Each item in the list that is returned is a
        dictionary of the details of the order.
        :param filepath: string
        :return: generator for a list of dictionaries representing order details
        """
        file = pandas.read_excel(filepath)
        rows = len(file)
        orders = (pandas.DataFrame(file).loc[i].to_dict() for i in range(rows))
        return orders


class TxtFileSource(WritableFileSource):
    """
    Reads and writes to an txt file.
    """
    def write_file(self, filepath, lines):
        """
        Writing given lines to a .txt file.
        :param filepath: path of the file as string
        :param lines: as string.
        """
        with open(filepath, mode='a') as appended_file:
            appended_file.write(lines)
