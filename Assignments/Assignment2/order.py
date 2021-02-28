import pandas
from factory import ChristmasFactory, HalloweenFactory, EasterFactory


class OrderProcessor:
    @staticmethod
    def read_order():
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

    def quantity_required(self):
        return self._details['quantity']

    def __str__(self):
        return f"order: {self._order_number}, name: {self._name}, productID: {self._product_id}, type: {self._item}"

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_item_type(self):
        return self._item

    def get_factory(self):
        return self._factory

    def get_details(self):
        return self._details

    product_id = property(get_product_id)
    name = property(get_name)
    factory = property(get_factory)
    item_type = property(get_item_type)
    item_details = property(get_details)
