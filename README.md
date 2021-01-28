# 3522_A00699267
BCIT_COMP3522_Projects_JackShih

BCIT Winter 2021\
Comp 3522\
author: Jack Shih

-------------------------------------------------
Lab1: \
Summary: A simple program that make calculations based on the user's selection. \
\
hypotenuse.py calculates contains one function that calculates the hypotenuse from two arguments.
calculator.py imports hypotenuse.py, and contains 4 additional calculation functions: addition, subtraction, multiplication, and division.
\
calculator.py prompts user to choose which calculation they want to perform, and asks for two inputs.
The answer is then calculated and printed out.

-------------------------------------------------
Lab2: \
Summary: Asteroids are created in a cube of 100 metres per side. Each asteroid has a randomly generated circumference, position, and velocity (metre/second). Controller contains a list of all asteroids and simulate their movements. \
\
vector.py : Helper class for asteroid.py. Vector contains attributes that represent x, y, z coordinates for an asteroid.\
asteroid.py : Asteroid moves every second. Each asteroid has a unique ID.\
controller.py : Controller contains all asteroids and runs the simulation.\
driver.py : Driver for the program.

-------------------------------------------------
Lab3: \
Summary: An implementation of a Library. User can view, check out, return, remove, add new library items. The point of this is to designate tasks to different classes based on OOP.
\
library.py : Main class. Represent the Library. Contains a simple user UI menu. Has a Catalogue. \
catalogue.py : Contains a list of LibraryItems. Performs backend work on managing the LibraryItems. \
library_item.py : Items in the Library. LibraryItem is the parent class. Book, DVD, and Journal are subclasses. \
library_item_generator.py : Helper class for Catalogue. Produces a menu for user to choose which type of LibraryItem to add.

-------------------------------------------------