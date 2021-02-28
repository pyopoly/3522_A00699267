from store import Store
from inventory import Inventory, InventoryManager
from ui import UI


def main():
    inventory = Inventory()
    inventory_manager = InventoryManager(inventory)
    store = Store(inventory_manager)
    ui = UI(store)
    ui.menu()


if __name__ == "__main__":
    main()