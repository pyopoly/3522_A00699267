"""
This module contains the Asteroid class, which has a circumference, a position in 3D space,
and the velocity it is moving at.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import vector


class Asteroid:
    """
    This class represent an asteroid in a 3D space. The asteroid's position and velocity are represented by the
    Vector class, which has x, y, and z coordinates as attributes. Each time an asteroid is created, it is given
    an incrementing ID.
    """
    # Total numbers of all asteroids created.
    __num_asteroids_created = 0

    def __init__(self, circumference, position: vector.Vector, velocity: vector.Vector):
        """
        Initialize an asteroid. position and velocity are represented by the Vector class.
        Velocity is measured in meters per second.
        Each asteroid has an ID starting at 1, and increments by 1 each time a new asteroid is created.
        :param circumference: a positive float or int
        :param position: a Vector representing x, y, z coordinates
        :param velocity: a Vector representing x, y, z coordinates
        """
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self._asteroid_ID = Asteroid._generate_asteroid_id()

    def move(self):
        """
        Move the asteroid by 1 second. New position is calculated base on adding the velocity to the current position.
        :return: the new position as a tuple
        """
        old_pos = vector.Vector.copy(self._position)
        self._position.add(self._velocity)
        print("Asteroid {0} Moved! Old Pos: {1} -> New Pos: {2}".format(
            self._asteroid_ID, old_pos, self._position
        ))
        return self._position.get_vector()

    def change_velocity(self, new_velocity: vector.Vector):
        """
        Change the velocity of the asteroid.
        :param new_velocity: a Vector
        """
        self._velocity = new_velocity

    def get_id(self):
        """
        Returns the ID of this asteroid.
        :return: an int indicating the ID
        """
        return self._asteroid_ID

    @classmethod
    def _generate_asteroid_id(cls):
        """
        Increments the global variable: num_asteroids_created by 1. And returns the newly incremented number.
        Used to give a unique ID to each asteroid.
        :return:
        """
        cls.__num_asteroids_created += 1
        return cls.__num_asteroids_created

    def __str__(self):
        """
        ToString.
        :return: User-friendly formatted String that depicts the asteroid's attributes.
        """
        return "Asteroid {0} is currently at {1} and moving at {2} meters per second. It has a circumference of {3}"\
            .format(self._asteroid_ID, self._position, self._velocity, self._circumference)
