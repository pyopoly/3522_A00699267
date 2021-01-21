"""
This module is a driver module for asteroid.py and controller.py.
Controller creates asteroids and oversees the activity of these asteroids.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import controller
import time
import datetime


def main():
    """
    Main method. Runs simulation of 100 asteroids for 20 seconds.
    Current time at which the simulation is run is printed.
    :return: none
    """
    galaxy = controller.Controller(100)
    print("Simulation Start Time: {0}\n".format(datetime.datetime.fromtimestamp(time.time())))
    print("Moving Asteroids!")
    print("-----------------")
    galaxy.simulate(20)


if __name__ == '__main__':
    main()
