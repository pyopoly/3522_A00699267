"""This module represents a vector with x, y, z coordinates."""

import random

class Vector:
    """This class."""

    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._z_coordinate = z_coordinate

    @classmethod
    def random_init(cls, x_range, y_range, z_range):
        x_coordinate = random.randint(0, x_range)
        y_coordinate = random.randint(0, y_range)
        z_coordinate = random.randint(0, z_range)
        return cls(x_coordinate, y_coordinate, z_coordinate)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def get_vector(self):
        return self.x, self.y, self.z

    def __str__(self):
        return "This vector has x, y, z coordinates: ({0}, {1}, {2}).".format(
            self.x, self.y, self.z)

    def set_x(self, x):
        self._x_coordinate = x

    def set_y(self, y):
        self._y_coordinate = y

    def set_z(self, z):
        self._z_coordinate = z

    def get_x(self):
        return self._x_coordinate

    def get_y(self):
        return self._y_coordinate

    def get_z(self):
        return self._z_coordinate

    x = property(get_x, set_x)

    y = property(get_y, set_y)

    z = property(get_z, set_z)


print("hi")
one = Vector(1, 2, 3)
print(one)
two = Vector(10, 20, 30)
one.add(two)
print(one)
v = one.get_vector()
print(v)
print(type(v))
print(two)
