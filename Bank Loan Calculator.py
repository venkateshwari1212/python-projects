""""Calculate monthly payments for a loan based on principal,
 rate, and time"""

# Get user input for loan details
principal = float(input("Enter the loan amount (Principal): "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the loan term (in years): "))

# Convert annual interest rate to monthly and loan term to months
monthly_rate = (annual_rate / 100) / 12
num_payments = years * 12

# Calculate monthly payment using the formula
if monthly_rate > 0:  # To avoid division by zero for 0% interest loans
    monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
else:
    monthly_payment = principal / num_payments  # Simple division for 0% interest loans

# Display result
print("\n--- Loan Payment Details ---")
print(f"Loan Amount: ${principal:.2f}")
print(f"Annual Interest Rate: {annual_rate:.2f}%")
print(f"Loan Term: {years} years")
print(f"Monthly Payment: ${monthly_payment:.2f}")
