""" This module contains handlers in a chain of responsibility to encrypt or decrypt data given from cmd line args. """

__author__ = "Jack Shih"
__version__ = "Mar 2021"

import abc
import ast
from crypto import Request
from des import DesKey


class BaseHandler(abc.ABC):
    """
    Abstract BaseHandler that validates a Request to encrypt or decrypt data.
    """
    def __init__(self, next_handler=None):
        """ The next handler in the chain of responsibility. Must also be of the type BaseHandler. """
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request: Request) -> (str, bool):
        """
        Handles a Request in the chain of responsibility.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        pass

    def set_handler(self, handler):
        """
        Sets the next handler for this handler.
        Returns the next handler so chaining of set_handlers() can be possible.
        :param handler: BaseHandler to be the next handler in the chain
        :return: BaseHandler, the passed in handler, which is also the next handler
        """
        self.next_handler = handler
        return self.next_handler


class ValidateKeyHandler(BaseHandler):
    """
    This handler ensures that the key is valid, which means it must be a length of 8, 16, or 24.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Validates key to be length of 8, 16, or 24.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        key = request.key
        if len(key) in (8, 16, 24):
            if not self.next_handler:
                return "", True
            else:
                return self.next_handler.handle_request(request)
        else:
            return f"Key ({key}) must be 8, 16, or 24 characters long", False


class CheckInputHandler(BaseHandler):
    """
    This handler checks ensures there is only one data source, either input_file or data_input.
    And also makes sure they are not empty strings.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Validation fails if both input_data and input_file exist, or if they are both empty.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        if request.input_file and request.data_input:
            return "Cannot have both input string and input file.", False
        if request.input_file or request.data_input:
            if self.next_handler:
                return self.next_handler.handle_request(request)
            else:
                return "", True
        return "Cannot have both input data and input file to be empty.", False


class CheckFileTypeHandler(BaseHandler):
    """
    This Handler ensures the file type for input file and/or output file are txt files.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Validation fails if input_file or output do not end in .txt
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        file_valid = True
        if not request.data_input and not request.input_file.endswith('.txt'):
            file_valid = False
        if request.output != 'print' and not request.output.endswith(".txt"):
            file_valid = False

        if file_valid:
            if not self.next_handler:
                return "", True
            else:
                return self.next_handler.handle_request(request)
        else:
            return f"File must be a txt file", False


class ReadFileHandler(BaseHandler):
    """
    This Handler reads data from the input file, if there is an input file to be read,
    else it moves on to the next handler. The data from the file is stored in request.data_input.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Validation fails if the input_file cannot be found.
        The data from the file is stored in request.data_input.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        if request.input_file:
            try:
                with open(request.input_file, mode='rb') as file:
                    data = file.read()
                    request.data_input = data
            except FileNotFoundError:
                return f"No file {request.input_file} Found", False
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True


class CheckEmptyDataHandler(BaseHandler):
    """
    This Handler ensures the data is not empty, such as in the case of an empty input file.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Validation fails if input_file contains no data.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        if request.data_input == b"":
            return "Input cannot be empty", False
        else:
            if not self.next_handler:
                return "", True
            else:
                return self.next_handler.handle_request(request)


class ValidateByteDataTypeHandler(BaseHandler):
    """
    This Handler ensures the data to be encrypted or decrypted is in bytes.
    If it is not, then converts the data to byes.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Converts data to bytes. Strings in the format of b"" or b'' are also converted to bytes.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        data = request.data_input
        if type(data) is str:
            if data.startswith('b"') and data.endswith('"') or data.startswith("b'") and data.endswith("'"):
                request.data_input = ast.literal_eval(data)
            else:
                request.data_input = data.encode('utf-8')
        if type(request.data_input) is bytes:
            if self.next_handler:
                return self.next_handler.handle_request(request)
            else:
                return "", True
        else:
            return "Data is not converted to bytes", False


class PrintOutputHandler(BaseHandler):
    """
    This handler returns the result so it can be printed.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Returns the result if Request asks the result to be printed.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        if request.output == 'print':
            if request.result:
                return request.result, True
            else:
                return "There is no result to be printed", False
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True


class WriteToFileHandler(BaseHandler):
    """
    This handler writes/overwrites the result to a text file.
    Result can be in bytes or in string.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Writes in binary mode if the result is in bytes, else string is writen to the file.
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        if not request.result:
            return "There is no result to write to file", False
        if type(request.result) is bytes:
            mode = "wb"
            encoding = None
        else:
            mode = 'w'
            encoding = 'utf-8'

        with open(request.output, mode=mode, encoding=encoding) as file:
            file.write(request.result)
        return "", True


class EncryptionHandler(BaseHandler):
    """
    This handler Encrypts the data in the Request (Request.data_input).
    ReadFileHandler will store data from a input file into Request.data_input.
    If data is from a input file. ReadFileHandler.handle_request needs to called first.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Encrypts the data with the key
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        data = request.data_input
        if not data:
            return "There is no data to be encrypted.", False
        key = DesKey(request.key.encode('utf-8'))
        request.result = key.encrypt(data, padding=True)
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True


class DecryptionHandler(BaseHandler):
    """
    This handler Decrypts the data in the Request (Request.data_input).
    ReadFileHandler will store data from a input file into Request.data_input.
    If data is from a input file. ReadFileHandler.handle_request needs to called first.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Decrypts the data with the key. Decryption can fail if the data is not valid (divisible by 8).
        :param request: Request from cmd line args
        :return: (str, bool) str: a message, bool True if validation is passed
        """
        key = DesKey(request.key.encode('utf-8'))
        data = request.data_input
        if len(data) % 8 != 0:
            return "length of the message should be divisible by 8, cannot be decrypted", False
        request.result = key.decrypt(data, padding=True)
        if request.result == b"":
            return f"Data cannot be decrypted with key {request.key}", False
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True
