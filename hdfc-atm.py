"""
Create a Python program that simulates an ATM machine with
basic functionalities. The program should allow the user to
check their account balance, deposit money, or withdraw
funds. It should start with an initial balance of 1000. The user
can perform these actions in a loop until they choose to exit.
When attempting to withdraw money, the program should
ensure that the user does not exceed the available balance and
display an appropriate message in case of insufficient funds. 
"""

account_balance = 1000 

while True:
    print("\n Welcome to HDFC ATM Machine")
    print("1. Balance enquiry")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choose_option = input("Enter your choice (1-4): ")
    
    if choose_option == '1':
        print(f"Your current balance is: ${account_balance}")
    
    elif choose_option == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            account_balance += amount
            print(f"${amount} deposited successfully.")
            print(f"Updated balance: ${account_balance}")
        else:
            print("Invalid deposit amount.")
    
    elif choose_option == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > account_balance:
            print("Insufficient funds! Withdrawal failed.")
        elif amount > 0:
            account_balance -= amount
            print(f"${amount} withdrawn successfully.")
            print(f"Updated balance: ${account_balance}")
        else:
            print("Invalid withdrawal amount.")
    
    elif choose_option == '4':
        print("Thank you for using the HDFC ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

