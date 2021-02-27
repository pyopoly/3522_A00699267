from factory import Factory


class Inventory:
    def __init__(self):
        self._products = {}
        # self._inventory_manager = InventoryManager()

    def get_stock(self, item):
        for product, stock in self.items():
            if product == item:
                return stock

    # def reduce_stock(self, item, amount):
    #     self._products[item] -= amount
    #
    # def increase_stock(self, item, amount):
    #     self._products[item] += amount
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

    def __getitem__(self, item):
        for product in self._products.keys():
            if item == product:
                return product
        else:
            return None

    def __len__(self):
        return len(self._products)

    def __iter__(self):
        return iter(self._products.items())


class InventoryManager:
    def __init__(self, inventory):
        self._inventory = inventory

    def process_order(self, order):
        # item = order.factory().create_item(order.item_type, 100)
        item = Factory.get_factory(order).create_item(order)
        # id = order.product_id
        amount = order.quantity_required()
        if self.item_in_inventory(item):
            if self.enough_stock(item, amount):
                self.reduce_stock(item, amount)
            else:
                self.replenish_stock(item, 100)
            # reduce stock
        else:
            self.purchase_item(item, 100)
            # product = self[id]
            # make new item from order
            # item = self.purchase_item(order)
            # print("itemL ", item)
            # purchase stock

    # def check_inventory(self):
    #     for product, stock in self._inventory:


    def purchase_item(self, item, amount):
        self._inventory.add_item(item, amount)
        # item = order.factory().create_item(order.item_type, 100)
        # factory = Factory.get_factory(order.factory)
        # item = factory.create_item(order.item_type, 100)
        # item.increase_stock(100)
        # return order.purchase_item()

    def item_in_inventory(self, item):
        return item in self._inventory

    def enough_stock(self, item, amount):
        # product = self._inventory[item]
        stock = self._inventory.get_stock(item)
        return amount <= stock

    def reduce_stock(self, item, amount):
        self._inventory.change_stock(item, -amount)
        # self._inventory[item].reduce_stock(amount)

    def replenish_stock(self, item, amount):
        self._inventory.change_stock(item, amount)

    def get_inventory(self):
        return self._inventory

    inventory = property(get_inventory)
    # def increase_stock(self, product, amount):

    # def add_product_to_inventory(self, product):
    #     self._products.append(product)