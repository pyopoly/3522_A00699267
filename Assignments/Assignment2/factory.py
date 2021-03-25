"""
This module contains the Factory classes. There are three types of Factories each corresponding to a holiday:
ChristmasFactory, HalloweenFactory, and EasterFactory. Each Factory can create three types of
Products: Toy, StuffedAnimal, and Candy.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

import abc
from products import *


class AbstractFactory(abc.ABC):
    """
    Abstract Factory that creates an product. When an order is sent to the factory, the factory figures out which
    Factory to call to create the item.
    """
    @staticmethod
    def instantiate_item_decorator(function):
        """
        This is a decorator method that instantiates a Product by inserting the product_id, name, and details.
        Function here is the create_item(self, order) of a Child Factory. Each time a Child Factory runs
        its create_item(self, order), this decorator method is called to instantiate the item for the Child Factory.
        :param function: Method, Child Factory.create_item(self, order)
        :return: Product, instantiated concrete product
        """
        def inner(item, order):
            product = function(item, order)
            return product(product_id=order.product_id, name=order.name, **order.item_details)
        return inner

    @abc.abstractmethod
    def create_toy(self, order):
        """
        Create a Toy Product. The method returns the class reference of Toy, and the class is then instantiated
        with @AbstractFactory.instantiate_item_decorator in the concrete Factory class.
        :param order: Order
        :return: class reference of Toy.
        """
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, order):
        """
        Create a StuffedAnimal Product. The method returns the class reference of StuffedAnimal, and the class is
        then instantiated with @AbstractFactory.instantiate_item_decorator in the concrete Factory class.
        :param order: Order
        :return: class reference of StuffedAnimal.
        """
        pass

    @abc.abstractmethod
    def create_candy(self, order):
        """
        Create a Candy Product. The method returns the class reference of Candy, and the class is
        then instantiated with @AbstractFactory.instantiate_item_decorator in the concrete Factory class.
        :param order: Order
        :return: class reference of Candy.
        """
        pass


class FactoryMapper:
    """ Factory returns the Factory that is needed to create the Product by asking the Order. """

    @staticmethod
    def create_item(order):
        """
        Order contains the Factory required to fulfill this Order and create the Product. The specific Factory
        is stored in Order, and the type of "create item method" is called based on the mapper.
        :param order: Order
        :return: Product
        """
        factory = order.factory()
        factory_item_mapper = {
            "Toy": factory.create_toy,
            "StuffedAnimal": factory.create_stuffed_animal,
            "Candy": factory.create_candy
        }
        return factory_item_mapper.get(order.item_type)(order)


class ChristmasFactory(AbstractFactory):
    """
    Christmas Factory that is in charge of create Products related to the Christmas holiday.
    """
    @AbstractFactory.instantiate_item_decorator
    def create_toy(self, order):
        return SantasWorkshop

    @AbstractFactory.instantiate_item_decorator
    def create_stuffed_animal(self, order):
        return Reindeer

    @AbstractFactory.instantiate_item_decorator
    def create_candy(self, order):
        return CandyCane


class HalloweenFactory(AbstractFactory):
    """
    Halloween Factory that is in charge of create Products related to the Halloween holiday.
    """
    @AbstractFactory.instantiate_item_decorator
    def create_toy(self, order):
        return RCSpider

    @AbstractFactory.instantiate_item_decorator
    def create_stuffed_animal(self, order):
        return DancingSkeleton

    @AbstractFactory.instantiate_item_decorator
    def create_candy(self, order):
        return PumpkinCaramelToffee


class EasterFactory(AbstractFactory):
    """
    Easter Factory that is in charge of create Products related to the Easter holiday.
    """
    @AbstractFactory.instantiate_item_decorator
    def create_toy(self, order):
        return RobotBunny

    @AbstractFactory.instantiate_item_decorator
    def create_stuffed_animal(self, order):
        return EasterBunny

    @AbstractFactory.instantiate_item_decorator
    def create_candy(self, order):
        return CremeEgg


