"""
Create a Python program that calculates the fare for a
 journey based on the distance traveled and the type of
 passenger (adult, child, or senior). The program should
 prompt the user to input the distance traveled (in
 kilometers) and the type of passenger. Based on this
 input, the fare will be calculated using predefined rates for
 each type of passenger. For example:
 Adult: $5 per kilometer
 Child: $3 per kilometer
 Senior: $4 per kilometer
 The program should apply the appropriate fare rate based
 on the passenger type and distance travelled, then display
 the total fare. Additionally, the program could provide a
 discount for seniors, if applicable
"""

# Predefined fare rates (per km)
fare_rates = {
    "adult": 5,
    "child": 3,
    "senior": 4
}

# Senior discount (optional)
senior_discount = 0.1  # 10% discount for seniors

# Get user input
try:
    distance = float(input("Enter the distance traveled (in km): "))
    passenger_type = input("Enter passenger type (adult/child/senior): ").strip().lower()

    # Validate input
    if distance <= 0:
        raise ValueError("Distance must be a positive number.")
    if passenger_type not in fare_rates:
        raise ValueError("Invalid passenger type! Choose from adult, child, or senior.")

    # Calculate fare
    fare = distance * fare_rates[passenger_type]

    # Apply senior discount if applicable
    if passenger_type == "senior":
        fare -= fare * senior_discount  # Apply 10% discount

    # Display total fare
    print("\n----- Fare Calculation -----")
    print(f"Passenger Type: {passenger_type.capitalize()}")
    print(f"Distance Traveled: {distance} km")
    print(f"Total Fare: ${fare:.2f}")

except ValueError as e:
    print(f"Error: {e}")
