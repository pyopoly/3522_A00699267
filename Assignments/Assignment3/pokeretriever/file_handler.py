
class FileHandler:
    @staticmethod
    def read_file(input_filename):
        with open(input_filename, mode='r', encoding='utf-8') as data:
            return data.read().lower().splitlines()

    @staticmethod
    def write_file(output_filename):
        pass
