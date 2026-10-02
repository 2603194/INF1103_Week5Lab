# -----------------------------
# Inventory Functions
# -----------------------------

def add_product(inventory, product_id, name, quantity):
    """Add a new product to the inventory."""
    new_product = {"id": str(product_id), "name": name, "quantity": quantity}
    inventory.append(new_product)
    print(f" Product added: {new_product}")
    return inventory


def update_stock(inventory, product_id, new_quantity):
    """Update stock quantity for a given product ID."""
    for product in inventory:
        if product["id"] == str(product_id):
            product["quantity"] = new_quantity
            print(f" Stock updated: {product}")
            return True
    print(" Product not found.")
    return False


def search_product(inventory, product_name):
    """Search for a product by name."""
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            print(f" Found: {product}")
            return product
    print(" Product not found.")
    return None


def display_all(inventory):
    """Display all products in the inventory."""
    print("\n Current Inventory:")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Quantity: {product['quantity']}")

def main():
    # Initialize with at least 3 products
    inventory = [
        {"id": "1001", "name": "Laptop", "quantity": 5},
        {"id": "1002", "name": "Mouse", "quantity": 10},
        {"id": "1003", "name": "Keyboard", "quantity": 7}
    ]

    display_all(inventory)

    # Add a new product
    add_product(inventory, 1004, "Monitor", 3)

    # Update stock
    update_stock(inventory, 1002, 15)

    # Search product
    search_product(inventory, "Keyboard")

    # Display all again
    display_all(inventory)


if __name__ == "__main__":
    main()
