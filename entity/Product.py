class Product:
    def __init__(self, product_id, name, price, description):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__description = description

    # Getters
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f"ProductID: {self.__product_id}, Name: {self.__name}, Price: {self.__price}, Description: {self.__description}"
