from util.DBConnector import DBConnector

def test_connection():
    try:
        conn = DBConnector.get_connection()
        print("Database connection established successfully.")
        conn.close()
    except Exception as e:
        print("Failed to connect to database:", e)

if __name__ == "__main__":
    test_connection()
