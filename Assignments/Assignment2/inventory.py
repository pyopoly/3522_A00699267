from enum import Enum, auto




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
                self.replenish_stock(id)
            # reduce stock
        else:
            # product = self[id]
            # make new item from order
            item = self.purchase_item(order)
            print("itemL ", item)
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
        return product_id in self

    def enough_stock(self, product_id, amount):
        product = self[product_id]
        return amount <= product.stock

    def reduce_stock(self, product_id, amount):
        self[product_id].reduce_stock(amount)

    def replenish_stock(self, product_id):
        self[product_id].stock += 100


    def purchase_item(self, order):
        return order.purchase_item()

