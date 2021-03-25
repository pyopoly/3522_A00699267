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

    def print_check_out_result(self, result, call_number, item_type, title):
        if result:
            print(f"Checkout complete for {item_type}: '{title}'!")
        elif result is False:
            print(f"No copies left for call number {call_number}. Checkout failed.")
        else:
            print(f"Could not find item with call number {call_number}. Checkout failed.")

    def print_return_item_result(self, result, call_number, item_type, title):
        if result:
            print(f"{item_type}: '{title}' returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}. Return failed.")

    def print_remove_item_result(self, result, call_number, title):
        if result:
            print(f"Successfully removed {title} with call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")
