from factory import Factory


class Inventory:
    def __init__(self):
        self._products = {}

    def get_stock(self, item):
        for product, stock in self.items():
            if product == item:
                return stock

    def change_stock(self, item, amount):
        self._products[item] += amount

    def add_item(self, item, amount):
        self._products[item] = amount

    def items(self):
        return self._products.items()

    def __contains__(self, item):
        for product in self._products.keys():
            if item == product:
                return True
        return False

    def __len__(self):
        return len(self._products)

    def __iter__(self):
        return iter(self._products.items())


class InventoryManager:
    in_stock = "IN STOCK"
    low_stock = "LOW"
    very_low_stock = "VERY LOW"
    out_of_stock = "OUT OF STOCK"

    def __init__(self, inventory):
        self._inventory = inventory

    def process_order(self, order):
        item = Factory.get_factory(order).create_item(order)
        amount = order.quantity_required()
        if self.item_in_inventory(item):
            if self.enough_stock(item, amount):
                self.reduce_stock(item, amount)
            else:
                self.replenish_stock(item, 100)
        else:
            self.purchase_item(item, 100)

    def purchase_item(self, item, amount):
        self._inventory.add_item(item, amount)

    def item_in_inventory(self, item):
        return item in self._inventory

    def enough_stock(self, item, amount):
        stock = self._inventory.get_stock(item)
        return amount <= stock

    def reduce_stock(self, item, amount):
        self._inventory.change_stock(item, -amount)

    def replenish_stock(self, item, amount):
        self._inventory.change_stock(item, amount)

    def stock_status(self, item):
        stock = self._inventory.get_stock(item)
        switch = {
            range(3, 10): self.low_stock,
            range(1, 3): self.very_low_stock,
            range(0, 1): self.out_of_stock
        }
        for key in switch.keys():
            if stock in key:
                return switch[key]
        return self.in_stock

    def get_inventory(self):
        return self._inventory

    inventory = property(get_inventory)
