import abc


class AbstractFactory(abc.ABC):
    pass


class Factory(AbstractFactory):
    pass


class ChristmasFactory(Factory):
    pass


class HalloweenFactory(Factory):
    pass


class EasterFactory(Factory):
    pass


class ToyFactory(Factory):
    pass


class StuffedAnimalFactory(Factory):
    pass


class CandyFactory(Factory):
    pass
