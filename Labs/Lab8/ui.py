class ConsoleUI:
    def get_call_num(self):
        return input("Please enter the call number of the item: ")

    def get_title(self):
        return input("Please enter the title of the item: ")

    def pause(self):
        return input("Press Enter to continue")

    def good_bye_phrase(self):
        print("Thank you for visiting the Library.")

    def main_menu(self):
        print("\nWelcome to the Library!")
        print("-----------------------")
        print("1. Display all items")
        print("2. Check Out a item")
        print("3. Return a item")
        print("4. Find a item")
        print("5. Add a item")
        print("6. Remove a item")
        print("7. Quit")
        while True:
            string_input = input("Please enter your choice (1-7): ")
            if string_input != '':
                break
        return int(string_input)

    def display_all_items(self, items):
        print("items List \n--------------", end="\n")
        list(map(lambda item: print(item, "\n"), items))
