"""
This module is used as control centre for the asteroids. Asteroids are created and their movements are simulated by
the class Controller.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import random
import math
import asteroid
import vector
import time
import datetime


class Controller:
    """ This class simulates movements of asteroids in a cube that is 100 metres per side. """

    def __init__(self, num_asteroids):
        """
        Asteroids are stored in a list. Asteroids have randomly generated attributes.
        Asteroids have random radius of 1 to 4.
        Asteroids have random velocity of 0 to 5 metres per second.
        :param num_asteroids: an int for total number of asteroids
        :precondition: num_asteroids must be an int greater than 0
        """
        self._list_of_asteroids = []
        for x in range(num_asteroids):
            radius = random.randint(1, 4)
            circumference = self.__calculate_circumference(radius)
            start_pos = vector.Vector.random_init(99, 99, 99)
            start_velocity = vector.Vector.random_init(5, 5, 5)
            new_asteroid = asteroid.Asteroid(circumference, start_pos, start_velocity)
            self._list_of_asteroids.append(new_asteroid)

    def simulate(self, seconds):
        """
        Simulate movements of asteroids by their velocity and position. Each movement happens 'on the second' of the
        system time. Asteroids move one by one by their velocity every second for the duration of the simulation.
        :param seconds: an int for how many total seconds the simulation is run
        :return: none
        """
        index = 0
        while seconds > 0:
            # sleep for the difference in reaching the next whole second.
            # time % 1 to get the time that is less than one second
            # 1 - above, to get the difference
            time.sleep(1 - (time.time() % 1))

            # print(datetime.datetime.fromtimestamp(time.time()))
            self._list_of_asteroids[index].move()  # move asteroid
            print(self._list_of_asteroids[index])  # print the status of asteroid that moved

            seconds -= 1  # seconds countdown to 0
            index += 1  # index increments by 1
            # restart index to 0 when it reaches end of the list of asteroids
            if index == len(self._list_of_asteroids):
                index = 0

    def __calculate_circumference(self, radius):
        """
        Helper method to calculate circumference from radius.
        :param radius: an int, or a float
        :return: a float as the circumference
        """
        return 2 * math.pi * radius
