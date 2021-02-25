import abc


class AbstractFactory(abc.ABC):
    pass


class Factory(AbstractFactory):
    pass


class ToyFactory(Factory):
    pass


class StuffedAnimalFactory(Factory):
    pass


class CandyFactory(Factory):
    pass
