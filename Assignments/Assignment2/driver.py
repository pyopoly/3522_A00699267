"""
Driver for the Store Program.
"""

__author__ = "Jack Shih & Tegvaran Sooch"
__version__ = "Mar 2021"

from store import Store, Inventory, InventoryManager
from ui import ConsoleUI


def main():
    inventory = Inventory()
    inventory_manager = InventoryManager(inventory)
    ui = ConsoleUI()
    store = Store(inventory_manager, ui)
    store.open_for_business()


if __name__ == "__main__":
    main()
