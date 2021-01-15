"""
Calculates the hypotenuse from user's two inputs.
"""

__author__ = "Jack Shih"
__version__ = "Winter 2021"

import math


def calculate_hypotenuse(a, b):
    """
    Calculates the hypotenuse using the two arguments.
    :param a: an int
    :param b: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the hypotenuse of a and b
    """
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return hypotenuse


def main():
    """
    Prints out the hypotenuse from the user's inputs.
    :precondition: inputs must be ints
    :return: none
    """
    print("Please enter two values to calculate the hypotenuse")
    a = int(input("1st value: "))
    b = int(input("2nd value: "))
    print(f"The hypotenuse of {a} and {b} is: {calculate_hypotenuse(a, b):.2f}")


if __name__ == "__main__":
    main()
