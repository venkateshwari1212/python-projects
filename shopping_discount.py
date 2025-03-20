"""
Apply Different Discount Percentages Based on Purchase Amount
 Create a Python program that applies different discount
 percentages based on the total purchase amount. The program
 should prompt the user for the total purchase amount and then
 apply the following discount rules:
 Purchase amount < $50: No discount. 1.
 Purchase amount between $50 and $100: 10% discount. 2.
 Purchase amount between $100 and $200: 15% discount. 3.
 Purchase amount > $200: 20% discount. 4.
 The program should calculate the discount based on the total and
 display the final amount after applying the discount.
"""

# Get user input for total purchase amount
try:
    total_amount = float(input("Enter the total purchase amount: $"))

    if total_amount < 0:
        raise ValueError("Amount cannot be negative.")

    # Apply discount based on purchase amount
    if total_amount < 50:
        discount_percentage = 0  # No discount
    elif 50 <= total_amount <= 100:
        discount_percentage = 10  # 10% discount
    elif 100 < total_amount <= 200:
        discount_percentage = 15  # 15% discount
    else:
        discount_percentage = 20  # 20% discount

    # Calculate discount amount and final amount
    discount_amount = (discount_percentage / 100) * total_amount
    final_amount = total_amount - discount_amount

    # Display results
    print("\n----- Bill Summary -----")
    print(f"Total Purchase Amount: ${total_amount:.2f}")
    print(f"Discount Applied: {discount_percentage}%")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Amount to Pay: ${final_amount:.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")
