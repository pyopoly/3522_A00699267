import difflib
import pathlib
from file_handler import FileHandler
from file_handler import FileExtensions
from file_handler import FileExtensionNotSupported

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
            raise FileExtensionNotSupported
        data = FileHandler.load_date(filepath, extension)
        self._dictionary = data

    def query_definition(self, word):
        matches = difflib.get_close_matches(word, self._dictionary, cutoff=0.5)
        word = self.confirm_mutiple_words(matches)
        if word is False:
            raise NoSuchWord
        lines = [f"\n{word}"]
        for i, definition in enumerate(self._dictionary[word], start=1):
            lines.append(f"{i}. {definition}")

        print(*lines, sep="\n")
        FileHandler.write_lines('query_history.txt', lines)

    def confirm_mutiple_words(self, words):
        num_of_words = len(words)

        if num_of_words == 0:
            return False
        elif num_of_words == 1:
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
                self.query_definition(word)
            except NoSuchWord as e:
                print(e)

class NoSuchWord(ValueError):
    def __init__(self):
        super().__init__("Word not found in the dictionary.")

def main():
    dictionary = Dictionary()
    try:
        dictionary.load_dictionary("")
    except FileExtensionNotSupported as e:
        print(e)
    except FileNotFoundError:
        print("No such file was found")
    else:
        dictionary.start_dictionary()
    finally:
        print("\nGoodBye")


if __name__ == "__main__":
    main()
