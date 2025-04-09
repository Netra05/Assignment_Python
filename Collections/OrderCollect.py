from entity.Order import Order
from exception.IncompleteOrderException import IncompleteOrderException

class OrderCollection:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        # Validate essential fields
        if not order.order_id or not order.customer_id or order.total_amount <= 0:
            raise IncompleteOrderException("Invalid order details.")
        self.orders.append(order)

    def update_order_status(self, order_id, new_status):
        for o in self.orders:
            if o.order_id == order_id:
                o.status = new_status
                return
        raise IncompleteOrderException("Order not found.")

    def remove_order(self, order_id):
        for o in self.orders:
            if o.order_id == order_id:
                self.orders.remove(o)
                return
        raise IncompleteOrderException("Cannot remove. Order not found.")

    def sort_orders_by_date(self, descending=False):
        return sorted(self.orders, key=lambda o: o.order_date, reverse=descending)

    def get_all_orders(self):
        return self.orders
