import pandas
from factory import ChristmasFactory, HalloweenFactory, EasterFactory, ProductType
from inventory import Inventory

class Store:
    def __init__(self, inventory):
        self._inventory = inventory
        self._order_processor = OrderProcessor()

    def download_orders(self, filepath):
        pass


    def process_order(self):
        orders = self._order_processor.read_order()
        for order in orders:
            self._inventory.check_item_in_inventory(order)


class OrderProcessor:
    # def __init__(self):
    #     self._orders = []

    def read_order(self):
        orders = []
        file = pandas.read_excel("orders.xlsx")

        rows = len(file)
        for i in range(rows):
            row = pandas.DataFrame(file).loc[i].to_dict()
            orders.append(Order(**row))
        return orders

    class FactoryMapping:
        factories = [ChristmasFactory, HalloweenFactory, EasterFactory]
        @classmethod
        def find_factory(cls, holiday):
            factory_type = holiday + "Factory"
            for factory in cls.factories:
                if factory.__name__ == factory_type:
                    return factory



class Order:
    def __init__(self, **kwargs):
        self._order_number = kwargs.pop('order_number')
        self._product_id = kwargs.pop('product_id')
        self._item = kwargs.pop('item')
        self._name = kwargs.pop('name')
        holiday = kwargs.pop('holiday')
        self._details = kwargs
        self._factory = OrderProcessor.FactoryMapping.find_factory(holiday)

    def __str__(self):
        return f"order: {self._order_number}, name: {self._name}, productID: {self._product_id}, type: {self._item}"

    def get_product_id(self):
        return self._product_id

    # def get_item_type(self):
    #     return self._item

    def quantity_required(self):
        return self._details['quantity']

    def purchase_item(self):
        f = self._factory()
        return f.create_item(self._item)

    product_id = property(get_product_id)
    # item_type = property(get_item_type)


class Report:
    pass


class User:
    pass


s = OrderProcessor()
s.read_order()
