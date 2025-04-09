# dao/InventoryDao.py

from util.DBConnector import DBConnector
from entity.Inventory import Inventory
import pyodbc

class InventoryDAO:
    def add_inventory(self, inventory):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock) VALUES (?, ?, ?)",
                inventory.get_inventory_id(),
                inventory.get_product_id(),
                inventory.get_quantity_available()
            )
            conn.commit()
            print("Inventory added successfully.")
        except pyodbc.Error as e:
            print("Error adding inventory:", e)
        finally:
            conn.close()

    def update_inventory_quantity(self, product_id, change):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Inventory SET QuantityInStock = QuantityInStock + ?, LastStockUpdate = GETDATE() WHERE ProductID = ?",
                change, product_id
            )
            conn.commit()
            print("Inventory updated successfully.")
        except pyodbc.Error as e:
            print("Error updating inventory:", e)
        finally:
            conn.close()

    def get_inventory_by_product_id(self, product_id):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT InventoryID, ProductID, QuantityInStock, LastStockUpdate FROM Inventory WHERE ProductID = ?",
                product_id
            )
            row = cursor.fetchone()
            if row:
                inventory = Inventory(row[0], row[1], row[2] if row[2] is not None else 0)  # Handle None quantity
                print(inventory)
                return {
                    "InventoryID": row[0],
                    "ProductID": row[1],
                    "QuantityInStock": row[2] if row[2] is not None else 0,  # Handle None quantity
                    "LastStockUpdate": row[3]
                }
            else:
                print("No inventory found for ProductID:", product_id)
                return None
        except pyodbc.Error as e:
            print("Error retrieving inventory:", e)
            return None
        finally:
            conn.close()

    def get_all_inventory(self):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT InventoryID, ProductID, QuantityInStock, LastStockUpdate FROM Inventory")
            rows = cursor.fetchall()
            inventory_list = []
            for row in rows:
                inventory_list.append({
                    "InventoryID": row[0],
                    "ProductID": row[1],
                    "QualityInStock": row[2],
                    "LastStockUpdate": row[3]
                })
            return inventory_list
        except pyodbc.Error as e:
            print("Error retrieving inventory list:", e)
            return []
        finally:
            conn.close()
