from util.DBConnector import DBConnector
from entity.OrderDetail import OrderDetail
import pyodbc

class OrderDetailsDAO:
    def add_order_detail(self, detail):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()

            # Auto-generate OrderDetailsID
            cursor.execute("SELECT ISNULL(MAX(OrderDetailsID), 0) + 1 FROM OrderDetails")
            detail_id = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO OrderDetails (OrderDetailsID, OrderID, ProductID, Quantity) VALUES (?, ?, ?, ?)",
                (detail_id, detail.get_order_id(), detail.get_product_id(), detail.get_quantity())
            )

            conn.commit()
            print("Order detail added successfully.")
        except pyodbc.Error as e:
            print("Error adding order detail:", e)
        finally:
            conn.close()

    def get_order_details_by_order_id(self, order_id):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT OrderDetailsID, OrderID, ProductID, Quantity FROM OrderDetails WHERE OrderID = ?",
                (order_id,)
            )
            rows = cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print("Error retrieving order details:", e)
            return []
        finally:
            conn.close()
