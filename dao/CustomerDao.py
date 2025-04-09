from util.DBConnector import DBConnector
from entity.Customer import Customer
import pyodbc

class CustomerDAO:
    def add_customer(self, customer):
        conn = DBConnector.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?, ?)",
                customer.get_customer_id(),
                customer.get_first_name(),
                customer.get_last_name(),
                customer.get_email(),
                customer.get_phone(),
                customer.get_address()
            )
            conn.commit()
            print("Customer added successfully.")
        except pyodbc.Error as e:
            print("Error adding customer:", e)
        finally:
            conn.close()

    def get_all_customers(self):
        conn = DBConnector.get_connection()
        customers = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customers")
            rows = cursor.fetchall()
            for row in rows:
                customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5])
                customers.append(customer)
            return customers
        except pyodbc.Error as e:
            print("Error retrieving customers:", e)
            return []
        finally:
            conn.close()

    def search_customer_by_name(self, name):
        conn = DBConnector.get_connection()
        customers = []
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Customers WHERE FirstName LIKE ? OR LastName LIKE ?",
                f"%{name}%", f"%{name}%"
            )
            rows = cursor.fetchall()
            for row in rows:
                customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5])
                customers.append(customer)
            return customers
        except pyodbc.Error as e:
            print("Error searching customer by name:", e)
            return []
        finally:
            conn.close()
