import random
import datetime
import math
import asteroid
import vector
import time
import datetime

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

        index = 0
        while seconds > 0 and (time.time() %1) == 0:
            # time.sleep(1-(time.time() % 1))
            print(datetime.datetime.fromtimestamp(time.time()))
            self._list_of_asteroids[index].move()
            # time.sleep(1)
            print(self._list_of_asteroids[index]._asteroid_ID)
            seconds -= 1
            index += 1
            if index == len(self._list_of_asteroids):
                index = 0


    def __calculate_circumference(self, radius):
        return 2 * math.pi * radius
ccc = Controller(10)
ccc.simulate(25)

start_time = time.time()
start_time = datetime.datetime.fromtimestamp(start_time)

print("Simulation start time: {0}".format(start_time))
delta = datetime.datetime(start_time.year, start_time.month, start_time.day, start_time.hour,
                          start_time.minute, start_time.second)
delta = start_time - delta
print(datetime.datetime.timestamp(start_time))
print(time.time())
print(1- (time.time() % 1))