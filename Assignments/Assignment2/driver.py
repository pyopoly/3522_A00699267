from store import Store
from inventory import Inventory
from ui import UI
def main():
    inventory = Inventory()
    store = Store(inventory)
    UI.menu(store)


if __name__ == "__main__":
    main()