from store import Store
from inventory import Inventory, InventoryManager
from ui import UI
def main():
    inventory = Inventory()
    inventory_manager = InventoryManager(inventory)
    store = Store(inventory_manager)
    UI.menu(store)


if __name__ == "__main__":
    main()