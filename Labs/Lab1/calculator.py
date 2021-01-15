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
    :param a: an int
    :param b: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the sum of a and b
    """
    return a + b


def multiply(a, b):
    """
    Finds the product of the two arguments.
    :param a: an int
    :param b: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the product of a and b
    """
    return a * b


def divide(a, b):
    """
    Finds the quotient of the two arguments.
    :param a: an int, the dividend
    :param b: an int, the divisor
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the quotient of a and b
    """
    return a / b


def subtract(a, b):
    """
    Finds the difference of the two arguments.
    :param a: an int
    :param b: an int
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
    :precondition: inputs must be ints
    :return: none
    """
    print("Choose your desired operator:")
    print("1 to calculate hypotenuse \n"
          "2 to add \n"
          "3 to subtract \n"
          "4 to multiply \n"
          "5 to divide")

    choice = int(input("your choice: "))
    while choice > 5 or choice < 1:
        print("\ninvalid choice")
        choice = int(input("your choice: "))

    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    switcher = {
        1: hypotenuse.calculate_hypotenuse(a, b),
        2: sum(a, b),
        3: subtract(a, b),
        4: multiply(a, b),
        5: divide(a, b)
    }
    answer = switcher.get(choice, "invalid")
    print("answer: {0} ".format(round(answer, 2)))


if __name__ == "__main__":
    main()
