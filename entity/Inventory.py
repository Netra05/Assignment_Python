# entity/Inventory.py

class Inventory:
    def __init__(self, inventory_id, product_id, quantity_available):
        self.__inventory_id = inventory_id
        self.__product_id = product_id
        self.__quantity_available = quantity_available

    # Getters
    def get_inventory_id(self):
        return self.__inventory_id

    def get_product_id(self):
        return self.__product_id

    def get_quantity_available(self):
        return self.__quantity_available

    # Setters
    def set_quantity_available(self, quantity):
        self.__quantity_available = quantity

    def __str__(self):
        return f"InventoryID: {self.__inventory_id}, ProductID: {self.__product_id}, Available Quantity: {self.__quantity_available}"
