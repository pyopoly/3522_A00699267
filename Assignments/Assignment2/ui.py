class UI:

    def menu(self):
        print("1. Process Web Orders\n"
              "2. Check Inventory\n"
              "3. Exit")
        prompt = "Enter your choice: "
        choice = UI.get_valid_input(prompt, 3)

        switch = {
            1: "choice1",
            2: "choice2",
            3: "choice3"
        }

        result = switch.get(choice)
        print(result)

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


ui = UI()
ui.menu()
