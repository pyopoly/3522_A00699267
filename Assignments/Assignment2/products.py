"""
This module contains all the Products that the Store sells. For each festive season, the store stocks a unique toy.
There are three festive seasons (Christmas, Halloween, Easter) and three types of products (Toy, StuffedAnimal, Candy)
for each season, for a total of 9 Products.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

from enum import Enum, auto


class Product:
    """ Represents a Product. All Products have a unique ID, name, description. and the rest are stored in kwargs. """
    YES_OR_NO = "Y, N"

    def __init__(self, product_id, name, description, **kwargs):
        self._product_id = product_id
        self._name = name
        self._description = description

    def get_id(self):
        """
        Getter for Product_id
        :return: string
        """
        return self._product_id

    def __key(self):
        """
        The unique key for this Product, which an immutable tuple of the unique product_id
        :return: tuple(string)
        """
        return tuple(self._product_id)

    def __hash__(self):
        """
        Make Product hashable. This is needed so Product can be used as a key in a dictionary in Inventory.
        :return: hashed key which is a tuple of product_id
        """
        return hash(self.__key())

    def __eq__(self, other):
        """
        Defines how two Products are compared. They are compared by their defined keys, which are their
        product_ids.
        :param other: Product, another Product to be compared to this Product
        :return: boolean
        """
        if isinstance(other, Product):
            return self.__key() == other.__key()
        return NotImplemented

    def __str__(self):
        """ toString for the Name for the Product. """
        return f"{self._name}"

    id = property(get_id)


class Toy(Product):
    """
    Toy as a Product. Information regarding a Toy:
    • Whether the toy is battery operated or not.
    • The minimum recommended age of the child that the toy is safe for.
    """

    def __init__(self, product_id, name, description, min_age, has_batteries):
        """ Initialized the properties that all Toys have. """
        super().__init__(product_id, name, description)
        if has_batteries not in self.YES_OR_NO:
            raise InvalidDataError("Has batteries", self.YES_OR_NO)
        else:
            if has_batteries == "Y":
                self._battery_operated = True
            else:
                self._battery_operated = False

        if not isinstance(min_age, float):
            raise InvalidDataError("Minimum Age", "integer")
        else:
            self._recommended_age = int(min_age)


class SantasWorkshop(Toy):
    """
    Christmas Toy. Not battery operated.
    Unique properties:
    • dimensions (width and height),
    • The number of rooms.
    """

    def __init__(self, num_rooms, dimensions, has_batteries=False, **kwargs):
        super().__init__(kwargs['product_id'], kwargs["name"], kwargs['description'], kwargs['min_age'], has_batteries)
        try:
            dimensions = [int(x) for x in dimensions.split(",")]
        except ValueError:
            raise InvalidDataError("Dimensions", "integer")

        if self._battery_operated:
            raise InvalidDataError("Has batteries", "N")

        self._width = dimensions[0]
        self._height = dimensions[1]

        if not isinstance(num_rooms, float):
            raise InvalidDataError("Number of rooms", "Integer")
        else:
            self._number_of_rooms = int(num_rooms)


class RCSpider(Toy):
    """
    Halloween Toy. Battery operated.
    Unique properties:
    • Speed
    • Jump height
    • Some spiders glow in the dark, while others do not.
    • The type of spider - This can either be a Tarantula or a Wolf Spider and nothing else.
    """

    class SpiderType(Enum):
        """Two types of spiders."""
        Tarantula = auto()
        Wolf_Spider = auto()

    def __init__(self, speed, jump_height, has_glow, has_batteries=True, **kwargs):
        super().__init__(kwargs['product_id'], kwargs["name"], kwargs['description'], kwargs['min_age'], has_batteries)
        try:
            self._speed = float(speed)
        except ValueError:
            raise InvalidDataError("Speed", "integer or float")
        try:
            self._jump_height = float(jump_height)
        except ValueError:
            raise InvalidDataError("Height", "integer or float")

        if has_glow not in self.YES_OR_NO:
            raise InvalidDataError("Has glow", self.YES_OR_NO)
        else:
            if has_glow == "Y":
                self._glow_in_the_dark = True
            else:
                self._glow_in_the_dark = False

        try:
            self._type = self.SpiderType[kwargs['spider_type'].replace(' ', '_')]
        except KeyError:
            raise InvalidDataError("Spider Type", get_key_names_as_string(self.SpiderType))

        if not self._battery_operated:
            raise InvalidDataError("Has batteries", "Y")


class RobotBunny(Toy):
    """
    Easter Toy. Battery operated. For toddlers and infants.
    Unique properties:
    • The number of sound effects
    • The colour - This can be either Orange, Blue, or Pink and nothing else
    """

    class Colour(Enum):
        """ Only three types of colour are available. """
        Orange = auto()
        Blue = auto()
        Pink = auto()

    def __init__(self, num_sound, has_batteries=True, **kwargs):
        super().__init__(kwargs['product_id'], kwargs["name"], kwargs['description'], kwargs['min_age'], has_batteries)
        try:
            self._number_of_sound_effects = int(num_sound)
        except ValueError:
            raise InvalidDataError("Number of sounds", "integer")
        try:
            self._colour = self.Colour[kwargs['colour']]
        except KeyError:
            raise InvalidDataError("Colour", get_key_names_as_string(self.Colour))

        if not self._battery_operated:
            raise InvalidDataError("Has batteries", "Y")


class StuffedAnimal(Product):
    """
    Toy as a Product. Information regarding a Toy:
    • Stuffing - This can either be Polyester Fiberfill or Wool
    • Size - This can either be Small, Medium or Large
    • Fabric - This can either be Linen, Cotton or Acrylic
    """

    class Stuffing(Enum):
        """ Only two choices: Polyester Fibrefill or Wool. """
        Polyester_Fibrefill = auto()
        Wool = auto()

    class Size(Enum):
        """ Only three choices: Small, Medium or Large. """
        S = auto()
        M = auto()
        L = auto()

    class Fabric(Enum):
        """ Only three choices: Linen, Cotton or Acrylic """
        Linen = auto()
        Cotton = auto()
        Acrylic = auto()

    def __init__(self, **kwargs):
        """ Initializes the properties that all StuffedAnimals have. """
        super().__init__(**kwargs)

        try:
            self._stuffing = self.Stuffing[kwargs['stuffing'].replace(' ', '_')]
        except KeyError:
            raise InvalidDataError("Stuffing", get_key_names_as_string(self.Stuffing))

        try:
            self._size = self.Size[kwargs['size']]
        except KeyError:
            raise InvalidDataError("Size", get_key_names_as_string(self.Size))

        try:
            self._fabric = self.Fabric[kwargs['fabric']]
        except KeyError:
            raise InvalidDataError("Fabric", get_key_names_as_string(self.Fabric))


class DancingSkeleton(StuffedAnimal):
    """
    Halloween StuffedAnimal. This skeleton is sure to add to your Halloween decorations.
    • Fabric: Acrylic yarn.
    • Stuffing: Polyester Fiberfill
    • Glows in the dark.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self._stuffing != self.Stuffing.Polyester_Fibrefill:
            raise InvalidDataError("Stuffing", "Polyester Fibrefill")

        if self._fabric != self.Fabric.Acrylic:
            raise InvalidDataError("Fabric", "Acrylic Yarn")

        if kwargs['has_glow'] not in self.YES_OR_NO:
            raise InvalidDataError("Has Glow", self.YES_OR_NO)
        else:
            if kwargs['has_glow'] == "Y":
                self._glow_in_the_dark = True
            else:
                self._glow_in_the_dark = False
        # self._stuffing = super().Stuffing.Polyester_Fiberfill
        # self._fabric = super().Fabric.Acrylic


class Reindeer(StuffedAnimal):
    """
    Christmas StuffedAnimal. Comes with its very own personal mini sleigh.
    • Fabric: Cotton.
    • Stuffing: Wool.
    • has a glow in the dark nose.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self._stuffing != self.Stuffing.Wool:
            raise InvalidDataError("Stuffing", "Wool")

        if self._fabric != self.Fabric.Cotton:
            raise InvalidDataError("Fabric", "Cotton")

        if kwargs['has_glow'] not in self.YES_OR_NO:
            raise InvalidDataError("Has Glow", self.YES_OR_NO)
        else:
            if kwargs['has_glow'] == "Y":
                self._glow_in_the_dark = True
            else:
                self._glow_in_the_dark = False
        # self._stuffing = super().Stuffing.Wool
        # self._fabric = super().Fabric.Cotton


class EasterBunny(StuffedAnimal):
    """
    Easter StuffedAnimal. Comes with its very own personal mini sleigh.
    • Fabric: Linen.
    • Stuffing: Polyester Fiberfill.
    • Four colours: White, Grey, Pink and Blue.
    """

    class Colour(Enum):
        """ Only four types of colour are available. """
        White = auto()
        Grey = auto()
        Pink = auto()
        Blue = auto()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self._stuffing != self.Stuffing.Polyester_Fibrefill:
            raise InvalidDataError("Stuffing", "Polyester Fibrefill")

        if self._fabric != self.Fabric.Linen:
            raise InvalidDataError("Fabric", "Linen")

        try:
            self._colour = self.Colour[kwargs['colour']]
        except KeyError:
            raise InvalidDataError("Colour", get_key_names_as_string(self.Colour))
        # self._stuffing = super().Stuffing.Polyester_Fiberfill
        # self._fabric = super().Fabric.Linen


class Candy(Product):
    """
    All candies have the following properties:
    • If it contains any nuts
    • If it is lactose free.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if kwargs['has_nuts'] not in self.YES_OR_NO:
            raise InvalidDataError("Has Nuts", self.YES_OR_NO)
        else:
            if kwargs['has_nuts'] == "Y":
                self._contains_nuts = True
            else:
                self._contains_nuts = False

        if kwargs['has_lactose'] not in self.YES_OR_NO:
            raise InvalidDataError("Has Lactose", self.YES_OR_NO)
        else:
            if kwargs['has_lactose'] == "Y":
                self._has_lactose = True
            else:
                self._has_lactose = False


class PumpkinCaramelToffee(Candy):
    """
    Halloween Candy.
    • Has Lactose: True
    • Contains nuts: True
    • Two varieties: Sea Salt and Regular.
    """

    class Flavour(Enum):
        """ Can be one of these two varieties. """
        Sea_Salt = auto()
        Regular = auto()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self._flavour = self.Flavour[kwargs['variety'].replace(' ', '_')]
        except KeyError:
            raise InvalidDataError("Variety", get_key_names_as_string(self.Flavour))

        if not self._has_lactose:
            raise InvalidDataError("Has Lactose", "Y")

        if not self._contains_nuts:
            raise InvalidDataError("Has Nuts", "Y")

        # contains_nuts = True
        # lactose_free = False


class CandyCane(Candy):
    """
    Christmas Candy.
    • Has Lactose: False
    • Contains nuts: False
    • Strips colour: Red or Green
    """

    class Stripes(Enum):
        """ Stripes on the candy cane can either be Red or Green. """
        Red = auto()
        Green = auto()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self._stripes = self.Stripes[kwargs['colour']]
        except KeyError:
            raise InvalidDataError("Stripes", get_key_names_as_string(self.Stripes))
        # contains_nuts = False
        # lactose_free = True

        if self._has_lactose:
            raise InvalidDataError("Has Lactose", "N")

        if self._contains_nuts:
            raise InvalidDataError("Has Nuts", "N")


class CremeEgg(Candy):
    """
    Easter Candy.
    • Has Lactose: True
    • Contains nuts: True
    • Pack size: different numbers of creme eggs per pack
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self._pack_size = int(kwargs['pack_size'])
        except ValueError:
            raise InvalidDataError("Pack Size", "integer")
        # contains_nuts = True
        # lactose_free = False

        if not self._has_lactose:
            raise InvalidDataError("Has Lactose", "Y")

        if not self._contains_nuts:
            raise InvalidDataError("Has Nuts", "Y")


class InvalidDataError(Exception):
    """
    The InvalidDataError is an exception that should be raised
    when a product is provided with invalid data.
    """

    def __init__(self, detail_type, valid_data):
        """
        Instantiates the exception with the following message:
        "InvalidDataError - (type) can only be (valid_data)

        :param detail_type: type of data.
        :param valid_data: valid data type as a list.
        """
        super().__init__(f"Error! Invalid data type detected.", detail_type, valid_data)


def get_key_names_as_string(enum):
    """
    Gets the names of the keys in an enum class as a string.
    :return: string
    """
    names = ""
    for i in range(1, len(enum) + 1):
        name = enum(i).name
        name = name.replace("_", " ")
        names += name
        if i < len(enum):
            names += " or "

    return names
