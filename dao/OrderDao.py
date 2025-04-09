from util.DBConnector import DBConnector
from entity.Order import Order
from exception.IncompleteOrderException import IncompleteOrderException
from exception.PaymentFailedException import PaymentFailedException
from exception.InsufficientStockException import InsufficientStockException
import pyodbc

class OrderDAO:
    def add_order(self, order):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            if not order.get_customer_id():
                raise IncompleteOrderException("Customer reference is missing.")

            cursor.execute("INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?, ?)",
                           order.get_order_id(), order.get_customer_id(), order.get_order_date(),
                           order.get_total_amount())

            conn.commit()
            print("Order placed successfully.")
        except pyodbc.Error as e:
            print("Error adding order:", e)
        finally:
            conn.close()

    def update_order_status(self, order_id, status):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE Orders SET Status = ? WHERE OrderID = ?", status, order_id)
            if cursor.rowcount == 0:
                print("Order not found.")
            else:
                conn.commit()
                print("Order status updated.")
        except pyodbc.Error as e:
            print("Error updating order status:", e)
        finally:
            conn.close()

    def get_order_summary(self):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    o.OrderID,
                    c.FirstName + ' ' + c.LastName AS CustomerName,
                    o.OrderDate,
                    o.TotalAmount
                FROM Orders o
                JOIN Customers c ON o.CustomerID = c.CustomerID
                ORDER BY o.OrderDate;
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                print(f"\nOrder Summary:")
                for row in results:
                    # Access the results by index since it's a tuple
                    print(f"Order ID: {row[0]}, Customer: {row[1]}, Date: {row[2]}, Total: ₹{row[3]}")
            else:
                print("No orders found.")
        except pyodbc.Error as e:
            print("Error fetching order summary:", e)
        finally:
            conn.close()

    def get_orders_by_customer(self, customer_id):
        conn = DBConnector.get_connection()
        orders = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Orders WHERE CustomerID = ?", customer_id)
            rows = cursor.fetchall()
            for row in rows:
                order = Order(row[0], row[1], row[2], row[3])
                orders.append(order)
            return orders
        except pyodbc.Error as e:
            print("Error retrieving orders:", e)
            return []
        finally:
            conn.close()
