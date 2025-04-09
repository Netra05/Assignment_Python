# dao/ProductDAO.py

from util.DBConnector import DBConnector
from entity.Product import Product
import pyodbc

class ProductDAO:
    def add_product(self, product):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Products (ProductID, ProductName, Price, Description)
                VALUES (?, ?, ?, ?)
            """, product.get_product_id(), product.get_name(), product.get_price(), product.get_description())
            conn.commit()
            print("Product added successfully.")
        except pyodbc.Error as e:
            print("Error adding product:", e)
        finally:
            conn.close()

    def search_product_by_name(self, name):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductName LIKE ?", ('%' + name + '%',))
            rows = cursor.fetchall()
            products = [Product(row[0], row[1], row[2], row[3]) for row in rows]
            return products
        except pyodbc.Error as e:
            print("Error searching product:", e)
            return []
        finally:
            conn.close()
