"""
This module contains the OrderProcessor class, and the Order class.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

from factory import ChristmasFactory, HalloweenFactory, EasterFactory
from file_handler import FileHandler


class OrderProcessor:
    """
    OrderProcessor Creates Orders by asking FileHandler to read an order file.
    """
    factory_mapping = {
            "Christmas": ChristmasFactory,
            "Halloween": HalloweenFactory,
            "Easter": EasterFactory
    }

    @staticmethod
    def read_order():
        """
        Asks the FileHandler to read from a filepath that is an Order request, and then instantiate all the Orders in
        the request and returns it as list (map).
        :return: map of Orders
        """
        while True:
            file_path = input("filepath (eg. orders.xlsx): ")
            if file_path != "":
                break
        orders = map(lambda order: Order(**order), FileHandler.read_order(file_path))
        return orders


class Order:
    """
    An order to request a Product. The Order has a _factory attribute which shows the Factory responsible of
    creating the Product in this Order.
    """
    def __init__(self, **kwargs):
        self._order_number = kwargs.pop('order_number')
        self._product_id = kwargs.pop('product_id')
        self._item = kwargs.pop('item')
        self._name = kwargs.pop('name')
        self._details = kwargs
        self._factory = OrderProcessor.factory_mapping[kwargs.pop('holiday')]

    def quantity_required(self):
        """
        The amount of this Product that is requested.
        :return: int
        """
        return self._details['quantity']

    def __str__(self):
        """ Formatted toString. """
        return f"order: {self._order_number}, name: {self._name}, productID: {self._product_id}, type: {self._item}"

    def get_order_number(self):
        """
        Gets the order number.
        :return: string
        """
        return self._order_number

    def get_product_id(self):
        """
        The product ID, a unique ID.
        :return: string
        """
        return self._product_id

    def get_name(self):
        """
        The name of the Product in this Order.
        :return: string
        """
        return self._name

    def get_item_type(self):
        """
        The type of Item of the Product in this Order. Can be Toy, Stuffed Animal, or Candy.
        :return: string
        """
        return self._item

    def get_factory(self):
        """
        The Factory that can create the Product in this Order.
        :return: Factory
        """
        return self._factory

    def get_details(self):
        """
        Gets a list of remaining details of this order.
        :return: list
        """
        return self._details

    order_number = property(get_order_number)
    product_id = property(get_product_id)
    name = property(get_name)
    factory = property(get_factory)
    item_type = property(get_item_type)
    item_details = property(get_details)
