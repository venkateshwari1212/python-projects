"""
Write a Python program to calculate the total bill for a
customer. The program should ask for the cost of
individual items, apply a 10% service charge, and
calculate the total.
"""
# Initialize total cost
total_cost = 0

print("Enter the cost of each item (Enter 0 to finish):")

# Keep taking inputs until the user enters 0
while True:
    cost = float(input("Enter item cost: "))
    
    if cost == 0:  # Stop when user enters 0
        break
        
    total_cost += cost

# Apply a 10% service charge
service_charge = total_cost * 0.10
final_total = total_cost + service_charge

# Display the results
print("\n----- BILL SUMMARY -----")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Service Charge (10%): ${service_charge:.2f}")
print(f"Final Total: ${final_total:.2f}")
