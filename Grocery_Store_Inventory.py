"""
Create a Python program that represents a grocery store
inventory using a dictionary, where the keys are the names
of items and the values are their quantities. The program
should allow the user to perform the following actions:
update the quantity of an existing item, add a new item to
the inventory with a specified quantity, and remove an item
from the inventory. The user should be prompted for their
desired action, and the program should handle invalid input
gracefully. This will help in understanding dictionary
manipulation and user interaction in Python.
"""
inventory = {}

while True:
    print("\nGrocery Store Inventory Management")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Remove Item")
    print("4. View Inventory")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        item = input("Enter the name of the item to add: ").strip()
        if item in inventory:
            print("Item already exists. Use the update option to change the quantity.")
        else:
            try:
                quantity = int(input("Enter the quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                else:
                    inventory[item] = quantity
                    print(f"Added {item} with quantity {quantity}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    elif choice == "2":
        item = input("Enter the name of the item to update: ").strip()
        if item in inventory:
            try:
                quantity = int(input("Enter the new quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                else:
                    inventory[item] = quantity
                    print(f"Updated {item} to quantity {quantity}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Item not found in inventory.")
    
    elif choice == "3":
        item = input("Enter the name of the item to remove: ").strip()
        if item in inventory:
            del inventory[item]
            print(f"Removed {item} from inventory.")
        else:
            print("Item not found in inventory.")
    
    elif choice == "4":
        print("\nCurrent Inventory:")
        if not inventory:
            print("Inventory is empty.")
        else:
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
        print("----------------------")
    
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
