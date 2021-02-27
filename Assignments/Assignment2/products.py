from enum import Enum, auto


class ProductType(Enum):
    Toy = auto()
    StuffedAnimal = auto()
    Candy = auto()


class ProductName(Enum):
    Santa_Workshop = auto()
    RC_Spider = auto()
    Robot_Bunny = auto()


class Product:
    def __init__(self, product_id, name, description, **kwargs):
        self._product_id = product_id
        self._name = name
        self._description = description

    # class Product:
    #     def __init__(self, **kwargs):
    #         self._product_id = kwargs['product_id']
    #         self._name = kwargs['name']
    #         self._description = kwargs['description']

    # def get_stock(self):
    #     return self._stock
    #
    # def set_stock(self, amount):
    #     self._stock = amount

    def get_id(self):
        return self._product_id

    # def __key(self):
    #     return self._product_id

    # def __eq__(self, other):
    #     if isinstance(other, Product):
    #         return self._product_id == other.id

    # stock = property(get_stock, set_stock)
    id = property(get_id)


class Toy(Product):
    def __init__(self, product_id, name, description, min_age, has_batteries):
        super().__init__(product_id, name, description)
        # self._battery_operated = has_batteries == "Y"
        self._battery_operated = has_batteries
        self._recommended_age = min_age


class SantasWorkshop(Toy):
    # def __init__(self, product_id, name, description, min_age, num_rooms, dimensions, has_batteries=False):
    def __init__(self, num_rooms, dimensions, has_batteries=False, **kwargs):
        super().__init__(kwargs['product_id'], kwargs["name"], kwargs['description'], kwargs['min_age'], has_batteries)
        dimensions = [int(x) for x in dimensions.split(",")]
        self._width = dimensions[0]
        self._height = dimensions[1]
        self._number_of_rooms = num_rooms


class RCSpider(Toy):
    class SpiderType(Enum):
        Tarantula = auto()
        Wolf_Spider = auto()

    def __init__(self, speed, jump_height, has_glow, has_batteries=True, **kwargs):
        super().__init__(kwargs['product_id'], kwargs["name"], kwargs['description'], kwargs['min_age'], has_batteries)
        self._speed = speed
        self._jump_height = jump_height
        self._glow_in_dark = has_glow
        self._type = self.SpiderType[kwargs['spider_type'].replace(' ', '_')]


class RobotBunny(Toy):
    class Colour(Enum):
        Orange = auto()
        Blue = auto()
        Pink = auto()

    def __init__(self, num_sound, has_batteries=True, **kwargs):
        super().__init__(kwargs['product_id'], kwargs["name"], kwargs['description'], kwargs['min_age'], has_batteries)
        # self._battery_operated = True
        self._number_of_sound_effects = num_sound
        self._colour = self.Colour[kwargs['colour']]


class StuffedAnimal(Product):
    class Stuffing(Enum):
        Polyester_Fibrefill = auto()
        Wool = auto()

    class Size(Enum):
        S = auto()
        M = auto()
        L = auto()

    class Fabric(Enum):
        Linen = auto()
        Cotton = auto()
        Acrylic = auto()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._stuffing = self.Stuffing[kwargs['stuffing'].replace(' ', '_')]
        self._size = self.Size[kwargs['size']]
        self._fabric = self.Fabric[kwargs['fabric']]


class DancingSkeleton(StuffedAnimal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self._stuffing = super().Stuffing.Polyester_Fiberfill
        # self._fabric = super().Fabric.Acrylic
        self._glow_in_dark = kwargs['has_glow']


class Reindeer(StuffedAnimal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self._stuffing = super().Stuffing.Wool
        # self._fabric = super().Fabric.Cotton
        self._glow_in_dark = kwargs['has_glow']


class EasterBunny(StuffedAnimal):
    class Colour(Enum):
        White = auto()
        Grey = auto()
        Pink = auto()
        Blue = auto()

    def __init__(self, **kwargs):
        # print("xxxxx super", super())
        super().__init__(**kwargs)

        # self._stuffing = super().Stuffing.Polyester_Fiberfill
        # self._fabric = super().Fabric.Linen
        # super().__init__(product_id, name, description, **kwargs)
        self._colour = EasterBunny.Colour[kwargs['colour']]


class Candy(Product):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._contains_nuts = kwargs['has_nuts']
        self._lactose_free = kwargs['has_lactose']


class PumpkinCaramelToffee(Candy):
    class Flavour(Enum):
        Sea_Salt = auto()
        Regular = auto()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # contains_nuts = True
        # lactose_free = False
        self._flavour = self.Flavour[kwargs['variety'].replace(' ', '_')]


class CandyCane(Candy):
    class Stripes(Enum):
        Red = auto()
        Green = auto()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # contains_nuts = False
        # lactose_free = True
        self._stripes = self.Stripes[kwargs['colour']]


class CremeEgg(Candy):
    # contains_nuts = True
    # lactose_free = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._pack_size = kwargs['pack_size']

# x = SantasWorkshop(product_id=10, num_rooms=10, name="S", min_age=5, description="s", dimensions="1,2")
# z = {x: 10}
