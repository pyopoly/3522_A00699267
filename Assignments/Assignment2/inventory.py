from enum import Enum, auto


class ProductType(Enum):
    Toy = auto()
    Stuffed_Animal = auto()
    Candy = auto()


class ProductName(Enum):
    Santa_Workshop = auto()
    RC_Spider = auto()
    Robot_Bunny = auto()


class Product:
    productID = None
    name = "Product Name"
    description = "Product Description"
    stock = 0


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
    stuffing = super().Stuffing.Polyester_Fiberfill
    fabric = super().Fabric.Acrylic
    glow_in_dark = True


class Reindeer(StuffedAnimal):
    stuffing = super().Stuffing.Wool
    fabric = super().Fabric.Cotton
#     glow in dark?


class EasterBunny(StuffedAnimal):
    class Colour(Enum):
        White = auto()
        Grey = auto()
        Pink = auto()
        Blue = auto()
    stuffing = super().Stuffing.Polyester_Fiberfill
    fabric = super().Fabric.Linen
    colour = Colour


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
