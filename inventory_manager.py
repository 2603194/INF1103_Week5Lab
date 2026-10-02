import os
import json

# -----------------------------
# Persistence Functions
# -----------------------------

def load_inventory(filename="inventory.json"):
    """Load inventory from JSON file if it exists, otherwise return empty list."""
    if not os.path.exists(filename):
        print("inventory.json not found.")
        return []
    with open(filename, "r") as f:
        inventory = json.load(f)
    print("inventory.json found.\nInventory loaded successfully.")
    return inventory


def save_inventory(inventory, filename="inventory.json"):
    """Save inventory to JSON file."""
    print("\nSaving inventory...")
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved successfully to inventory.json.")


# -----------------------------
# Inventory Functions
# -----------------------------

def add_product(inventory, product_id, name, price, quantity):
    """Add a new product to the inventory."""
    new_product = {
        "id": str(product_id),
        "name": name,
        "price": float(price),
        "stock": int(quantity)
    }
    inventory.append(new_product)
    print("\nProduct added successfully!")
    return inventory


def update_stock(inventory, product_id, new_quantity):
    """Update stock quantity for a given product ID."""
    for product in inventory:
        if product["id"] == str(product_id):
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            product["stock"] = int(new_quantity)
            print(f"\nStock updated successfully!")
            return True
    print("\nProduct not found.")
    return False


def search_product(inventory, product_id):
    """Search for a product by ID."""
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("\nProduct Found")
            print("------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------")
            return product
    print("\nProduct not found.")
    return None


def display_all(inventory):
    """Display all products in the inventory."""
    print("\nCurrent Inventory")
    print("----------------------------------------")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("----------------------------------------")


# -----------------------------
# Menu System
# -----------------------------

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    inventory = load_inventory()

    # Initialize with at least 3 products if inventory is empty
    if not inventory:
        inventory = [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]

    while True:
        print("\n--------- MENU ---------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("------------------------")

        choice = input("Enter option: ")

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            print("\nAdd New Product")
            pid = input("Product ID: ")
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                qty = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid input. Price must be a number, quantity must be an integer.")
                continue
            add_product(inventory, pid, name, price, qty)

        elif choice == "3":
            print("\nUpdate Stock")
            pid = input("Enter Product ID: ")
            try:
                qty = int(input("New Stock Quantity: "))
            except ValueError:
                print("Invalid quantity.")
                continue
            update_stock(inventory, pid, qty)

        elif choice == "4":
            print("\nSearch Product")
            pid = input("Enter Product ID: ")
            search_product(inventory, pid)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
