from entity.Product import Product
from exception.InvalidDataException import InvalidDataException

class ProductCollection:
    def __init__(self):
        self.products = []  # List of Product objects

    def add_product(self, product):
        if any(p.get_product_id() == product.get_product_id() for p in self.products):
            raise InvalidDataException("Duplicate product ID detected.")
        self.products.append(product)

    def update_product(self, product_id, name=None, price=None, description=None):
        for p in self.products:
            if p.get_product_id() == product_id:
                if name:
                    p.set_name(name)
                if price is not None:
                    p.set_price(price)
                if description:
                    p.set_description(description)
                return
        raise InvalidDataException("Product not found.")

    def remove_product(self, product_id):
        for p in self.products:
            if p.get_product_id() == product_id:
                self.products.remove(p)
                return
        raise InvalidDataException("Cannot remove. Product not found.")

    def search_product_by_name(self, name):
        return [p for p in self.products if name.lower() in p.get_name().lower()]

    def get_all_products(self):
        return self.products
