import abc
from abc import ABC
from enum import Enum, auto


class Toy:
    battery_operated = None
    recommended_age = 0


class SantaWorkshop(Toy):
    battery_operated = False
    width = 0
    height = 0
    number_of_rooms = 0


class RCSpider(Toy):
    class SpiderType(Enum):
        Tarantula = auto()
        Wolf_Spider = auto()

    battery_operated = True
    speed = 0
    jump_height = 0
    glow_in_dark = False
    type = SpiderType


class RobotBunny(Toy):
    class Colour(Enum):
        Orange = auto()
        Blue = auto()
        Pink = auto()

    battery_operated = True
    number_of_sound_effects = 0
    colour = Colour


class StuffedAnimal:
    class Stuffing(Enum):
        Polyester_Fiberfill = auto()
        Wool = auto()

    class Size(Enum):
        small = auto()
        medium = auto()
        large = auto()

    class Fabric(Enum):
        Linen = auto()
        Cotton = auto()
        Acrylic = auto()

    stuffing = Stuffing
    size = Size
    fabric = Fabric


class DancingSkeleton(StuffedAnimal):
    def __init__(self):
        self._stuffing = super().Stuffing.Polyester_Fiberfill
        self._fabric = super().Fabric.Acrylic
        self._glow_in_dark = True


class Reindeer(StuffedAnimal):
    def __init__(self):
        self._stuffing = super().Stuffing.Wool
        self._fabric = super().Fabric.Cotton


#     glow in dark?


class EasterBunny(StuffedAnimal):
    class Colour(Enum):
        White = auto()
        Grey = auto()
        Pink = auto()
        Blue = auto()

    def __init__(self):
        self._stuffing = super().Stuffing.Polyester_Fiberfill
        self._fabric = super().Fabric.Linen
        self._colour = EasterBunny.Colour


class Candy:
    contains_nuts = False
    lactose_free = False


class PumpkinCaramelToffee(Candy):
    class Flavour(Enum):
        Sea_Salt = auto()
        Regular = auto()

    contains_nuts = True
    lactose_free = False
    flavour = Flavour


class CandyCane(Candy):
    class Stripes(Enum):
        Red = auto()
        Green = auto()

    contains_nuts = False
    lactose_free = True
    stripes = Stripes


class CremeEgg(Candy):
    contains_nuts = True
    lactose_free = False
    pack_size = 0


class ProductType(Enum):
    Toy = auto()
    StuffedAnimal = auto()
    Candy = auto()


class ProductName(Enum):
    Santa_Workshop = auto()
    RC_Spider = auto()
    Robot_Bunny = auto()


class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_item(self, item_type):
        pass


class Factory(AbstractFactory, ABC):
    pass


class ChristmasFactory(Factory):
    def create_item(self, item_type):
        d = {
            ProductType.Toy: SantaWorkshop,
            ProductType.StuffedAnimal: Reindeer,
            ProductType.Candy: CandyCane
        }
        item_type = ProductType[item_type]
        return d[item_type]()

class HalloweenFactory(Factory):
    def create_item(self, item_type):
        d = {
            ProductType.Toy: RCSpider,
            ProductType.StuffedAnimal: DancingSkeleton,
            ProductType.Candy: PumpkinCaramelToffee
        }


class EasterFactory(Factory):
    def create_item(self, item_type):
        d = {
            ProductType.Toy: RobotBunny,
            ProductType.StuffedAnimal: EasterBunny,
            ProductType.Candy: CremeEgg
        }


class ToyFactory(Factory):
    pass


class StuffedAnimalFactory(Factory):
    pass


class CandyFactory(Factory):
    pass


class Product:
    # product_id = None
    # name = "Product Name"
    # description = "Product Description"
    # stock = 0

    def __init__(self):
        self._product_id = None
        self._name = "Product Name"
        self._description = "Product Description"
        self._stock = 0

    def get_stock(self):
        return self._stock

    def set_stock(self, amount):
        self._stock = amount

    stock = property(get_stock, set_stock)
