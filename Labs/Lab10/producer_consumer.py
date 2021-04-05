import city_processor


class CityOverheadTimeQueue:
    def __int__(self):
        self._data_queue = []

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        This method is responsible for adding to the queue. Accepts a parameter and appends it to the list.
        :param overhead_time: CityOverHeadTimes
        :return: None
        """
        self._data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        """
        This method is responsible for removing an element from a Queue. Remember a queue is a FIFO data structure,
        that is it is First In First Out. Each call to this method should return the element at index 0 and delete
        it from the list. Use the keyword to delete the element as this will also automatically move all
        the other elements so there will be no empty spaces.
        :return:
        """
        pass

    def __len__(self) -> int:
        """
        Returns the length of the data queue.
        :return: int
        """
        return len(self._data_queue)


def main():
    pass


if __name__ == "__main__":
    main()
