# # Initialize total cost
# total_cost = 0

# print("Enter the cost of each item (Enter 0 to finish):")

# # Keep taking inputs until the user enters 0
# while True:
#     cost = float(input("Enter item cost: "))
    
#     if cost == 0:  # Stop when user enters 0
#         break
        
#     total_cost += cost

# # Apply a 10% service charge
# service_charge = total_cost * 0.10
# final_total = total_cost + service_charge

# # Display the results
# print("\n----- BILL SUMMARY -----")
# print(f"Total Cost: ${total_cost:.2f}")
# print(f"Service Charge (10%): ${service_charge:.2f}")
# print(f"Final Total: ${final_total:.2f}")


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

# account_balance = 1000 

# while True:
#     print("\n Welcome to HDFC ATM Machine")
#     print("1. Balance enquiry")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
    
#     choose_option = input("Enter your choice (1-4): ")
    
#     if choose_option == '1':
#         print(f"Your current balance is: ${account_balance}")
    
#     elif choose_option == '2':
#         amount = float(input("Enter amount to deposit: "))
#         if amount > 0:
#             account_balance += amount
#             print(f"${amount} deposited successfully.")
#             print(f"Updated balance: ${account_balance}")
#         else:
#             print("Invalid deposit amount.")
    
#     elif choose_option == '3':
#         amount = float(input("Enter amount to withdraw: "))
#         if amount > account_balance:
#             print("Insufficient funds! Withdrawal failed.")
#         elif amount > 0:
#             account_balance -= amount
#             print(f"${amount} withdrawn successfully.")
#             print(f"Updated balance: ${account_balance}")
#         else:
#             print("Invalid withdrawal amount.")
    
#     elif choose_option == '4':
#         print("Thank you for using the HDFC ATM. Goodbye!")
#         break
    
#     else:
#         print("Invalid choice! Please enter a number between 1 and 4.")



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
manipulation and user interaction in Python"

"""

# inventory = {
#     "apples": 10,
#     "bananas": 15,
#     "oranges": 12
# }

# while True:
#     print("\nGrocery Store Inventory")
#     print("1. Update item quantity")
#     print("2. Add a new item")
#     print("3. Remove an item")
#     print("4. View inventory")
#     print("5. Exit")
    
#     choice = input("Enter your choice (1-5): ")
    
#     if choice == '1':
#         item = input("Enter the item name to update: ").lower()
#         if item in inventory:
#             quantity = int(input("Enter the new quantity: "))
#             inventory[item] = quantity
#             print(f"Updated {item} quantity to {quantity}.")
#         else:
#             print("Item not found in inventory.")
    
#     elif choice == '2':
#         item = input("Enter the new item name: ").lower()
#         if item in inventory:
#             print("Item already exists. Use update option instead.")
#         else:
#             quantity = int(input("Enter the quantity: "))
#             inventory[item] = quantity
#             print(f"Added {item} with quantity {quantity}.")
    
#     elif choice == '3':
#         item = input("Enter the item name to remove: ").lower()
#         if item in inventory:
#             del inventory[item]
#             print(f"Removed {item} from inventory.")
#         else:
#             print("Item not found in inventory.")
    
#     elif choice == '4':
#         print("\nCurrent Inventory:")
#         for item, quantity in inventory.items():
#             print(f"{item}: {quantity}")
    
#     elif choice == '5':
#         print("Exiting the program. Goodbye!")
#         break
    
#     else:
#         print("Invalid choice! Please enter a number between 1 and 5.")


"""
Develop a Python program to manage a library system
with options to add, remove, and search for books.
"""

# library = {}

# def display_menu():
#     print("\nLibrary Management System")
#     print("1. Add a book")
#     print("2. Remove a book")
#     print("3. Search for a book")
#     print("4. View all books")
#     print("5. Exit")

# def add_book():
#     book = input("Enter the book title to add: ").strip().title()
#     if book in library:
#         print("Book already exists in the library.")
#     else:
#         author = input("Enter the author's name: ").strip().title()
#         library[book] = author
#         print(f"Added '{book}' by {author} to the library.")

# def remove_book():
#     book = input("Enter the book title to remove: ").strip().title()
#     if book in library:
#         del library[book]
#         print(f"Removed '{book}' from the library.")
#     else:
#         print("Book not found in the library.")

# def search_book():
#     book = input("Enter the book title to search: ").strip().title()
#     if book in library:
#         print(f"'{book}' by {library[book]} is available in the library.")
#     else:
#         print("Book not found in the library.")

# def view_books():
#     if library:
#         print("\nBooks in the Library:")
#         for book, author in library.items():
#             print(f"'{book}' by {author}")
#     else:
#         print("The library is empty.")

# while True:
#     display_menu()
#     choice = input("Enter your choice (1-5): ")
    
#     if choice == '1':
#         add_book()
#     elif choice == '2':
#         remove_book()
#     elif choice == '3':
#         search_book()
#     elif choice == '4':
#         view_books()
#     elif choice == '5':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice! Please enter a number between 1 and 5.")

"""
Create Cre a Python program that functions as a temperature
converter, allowing the user to convert temperatures between
Celsius and Fahrenheit. The program should store and display
the last five conversions, showing both the input value and the
result. The user should be able to choose the direction of
conversion (Celsius to Fahrenheit or Fahrenheit to Celsius), and
the program should maintain a history of the last five
conversions, displaying the most recent ones at the end of each
conversion.
"""
# from collections import deque

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# history = deque(maxlen=5)  # Stores the last 5 conversions

# while True:
#     print("\nTemperature Converter")
#     print("1. Convert Celsius to Fahrenheit")
#     print("2. Convert Fahrenheit to Celsius")
#     print("3. View last 5 conversions")
#     print("4. Exit")
    
#     choice = input("Enter your choice (1-4): ")
    
#     if choice == '1':
#         try:
#             celsius = float(input("Enter temperature in Celsius: "))
#             fahrenheit = celsius_to_fahrenheit(celsius)
#             print(f"{celsius}°C = {fahrenheit:.2f}°F")
#             history.append(f"{celsius}°C = {fahrenheit:.2f}°F")
#         except ValueError:
#             print("Invalid input! Please enter a numerical value.")
    
#     elif choice == '2':
#         try:
#             fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#             celsius = fahrenheit_to_celsius(fahrenheit)
#             print(f"{fahrenheit}°F = {celsius:.2f}°C")
#             history.append(f"{fahrenheit}°F = {celsius:.2f}°C")
#         except ValueError:
#             print("Invalid input! Please enter a numerical value.")
    
#     elif choice == '3':
#         if history:
#             print("\nLast 5 conversions:")
#             for record in history:
#                 print(record)
#         else:
#             print("No conversions yet.")
    
#     elif choice == '4':
#         print("Exiting the program. Goodbye!")
#         break
    
#     else:
#         print("Invalid choice! Please enter a number between 1 and 4.")


"""
Create a Python program where the computer randomly
selects a number between 1 and 100, and the user has to
guess the number. After each guess, the program should
provide feedback such as 'Too High' if the guess is greater
than the number, or 'Too Low' if the guess is smaller. The
program should continue prompting the user for guesses
until the correct number is guessed, and then it should
congratulate the user for finding the number.
"""
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            if user_guess < number_to_guess:
                print("Too Low! Try again.")
            elif user_guess > number_to_guess:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
