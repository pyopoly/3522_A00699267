import difflib
import pathlib
from file_handler import FileHandler
from file_handler import FileExtensions
from file_handler import InvalidFileTypeError


class Dictionary:
    def __init__(self):
        self._dictionary = None

    def load_dictionary(self, filepath):
        if not pathlib.Path(filepath).exists() or not filepath:
            raise FileNotFoundError
        file_segments = filepath.upper().split('.')
        try:
            extension = FileExtensions[file_segments[-1]]
        except KeyError:
            raise InvalidFileTypeError
        data = FileHandler.load_date(filepath, extension)
        self._dictionary = data

    def query_definition(self, word):
        lines = [f"\n{word}"]
        try:
            for i, definition in enumerate(self._dictionary[word], start=1):
                lines.append(f"{i}. {definition}")
        except KeyError as e:
            print(f"No such word: {e}")
            return False
        return lines

    def write_to_file(self, lines):
        FileHandler.write_lines('query_history.txt', lines)

    def find_matches_in_dictionary(self, word):
        matches = difflib.get_close_matches(word.lower(), self._dictionary, cutoff=0.5)
        if not matches:
            raise NoSuchWord
        return matches

    def confirm_multiple_words(self, words):
        num_of_words = len(words)
        if num_of_words == 1:
            return words[0]
        print(f"{len(words)} words are found:")
        for i, word in enumerate(words, start=1):
            print(f"{i}. {word}")

        while True:
            try:
                choice = int(input("which word is the correct choice? "))
            except ValueError:
                print(f"please choose from 1 to {num_of_words}")
            else:
                if choice in range(1, num_of_words + 1):
                    break
                else:
                    print(f"please choose from 1 to {num_of_words}")
        return words[choice - 1]

    def start_dictionary(self):
        while True:
            word = input("\nEnter a word (exitprogram to quit): ")
            if word == "exitprogram":
                break
            try:
                matches = self.find_matches_in_dictionary(word)
            except NoSuchWord as e:
                print(e)
            else:
                word = self.confirm_multiple_words(matches)
                definition = self.query_definition(word)
                self.write_to_file(definition)
                print(*definition, sep="\n")


class NoSuchWord(ValueError):
    def __init__(self):
        super().__init__("Word not found in the dictionary.")

def main():
    dictionary = Dictionary()
    try:
        dictionary.load_dictionary("data.json")
    except InvalidFileTypeError as e:
        print(e)
    except FileNotFoundError:
        print("No such file was found")
    else:
        dictionary.start_dictionary()
    finally:
        print("\nGoodBye")


if __name__ == "__main__":
    main()
