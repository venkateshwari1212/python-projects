"""
Create a Python program that generates a simple invoice for a customer. The program
 should allow the user to input the name, price, and quantity of items purchased. It should
 then calculate the total cost for each item (price × quantity), display the itemized list, and
 include a final total for the invoice. If applicable, it should apply the discount from the
 previous section to the total cost and display the final amount.
 Here's a possible structure for the invoice:
 Item name 1.
 Item price 2.
 Item quantity 3.
 Total for that item 4.
 Subtotal of all items 5.
 Discount applied (if any) 6.
 Final amount to be paid
"""
# List to store items
items = []

# Input item details
while True:
    name = input("Enter item name (or type 'done' to finish): ")
    if name.lower() == "done":
        break

    try:
        price = float(input(f"Enter price of '{name}': $"))
        quantity = int(input(f"Enter quantity of '{name}': "))

        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")

        total_price = price * quantity  # Calculate total for item
        items.append((name, price, quantity, total_price))  # Store item details
    except ValueError as e:
        print(f"Invalid input: {e}")
        continue

# Calculate subtotal
subtotal = sum(item[3] for item in items)

# Determine discount percentage
if subtotal < 50:
    discount_percentage = 0  # No discount
elif 50 <= subtotal <= 100:
    discount_percentage = 10  # 10% discount
elif 100 < subtotal <= 200:
    discount_percentage = 15  # 15% discount
else:
    discount_percentage = 20  # 20% discount

# Calculate discount amount and final total
discount_amount = (discount_percentage / 100) * subtotal
final_amount = subtotal - discount_amount

# Display invoice
print("\n----- Invoice -----")
print("{:<20} {:<10} {:<10} {:<10}".format("Item Name", "Price", "Quantity", "Total"))
print("-" * 50)

for item in items:
    print("{:<20} ${:<9.2f} {:<10} ${:<10.2f}".format(item[0], item[1], item[2], item[3]))

print("-" * 50)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount Applied: {discount_percentage}%")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Amount to Pay: ${final_amount:.2f}")
print("-" * 50)
print("Thank you for shopping with us!")
