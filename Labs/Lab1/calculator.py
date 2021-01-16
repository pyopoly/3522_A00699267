"""
Calculator module that does calculation based on user's two inputs.

Calculator module with functions for summing, multiplying, dividing,
subtracting and finding the hypotenuse of two arguments.
"""

__author__ = "Jack Shih"
__version__ = "Winter 2021"

import hypotenuse


def sum(a, b):
    """
    Finds the sum of the two arguments.
    :param a: an int or float
    :param b: an int or float
    :return: the sum of a and b
    """
    return a + b


def multiply(a, b):
    """
    Finds the product of the two arguments.
    :param a: an int or float
    :param b: an int or float
    :return: the product of a and b
    """
    return a * b


def divide(a, b):
    """
    Finds the quotient of the two arguments.

    Error is given if user tries to divide a by 0 (b is zero).
    :param a: an int or float, the dividend
    :param b: an int or float, the divisor
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the quotient of a and b
    """
    while b == 0:
        b = int(input("divisor cannot be 0, enter new number: "))
    return a / b


def subtract(a, b):
    """
    Finds the difference of the two arguments.
    :param a: an int or float
    :param b: an int or float
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the different of a and b
    """
    return a - b


def main():
    """
    Calculates and prints out the result based on the user's choice and inputs.

    User chooses from finding the hypotenuse, addition, subtraction, multiplication, or division, and
    the result is calculated and printed out.
    :precondition: inputs must be ints or floats
    :return: none
    """
    print("Choose your desired operator:")
    print("1 to calculate hypotenuse \n"
          "2 to add \n"
          "3 to subtract \n"
          "4 to multiply \n"
          "5 to divide")

    user_input = input("your choice: ")

    # check if input is an int from 1 to 5.
    while not user_input.isnumeric() or int(user_input) > 5 or int(user_input) < 1:
        print("\ninvalid choice")
        user_input = input("your choice: ")
    choice = int(user_input)

    a = float(input("enter first number: "))
    b = float(input("enter second number: "))

    # switch case using dictionary
    switcher = {
        1: hypotenuse.calculate_hypotenuse(a, b),
        2: sum(a, b),
        3: subtract(a, b),
        4: multiply(a, b),
        5: divide(a, b)
    }
    answer = switcher.get(choice, "invalid")
    print("answer: {0}".format(round(answer, 2)))


if __name__ == "__main__":
    main()
