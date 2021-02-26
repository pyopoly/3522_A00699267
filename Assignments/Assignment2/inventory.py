from enum import Enum, auto


class ProductType(Enum):
    Toy = auto()
    Stuffed_Animal = auto()
    Candy = auto()


class ProductName(Enum):
    Santa_Workshop = auto()
    RC_Spider = auto()
    Robot_Bunny = auto()


class Inventory:
    def __init__(self):
        self._products = []


    def check_item_in_inventory(self, order):
        id = order.product_id
        amount = order.quantity_required()
        if self.item_in_inventory(id):
            if self.enough_stock(id, amount):
                self.reduce_stock(id, amount)
            else:
                self.replenish_stock_by_100(id)
            # reduce stock
        else:
            # product = self[id]
            # make new item from order
            self.purchase_100_item(order)
            # purchase stock

    def __contains__(self, product_id):
        for product in self._products:
            if product.product_id == product_id:
                return True
        return False

    def __getitem__(self, product_id):
        for product in self._products:
            if product.product_id == product_id:
                return product
        else:
            return None

    def item_in_inventory(self, product_id):
        return product_id in Inventory

    def enough_stock(self, product_id, amount):
        product = self[product_id]
        return amount <= product.stock

    def reduce_stock(self, product_id, amount):
        self[product_id].reduce_stock(amount)

    def replenish_stock_by_100(self, order):
        self[product_id].stock += 100


    def purchase_100_item(self, product):
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
