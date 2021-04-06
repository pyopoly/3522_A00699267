import city_processor
from threading import Thread
import time


class CityOverheadTimeQueue:
    def __init__(self):
        self._data_queue = []

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        This method is responsible for adding to the queue. Accepts a overhead_time parameter and appends
        it to the list.
        :param overhead_time: CityOverHeadTimes
        :return: None
        """
        self._data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        """
        This method is responsible for removing an element from a Queue. Remember a queue is a FIFO data structure,
        that is it is First In First Out. Each call to this method should return the element at index 0 and delete
        it from the list. Use the 'del' keyword to delete the element as this will also automatically move all
        the other elements so there will be no empty spaces.
        :return:
        """
        overhead_times = self._data_queue[0]
        del self._data_queue[0]
        return overhead_times

    def __len__(self) -> int:
        """
        Returns the length of the data queue.
        :return: int
        """
        return len(self._data_queue)


class ProducerThread(Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        """
        This method initializes the class with a list of City Objects as well as a CityOverheadTimeQueue.
        :param cities: list(City)
        :param queue: CityOverheadTimeQueue
        :return: None
        """
        super().__init__()
        self._cities = cities
        self._overhead_queue = queue

    def run(self) -> None:
        """
        This method executes when the thread starts. It should loop over each City and pass it to the
        ISSDataRequest.get_overheadpass() method. It then proceeds to add the city to the queue.
        After reading in 5 cities, the thread should sleep for 1 second.
        :return:
        """
        for i, city in enumerate(self._cities, start=1):
            overhead_time = city_processor.ISSDataRequest.get_overhead_pass(city)
            self._overhead_queue.put(overhead_time)
            if i == 5:
                time.sleep(1)


class ConsumerThread(Thread):
    """
    The ConsumerThread is responsible for consuming data from the queue and printing it out to the console.
    """
    def __init__(self, queue: CityOverheadTimeQueue):
        """
        Initializes the ConsumerThread with the same queue as the one the producer has. It also implements a
        data_incoming boolean attribute that is set to True. This attribute should change to False after the
        producer thread has joined the main thread and finished processing all the cities.
        :param queue: CityOverheadTimeQueue
        :return: None
        """
        super().__init__()
        self._queue = queue
        self.data_incoming = True

    def run(self) -> None:
        """
        While data_incoming is true OR the length of the queue is > 0, this method should get an item from the
        queue and print it to the console and then sleep for 0.5 seconds. While processing the queue, if the
        queue is empty, put the thread to sleep for 0.75 seconds.
        :return: None
        """
        while self.data_incoming or len(self._queue):
            if not self._queue:
                time.sleep(0.75)
            print(self._queue.get())
            time.sleep(0.5)



def main():
    city_db = city_processor.CityDatabase("city_locations_test.xlsx")
    overhead_time_queue = CityOverheadTimeQueue()

    # DEBUG CityOverheadTimeQueue
    # for city in city_db.city_db:
    #     overhead_time = city_processor.ISSDataRequest.get_overhead_pass(city)
    #     overhead_time_queue.put(overhead_time)
    #
    # print(len(overhead_time_queue))
    # for i in range(len(overhead_time_queue)):
    #     overhead_time = overhead_time_queue.get()
    #     print(overhead_time)
    #     print()
    # print(len(overhead_time_queue))

    # DEBUG ProducerThread ConsumerThread
    producer = ProducerThread(city_db.city_db, overhead_time_queue)
    consumer = ConsumerThread(overhead_time_queue)
    producer.start()
    consumer.start()
    producer.join()
    print("Producer finished")
    consumer.data_incoming = False
    consumer.join()


if __name__ == "__main__":
    main()
