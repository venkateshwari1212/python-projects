"""
Create a Python program that converts currency from USD
(United States Dollar) to INR (Indian Rupee), EUR (Euro), and
GBP (British Pound) based on provided exchange rates. The
program should prompt the user to input the amount in USD
and the exchange rates for INR, EUR, and GBP. It will then
calculate and display the converted amounts for each of these
currencies. The user should also be able to input new exchange
rates if desired.
"""
while True:
    try:
        usd_amount = float(input("Enter the amount in USD: "))
        inr_rate = float(input("Enter the exchange rate for USD to INR: "))
        eur_rate = float(input("Enter the exchange rate for USD to EUR: "))
        gbp_rate = float(input("Enter the exchange rate for USD to GBP: "))

        inr_amount = usd_amount * inr_rate
        eur_amount = usd_amount * eur_rate
        gbp_amount = usd_amount * gbp_rate

        print("\nConverted Amounts:")
        print(f"INR: {inr_amount:.2f}")
        print(f"EUR: {eur_amount:.2f}")
        print(f"GBP: {gbp_amount:.2f}")
    
        choice = input("Do you want to enter new exchange rates? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter numeric values.")
