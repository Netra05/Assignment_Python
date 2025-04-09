class Order:
    def __init__(self, order_id, customer_id, order_date, total_amount):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__order_date = order_date
        self.__total_amount = total_amount

    def get_order_id(self):
        return self.__order_id

    def get_customer_id(self):
        return self.__customer_id

    def get_order_date(self):
        return self.__order_date

    def get_total_amount(self):
        return self.__total_amount

    def __str__(self):
        return f"OrderID: {self.__order_id}, CustomerID: {self.__customer_id}, Date: {self.__order_date}, Total: {self.__total_amount}"
