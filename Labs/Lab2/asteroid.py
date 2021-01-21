import random
import vector


class Asteroid:
    __num_asteroids_created = 0

    def __init__(self, circumference, position: vector, velocity: vector):
        self._circumference = circumference
        self._position: vector = position
        self._velocity: vector = velocity
        self._asteroid_ID = Asteroid.generate_asteroid_id()


    def move(self):
        # old_position = self._position
        self._position.add(self._velocity)
        # print("Asteroid {0} Moved! Old Pos: {1} -> New Pos: {2}".format(
        #     self._asteroid_ID, old_position, self._position
        # ))
        return self._position.get_vector()

    def change_velocity(self, new_velocity):
        self._velocity = new_velocity

    @staticmethod
    def generate_asteroid_id():
        Asteroid.__num_asteroids_created += 1
        return Asteroid.__num_asteroids_created

    @classmethod
    def generate_asteroid_id2(cls):
        cls.__num_asteroids_created += 1
        return cls.__num_asteroids_created

    def __str__(self):
        return "Asteroid {0} is currently at {1} and moving at {2} meters per second. It has a circumference of {3}"\
            .format(self._asteroid_ID, self._position, self._velocity, self._circumference)
