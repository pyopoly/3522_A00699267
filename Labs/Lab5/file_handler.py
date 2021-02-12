import enum
import pathlib
import json


class FileHandler:
    @staticmethod
    def load_date(path, file_extension):
        if not pathlib.Path(path).exists():
            raise FileNotFoundError

        if not isinstance(file_extension, FileExtensions):
            raise InvalidFileTypeError()

        if file_extension == FileExtensions["TXT"]:
            with open(path, mode='r', encoding='utf-8') as text_file:
                return text_file.read()
        elif file_extension == FileExtensions["JSON"]:
            with open(path, mode='r', encoding='utf-8') as json_file:
                return json.load(json_file)

    @staticmethod
    def write_lines(path, lines):
        with open(path, mode='a', encoding='utf-8') as file:
            for line in lines:
                file.write(f"\n{line}")


class FileExtensions(enum.Enum):
    TXT = 1
    JSON = 2


class InvalidFileTypeError(OSError):
    def __init__(self):
        super().__init__("This file extension is not supported. "
                         "Supported extension is a enum value in file_handler.FileExtensions")

# print(FileExtensions(1))
# data = FileHandler.load_date("data.json", FileExtensions['JSON'])
