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

from collections import deque

history = deque(maxlen=5)  # Stores the last five conversions

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. View History")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        result = f"{celsius}°C = {fahrenheit:.2f}°F"
        history.append(result)
        print(result)
        
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        result = f"{fahrenheit}°F = {celsius:.2f}°C"
        history.append(result)
        print(result)
        
    elif choice == '3':
        print("\nLast Five Conversions:")
        for record in history:
            print(record)
        
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")
