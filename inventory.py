class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[input("Enter item name: ")] += quantity
        else:
            self.items[input("Enter item name: ")] = quantity

    def update_item(self, name, quantity):
        if name in self.items:
            self.items[name] = quantity
        else:
            print(f"Item '{name}' not found in inventory.")

    def get_item(self, name):
        return self.items.get(name, f"Item '{name}' not found in inventory.")

    def total_quantity(self):
        return sum(self.items.values())

    def display_inventory(self):
        for name, quantity in self.items.items():
            print(f"{name}: {quantity}")


