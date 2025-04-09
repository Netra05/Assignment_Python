import pyodbc

class DBConnector:
    @staticmethod
    def get_connection():
        try:
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=LAPTOP-A3LRA9TF;"
                "DATABASE=TechShop;"
                "Trusted_Connection=yes;"
            )
            return conn
        except pyodbc.Error as e:
            print("Database connection failed:", e)
            return None
