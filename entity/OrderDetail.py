class OrderDetail:
    def __init__(self, order_id, product_id, quantity):
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity

    def get_order_id(self):
        return self.__order_id

    def get_product_id(self):
        return self.__product_id

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return f"OrderID: {self.__order_id}, ProductID: {self.__product_id}, Quantity: {self.__quantity}"
