import abc
import ast
from crypto import Request
from des import DesKey


class BaseHandler(abc.ABC):
    """

    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request: Request) -> (str, bool):
        pass

    def set_handler(self, handler):
        self.next_handler = handler
        return self.next_handler


class ValidateKeyHandler(BaseHandler):
    """
    This handler ensures that the key is valid, which means it must be a length of 8, 16, or 24.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """

        validate key to be 8, 16, 24
        :param request:
        :return:
        """
        key = request.key
        if len(key) in (8, 16, 24):
            if not self.next_handler:
                return "", True
            else:
                print("next")
                return self.next_handler.handle_request(request)
        else:
            return f"Key ({key}) must be 8, 16, or 24 characters long", False


class CheckInputHandler(BaseHandler):
    def handle_request(self, request: Request) -> (str, bool):
        if request.input_file and request.data_input:
            return "Cannot have both input string and input file.", False
        if request.input_file or request.data_input:
            if self.next_handler:
                return self.next_handler.handle_request(request)
            else:
                return "", True
        return "Cannot have both input data and input file to be empty.", False


class CheckFileTypeHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
        """

        request.input_file = args.file
        request.output = args.output
        :param request:
        :return:
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
    def handle_request(self, request: Request) -> (str, bool):
        if request.input_file:
            with open(request.input_file, mode='rb') as file:
                data = file.read()
                request.data_input = data
        return self.next_handler.handle_request(request)


class CheckEmptyDataHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
        """
        :param request:
        :return:
        """
        if request.data_input != b"":
            if not self.next_handler:
                return "", True
            else:
                return self.next_handler.handle_request(request)
        else:
            return "Input cannot be empty", False


class ValidateByteDataTypeHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
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
    def handle_request(self, request: Request) -> (str, bool):
        if request.output == 'print':
            return request.result, True
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True


class WriteToFileHandler(BaseHandler):

    def handle_request(self, request: Request) -> (str, bool):
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

    def handle_request(self, request: Request) -> (str, bool):
        key = DesKey(request.key.encode('utf-8'))
        data = request.data_input
        request.result = key.encrypt(data, padding=True)
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True


class DecryptionHandler(BaseHandler):
    def handle_request(self, request: Request) -> (str, bool):
        key = DesKey(request.key.encode('utf-8'))
        data = request.data_input
        if len(data) % 8 != 0:
            return "length of the message should be divisible by 8, cannot be decrypted", False
        request.result = key.decrypt(data, padding=True)
        if self.next_handler:
            return self.next_handler.handle_request(request)
        else:
            return "", True
