class UI:

    def __init__(self, store):
        self._store = store

    def menu(self):
        while True:
            print("1. Process Web Orders\n"
                  "2. Check Inventory\n"
                  "3. Exit")
            prompt = "Enter your choice: "
            choice = UI.get_valid_input(prompt, 3)

            switch = {
                1: self.process_orders,
                2: self.print_inventory,
                3: exit
            }

            switch.get(choice)(self._store)
            input("Press Enter to continue ")

    def process_orders(self, store):
        store.process_orders()

    def print_inventory(self, store):
        inventory = store.get_inventory()

        for i, (product, stock) in enumerate(inventory, start=1):
            print("{:3}  {:50} stock: {}".format(i, str(product), stock))

    @staticmethod
    def get_valid_input(prompt, num_of_choices):
        """
        Get input from User. Also valid the input and re-prompt the user if input is invalid.
        Number of choices is the desired number of choices required of the user. Anything that is
        not an int in the range of 1 to num_of_choices inclusive will be invalid.
        :param prompt: a string msg. To show the user to prompt for their input
        :param num_of_choices: int. Total number of choices expected from this prompt.
        :return: int, the user's choice
        """
        str_input = input(prompt)
        warning = f"Please enter a number (1-{num_of_choices}): "
        while True:
            if str_input.isnumeric():
                choice = int(str_input)
                if choice in range(1, num_of_choices + 1):
                    break
            str_input = input(warning)
        return choice

    @staticmethod
    def get_valid_string_input(prompt):
        while True:
            string_input = input(prompt)
            if string_input.strip() == '':
                print("\n----Please do not leave this empty----")
            else:
                return string_input
