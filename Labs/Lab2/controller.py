import random
import datetime
import math
import asteroid
import vector


class Controller:

    def __init__(self, num_asteroids):
        self._list_of_asteroids = []
        for x in range(num_asteroids):
            radius = random.randint(1, 4)
            circumference = self.__calculate_circumference(radius)
            start_pos = vector.Vector.random_init(99, 99, 99)
            start_velocity = vector.Vector.random_init(5, 5, 5)
            new_asteroid = asteroid.Asteroid(circumference, start_pos, start_velocity)
            self._list_of_asteroids.append(new_asteroid)

    def simulate(self, seconds):
        for x in range(seconds):
            for y in self._list_of_asteroids:
                y.move()

    def __calculate_circumference(self, radius):
        return 2 * math.pi * radius
