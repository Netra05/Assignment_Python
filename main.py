# main.py (Updated with Exception Handling, Search & Reports)

from dao.CustomerDao import CustomerDAO
from dao.ProductDao import (ProductDAO)
from dao.OrderDao import OrderDAO
from dao.OrderDetailsDao import OrderDetailsDAO
from dao.InventoryDao import InventoryDAO
from entity.Customer import Customer
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetail import OrderDetail
from entity.Inventory import Inventory
from datetime import datetime

customer_dao = CustomerDAO()
product_dao = ProductDAO()
order_dao = OrderDAO()
details_dao = OrderDetailsDAO()
inventory_dao = InventoryDAO()

def display_menu():
    print("\n==== TechShop Main Menu ====")
    print("1. Add Customer")
    print("2. Add Product")
    print("3. Place Order")
    print("4. Add Order Detail")
    print("5. Add Inventory")
    print("6. Update Inventory")
    print("7. View Inventory")
    print("8. Search Customer by Name")
    print("9. Search Product by Name")
    print("10. View Orders by Customer ID")
    print("11. View Inventory Report")
    print("12. Daily Order Summary")
    print("13. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            cid = input("Customer ID: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            customer = Customer(cid, fname, lname, email, phone, address)
            customer_dao.add_customer(customer)

        elif choice == '2':
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            desc = input("Description: ")
            product = Product(pid, name, price, desc)
            product_dao.add_product(product)

        elif choice == '3':
            oid = input("Order ID: ")
            cid = input("Customer ID: ")
            total = float(input("Total Amount: "))
            date = datetime.now().strftime("%Y-%m-%d")
            order = Order(oid, cid, date, total)
            order_dao.add_order(order)


        elif choice == '4':

            oid = input("Order ID: ")
            pid = input("Product ID: ")
            qty = int(input("Quantity: "))
            detail = OrderDetail(oid, pid, qty)
            details_dao.add_order_detail(detail)

        elif choice == '5':
            inv_id = int(input("Inventory ID: "))
            pid = input("Product ID: ")
            qty = int(input("Quantity In Stock: "))
            inv = Inventory(inv_id, pid, qty)
            inventory_dao.add_inventory(inv)

        elif choice == '6':
            pid = input("Product ID: ")
            change = int(input("Quantity to add/remove: "))
            inventory_dao.update_inventory_quantity(pid, change)

        elif choice == '7':
            pid = input("Product ID: ")
            inv = inventory_dao.get_inventory_by_product_id(pid)
            if inv:
                print(inv)

        elif choice == '8':
            name = input("Enter customer name to search: ")
            results = customer_dao.search_customer_by_name(name)
            for c in results:
                print(c)

        elif choice == '9':
            name = input("Enter product name to search: ")
            results = product_dao.search_product_by_name(name)
            for p in results:
                print(p)

        elif choice == '10':
            cid = input("Enter customer ID: ")
            orders = order_dao.get_orders_by_customer(cid)
            for o in orders:
                print(o)

        elif choice == '11':
            stock_list = inventory_dao.get_all_inventory()
            for stock in stock_list:
                print(
                    f"Product ID: {stock['ProductID']}, Stock: {stock['QuantityInStock']}, Last Updated: {stock['LastStockUpdate']}")

        elif choice == '12':
            date = input("Enter date (YYYY-MM-DD): ")
            summary = order_dao.get_order_summary()
            print(summary)

        elif choice == '13':
            print("Exiting TechShop. Goodbye!")
            break

        else:
            print("Invalid choice.")

    except Exception as e:
        print("An error occurred:", e)
