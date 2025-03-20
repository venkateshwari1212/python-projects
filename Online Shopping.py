# Simulate a shopping cart where users can add, remove, and
#  view items.

cart = {}  # Dictionary to store items and their quantities

while True:
    print("\nOptions: add, remove, view, exit")
    action = input("Enter your action: ").strip().lower()

    if action == "add":
        item = input("Enter item name: ").strip()
        quantity = int(input("Enter quantity: "))
        
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

        print(f"Added {quantity} of {item} to the cart.")

    elif action == "remove":
        item = input("Enter item name to remove: ").strip()

        if item in cart:
            quantity = int(input("Enter quantity to remove: "))

            if cart[item] > quantity:
                cart[item] -= quantity
                print(f"Removed {quantity} of {item}.")
            else:
                del cart[item]
                print(f"Removed {item} completely from the cart.")
        else:
            print(f"{item} is not in the cart.")

    elif action == "view":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your shopping cart:")
            for item, quantity in cart.items():
                print(f"- {item}: {quantity}")

    elif action == "exit":
        print("Exiting the shopping cart. Thank you!")
        break

    else:
        print("Invalid option. Please try again.")

