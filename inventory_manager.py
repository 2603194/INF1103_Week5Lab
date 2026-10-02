import os
import json

# -----------------------------
# Persistence Functions
# -----------------------------

def load_inventory(filename="inventory.json"):
    """Load inventory from JSON file if it exists, otherwise return empty list."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        inventory = json.load(f)
    return inventory


def save_inventory(inventory, filename="inventory.json"):
    """Save inventory to JSON file."""
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved to inventory.json")


# -----------------------------
# Inventory Functions
# -----------------------------

def add_product(inventory, product_id, name, quantity):
    """Add a new product to the inventory."""
    new_product = {"id": str(product_id), "name": name, "quantity": quantity}
    inventory.append(new_product)
    print(f"Product added: {new_product}")
    return inventory


def update_stock(inventory, product_id, new_quantity):
    """Update stock quantity for a given product ID."""
    for product in inventory:
        if product["id"] == str(product_id):
            product["quantity"] = new_quantity
            print(f"Stock updated: {product}")
            return True
    print("Product not found.")
    return False


def search_product(inventory, product_name):
    """Search for a product by name."""
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            print(f"Found: {product}")
            return product
    print("Product not found.")
    return None


def display_all(inventory):
    """Display all products in the inventory."""
    print("\nCurrent Inventory:")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Quantity: {product['quantity']}")


# -----------------------------
# Main Program
# -----------------------------

def main():
    inventory = load_inventory()

    # Initialize with at least 3 products if inventory is empty
    if not inventory:
        inventory = [
            {"id": "1001", "name": "Laptop", "quantity": 5},
            {"id": "1002", "name": "Mouse", "quantity": 10},
            {"id": "1003", "name": "Keyboard", "quantity": 7}
        ]

    while True:
        display_all(inventory)
        choice = input("\nChoose action: add / update / search / quit: ").lower()

        if choice == "quit":
            save_inventory(inventory)
            break

        elif choice == "add":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            try:
                qty = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid quantity.")
                continue
            add_product(inventory, pid, name, qty)

        elif choice == "update":
            pid = input("Enter Product ID to update: ")
            try:
                qty = int(input("Enter New Quantity: "))
            except ValueError:
                print("Invalid quantity.")
                continue
            update_stock(inventory, pid, qty)

        elif choice == "search":
            name = input("Enter Product Name to search: ")
            search_product(inventory, name)

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
