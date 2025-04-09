
from exception.InsufficientStockException import InsufficientStockException

class InventoryCollection:
    def __init__(self):
        self.inventory = {}  # key: product_id, value: quantity

    def add_stock(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id] += quantity
        else:
            self.inventory[product_id] = quantity

    def remove_stock(self, product_id, quantity):
        if product_id not in self.inventory or self.inventory[product_id] < quantity:
            raise InsufficientStockException("Stock not available.")
        self.inventory[product_id] -= quantity

    def get_stock(self, product_id):
        return self.inventory.get(product_id, 0)

    def get_inventory(self):
        return dict(sorted(self.inventory.items()))  # Sorted by product_id
