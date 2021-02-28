import abc
from products import *


class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_item(self, order):
        pass


class Factory(AbstractFactory, abc.ABC):
    pass

    @staticmethod
    def get_factory(order):
        return order.factory()


class ChristmasFactory(Factory):
    def create_item(self, order):
        switch = {
            ProductType.Toy: SantasWorkshop,
            ProductType.StuffedAnimal: Reindeer,
            ProductType.Candy: CandyCane
        }
        item_type = ProductType[order.item_type]
        return switch[item_type](product_id=order.product_id, name=order.name, **order.item_details)


class HalloweenFactory(Factory):
    def create_item(self, order):
        switch = {
            ProductType.Toy: RCSpider,
            ProductType.StuffedAnimal: DancingSkeleton,
            ProductType.Candy: PumpkinCaramelToffee
        }
        item_type = ProductType[order.item_type]
        return switch[item_type](product_id=order.product_id, name=order.name, **order.item_details)


class EasterFactory(Factory):
    def create_item(self, order):
        switch = {
            ProductType.Toy: RobotBunny,
            ProductType.StuffedAnimal: EasterBunny,
            ProductType.Candy: CremeEgg
        }
        item = switch[ProductType[order.item_type]]
        return item(product_id=order.product_id, name=order.name, **order.item_details)
