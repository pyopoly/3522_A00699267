from order import OrderProcessor


class Store:
    def __init__(self, inventory_manager):
        self._inventory_manager = inventory_manager
        self._order_processor = OrderProcessor()

    def download_orders(self, filepath):
        pass

    def process_orders(self):
        orders = OrderProcessor.read_order()
        for order in orders:
            self._inventory_manager.process_order(order)

    def get_inventory(self):
        return self._inventory_manager.inventory

    def get_inventory_manager(self):
        return self._inventory_manager

    inventory = property(get_inventory)
    inventory_manager = property(get_inventory_manager)


class Report:
    pass


class User:
    pass
