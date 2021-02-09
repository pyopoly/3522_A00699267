import enum

class FileHandler:
    def load_date(self, path, file_extensions):
        pass

    def write_lines(self, path, lines):
        pass


class InvalidFileTypeError(Exception):
    pass


class FileExtensions(enum):
    TXT = 1
    JSON = 2
