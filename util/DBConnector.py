import pyodbc

class DBConnector:
    @staticmethod
    def get_connection():
        try:
            conn = pyodbc.connect(
                "DRIVER={Your server name};"
                "SERVER={your server name};"
                "DATABASE={your db name};"
                "Trusted_Connection=yes;"
            )
            return conn
        except pyodbc.Error as e:
            print("Database connection failed:", e)
            return None
