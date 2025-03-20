"""
Create a Python program that implements a calculator
capable of performing addition, subtraction,
multiplication, and division. The program should allow
the user to input two numbers and select the desired
operation. After each calculation, the program should
display the result and store the last three calculations. If
more than three calculations are performed, the oldest
one should be removed to make room for the new one.
"""
from collections import deque

history = deque(maxlen=3)  # Stores last three calculations

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Exit")
    
    choice = input("Select an operation (1-6): ")
    
    if choice == '6':
        print("Exiting calculator. Goodbye!")
        break
    
    if choice == '5':
        print("\nCalculation History:")
        for record in history:
            print(record)
        continue
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select a valid operation.")
        continue
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    
    if choice == '1':
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"
    elif choice == '2':
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"
    elif choice == '3':
        result = num1 * num2
        operation = f"{num1} * {num2} = {result}"
    elif choice == '4':
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
        operation = f"{num1} / {num2} = {result}"
    
    print("Result:", result)
    history.append(operation)
