"""
This module contains the Store, Inventory, and InventoryManager classes. The Store processes orders.
Store hires an InventoryManager to manage the Inventory. The Inventory contains a dictionary of
all Products and their current stock.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

import datetime

from file_handler import FileHandler
from order import OrderProcessor
from factory import FactoryMapper
from products import Product, InvalidDataError


class Store:
    """
    Store communicates with OrderProcessor and InventoryManager to manage the store. OrderProcessor grabs Orders and
    the Store tells InventoryManager to respond to these Orders.
    """
    def __init__(self, inventory_manager, ui):
        self._ui = ui
        self._inventory_manager = inventory_manager
        self._report_manager = ReportManager()

    def process_web_orders(self):
        """
        Processes web orders from an xlsx excel sheet. The order is read by OrderProcessor and then the Product is
        created by the Factory. And then the Inventory manager will manage the Inventory based on the request in
        the order. Then Store asks UI to print the status as each Product is being processed.
        :return: None
        """
        while True:
            try:
                orders = OrderProcessor.read_order()
            except FileNotFoundError:
                print("File not found")
            else:
                break
        restock_amount = 100
        for i, order in enumerate(orders, start=1):
            requested_amount = order.quantity_required()
            try:
                item = FactoryMapper.create_item(order)
                stock_status = self._inventory_manager.process_order(item, requested_amount, restock_amount)
                self._ui.print_order_process_status(order.order_number, str(item), stock_status, restock_amount,
                                                    requested_amount)
                self._report_manager.save_successful_report(order.order_number, order.name, order.item_type,
                                                            order.product_id, requested_amount)
            except InvalidDataError as exception:
                stock_status = "FAILED"
                self._ui.print_order_process_status(order.order_number, "Invalid Data", stock_status, restock_amount,
                                                    requested_amount)
                self._report_manager.save_failed_report(order.order_number, exception)

    def show_inventory(self):
        """
        Asks InventoryManager to give the status of all Products in the Inventory, which include the name of
        the product as a string, the stock as an int, the stock_status as a string, and then asks the UI to
        display the status to the user.
        :return: None
        """
        inventory_status = self._inventory_manager.get_inventory_status()
        for i, (product, stock, stock_status) in enumerate(inventory_status, start=1):
            self._ui.print_inventory(i, product, stock, stock_status)

    def open_for_business(self):
        """ Open the Store for Business. Asks UI to print menu choices for user to choose and then run that choice."""
        while True:
            choice = self._ui.menu(self.process_web_orders, self.show_inventory, self.exit)
            choice()
            self._ui.pause()

    def exit(self):
        report = self._report_manager.create_report()
        self._ui.print_report(report)
        exit()


class Inventory:
    """
    Inventory contains a dictionary of Products and their current stock. Inventory is an iterable which iterates
    through the Products and it's stock (dictionary).
    """
    def __init__(self):
        self._products = {}

    def get_stock(self, item: Product):
        """
        Checks the current stock of the item/Product.
        :param item: Product to be checked
        :return: int for the stock number
        """
        for product, stock in self.items():
            if product == item:
                return stock

    def change_stock(self, item: Product, amount: int):
        """
        Changes the stock in the Inventory for the item/Product.
        :param item: Product
        :param amount: int, the amount to be changed
        :return: None
        """
        self._products[item] += amount

    def add_item(self, item: Product, amount: int):
        """
        Add a new item to the Inventory.
        :param item: Product to be added
        :param amount: int, the amount added
        :return: None
        """
        self._products[item] = amount

    def items(self):
        """
        Returns a Product and it's stock as an int in the Inventory (dictionary).
        :return: (Product, int) product and it's stock as an int
        """
        return self._products.items()

    def __contains__(self, item: Product):
        """ Container Protocol. Checks if a Product is in the Inventory. """
        for product in self._products.keys():
            if item == product:
                return True
        return False

    def __len__(self):
        """ Iterable Protocol. Returns the number of the Products in the Inventory. """
        return len(self._products)

    def __iter__(self):
        """ Iterable Protocol. Returns the Dictionary of Products: stock(int). """
        return iter(self._products.items())


class InventoryManager:
    """
    InventoryManager manages the Inventory. This contains all logic related to showing Inventory status, reducing
    stock, increasing stock, adding Products to the Inventory.
    """
    in_stock = "IN STOCK"
    low_stock = "LOW"
    very_low_stock = "VERY LOW"
    out_of_stock = "OUT OF STOCK"
    new_item = "NEW ITEM"

    def __init__(self, inventory):
        self._inventory = inventory

    def process_order(self, item, requested_amount, restock_amount):
        """
        Order will always be fulfilled, meaning that stock will always be reduced by the requested amount.
        Order is processed by checking if inventory has a record of the item. If not, the item is purchased
        by the restock amount, if so, stock is checked to see if there is enough, if not, stock is replenished
        by the restock amount. In the end, the stock status is returned (NEW ITEM, IN STOCK, or OUT OF STOCK).
        :param item: Product
        :param requested_amount: int
        :param restock_amount: int
        :return: str for the stock status
        """
        if self.item_in_inventory(item):
            if self.enough_stock(item, requested_amount):
                stock_status = self.in_stock
            else:
                stock_status = self.out_of_stock
                self.replenish_stock(item, restock_amount)
        else:
            stock_status = self.new_item
            self.purchase_item(item, restock_amount)
        self.reduce_stock(item, requested_amount)
        return stock_status

    def purchase_item(self, item, amount):
        """
        Purchase a new Product and add it to the Inventory.
        :param item: Product
        :param amount: int, the number of this Product to add
        :return: None
        """
        self._inventory.add_item(item, amount)

    def item_in_inventory(self, item):
        """
        Checks if this Product is in the Inventory or not.
        :param item: Product
        :return: boolean, True if Product is in Inventory
        """
        return item in self._inventory

    def enough_stock(self, item, amount):
        """
        Checks if there is enough amount of stock for this Product in the Inventory.
        Compares the param amount to the stock of this Product.
        :param item: Product
        :param amount: int
        :return: boolean, True if the Inventory has enough of this Product in stock.
        """
        stock = self._inventory.get_stock(item)
        return amount <= stock

    def reduce_stock(self, item, amount):
        """
        Reduces this Product's stock by this amount in the Inventory.
        :param item: Product
        :param amount: int
        :return: None
        """
        self._inventory.change_stock(item, -amount)

    def replenish_stock(self, item, amount):
        """
        Replenishes this Product's stock by increasing its stock by the amount.
        :param item: Product
        :param amount: int
        :return: None
        """
        self._inventory.change_stock(item, amount)

    def stock_status(self, item):
        """
        Checks the stock of this Product, and then returns a message representing its stock status.
        0 in Inventory is "OUT OF STOCK".
        1 ~ 2 is "VERY LOW".
        3 ~ 10 is "LOW".
        else, return "IN STOCK" for 10 or more in Inventory.
        :param item: Product
        :return: string for the status of the stock
        """
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

    def get_inventory_status(self):
        """
        Gets the status of the products in inventory when requested. The status includes the name of the product,
        the current stock of this product, and it's stock status such as out of stock.
        :return: Iterable(Product name: string, stock: int, stock_status: str)
        """
        inventory_status = ((str(product), stock, self.stock_status(product)) for (product, stock) in self._inventory)
        return inventory_status


class ReportManager:
    def __init__(self):
        self._dtr = ""

    def save_successful_report(self, order_number, item_name, item_type, product_id, request_amount):
        successful_order_record = f'Order {order_number}, Item {item_type}, ' \
                                  f'Product ID {product_id}, Name "{item_name}", ' \
                                  f'Quantity {request_amount}\n'
        self._dtr += successful_order_record

    def save_failed_report(self, order_number, exception):
        failed_order_record = f"Order {order_number}, Could not process " \
                              f"order data was corrupted, InvalidDataError - {exception.args[1]} can " \
                              f"only be {exception.args[2]}\n"
        self._dtr += failed_order_record

    def create_report(self):
        date = datetime.date.today().strftime("%d%m%y")
        time = datetime.datetime.now().strftime("%H%M")
        file_path = f"DTR_{date}_{time}.txt"
        current_date = datetime.date.today().strftime("%d-%m-%Y")
        current_time = datetime.datetime.now().strftime("%H:%m")
        transaction_report = f"HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)" \
                             f"\n{current_date} {current_time}\n"
        FileHandler.write_order(file_path, transaction_report)
        FileHandler.write_order(file_path, self._dtr)
        return self._dtr
