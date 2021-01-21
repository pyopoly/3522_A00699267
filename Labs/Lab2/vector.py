"""
This module is a helper module for Asteroid class. The vector class represents the position or velocity within
a 3D space.
"""

__author__ = "Jack Shih"
__version__ = "Jan 2021"

import random


class Vector:
    """This class represents a vector with x, y, z coordinates that indicates a position in a 3D space"""

    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        """
        Initialize the vector with the x, y, z coordinates.
        :param x_coordinate: an int for x
        :param y_coordinate: an int for y
        :param z_coordinate: an int for z
        """
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._z_coordinate = z_coordinate

    @classmethod
    def random_init(cls, x_range, y_range, z_range):
        """
        Additional init method. The upper bound (inclusive) is given for each coordinate, and a randomly generated
        vector is initialized with 0 as the lower bound (inclusive).
        :param x_range: an int for x upper bound
        :param y_range: an int for y upper bound
        :param z_range: an int for z upper bound
        :return: a Vector with randomly generated coordinates
        """
        x_coordinate = random.randint(0, x_range)
        y_coordinate = random.randint(0, y_range)
        z_coordinate = random.randint(0, z_range)
        return cls(x_coordinate, y_coordinate, z_coordinate)

    def add(self, vector):
        """
        Increase the coordinates of a vector by adding another vector to it. X-coordinate is summed with X-coordinate,
        and so on.
        :param vector: a vector to be added
        """
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def get_vector(self):
        """
        Returns the x, y, z coordinates of the vector as a tuple.
        :return: a tuple representing the x, y, z coordinates
        """
        return self.x, self.y, self.z

    def __str__(self):
        """
        ToString method.
        :return: a user-friendly formatted string depicting the x, y, z coordinates
        """
        return "This vector has x, y, z coordinates: ({0}, {1}, {2}).".format(
            self.x, self.y, self.z)

    def set_x(self, x):
        """
        Setter for the x-coordinate.
        :param x: an int for x
        """
        self._x_coordinate = x

    def set_y(self, y):
        """
        Setter for the y-coordinate.
        :param y: an int for y
        """
        self._y_coordinate = y

    def set_z(self, z):
        """
        Setter for the z-coordinate.
        :param z: an int for z
        :return:
        """
        self._z_coordinate = z

    def get_x(self):
        """
        Getter for x-coordinate.
        :return: x as an int
        """
        return self._x_coordinate

    def get_y(self):
        """
        Getter for y-coordinate.
        :return: y as an int
        """
        return self._y_coordinate

    def get_z(self):
        """
        Getter for z-coordinate.
        :return: z as an int
        """
        return self._z_coordinate

    x = property(get_x, set_x, None, "property to get x-coordinate of the vector")
    y = property(get_y, set_y, None, "property to get y-coordinate of the vector")
    z = property(get_z, set_z, None, "property to get z-coordinate of the vector")
