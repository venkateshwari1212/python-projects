"""
Create a Python program to sell tickets for an event where
 the user can choose the type of ticket (VIP, Regular, or
 Economy) and specify the number of tickets they want to
 purchase. The program should display the price for each
 ticket type, calculate the total cost based on the number of
 tickets, and then prompt the user to confirm the purchase.
 The ticket prices can be predefined, for example:
 VIP: $100
 Regular: $50
 Economy: $20
 After the user selects the ticket type and number, the
 program should display the total price for the tickets and
 confirm the transaction.
"""
ticket_prices = {
    "VIP": 100,
    "Regular": 50,
    "Economy": 20
}

print("Ticket Prices:")
for ticket, price in ticket_prices.items():
    print(f"{ticket}: ${price}")

while True:
    ticket_type = input("\nEnter the type of ticket (VIP, Regular, Economy): ").strip().title()
    if ticket_type not in ticket_prices:
        print("Invalid ticket type. Please choose from VIP, Regular, or Economy.")
        continue
    
    try:
        num_tickets = int(input("Enter the number of tickets: "))
        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")
            continue
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue
    
    total_cost = ticket_prices[ticket_type] * num_tickets
    print(f"\nTotal cost for {num_tickets} {ticket_type} ticket(s): ${total_cost}")
    
    confirm = input("Confirm purchase? (yes/no): ").strip().lower()
    if confirm == "yes":
        print("Purchase confirmed. Enjoy the event!")
        break
    else:
        print("Purchase canceled.")
        break
