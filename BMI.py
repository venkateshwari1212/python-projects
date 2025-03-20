"""Create a Python program that calculates the Body Mass
 Index (BMI) based on the user's height and weight. The
 BMI can be calculated using the following formula:
 The program should prompt the user to input their weight
 and height, calculate the BMI using the above formula,
 and then categorize the BMI according to standard ranges:
 Underweight: BMI < 18.5
 Normal weight: 18.5 <= BMI < 24.9
 Overweight: 25 <= BMI < 29.9
 Obesity: BMI >= 30
 The program should then display the BMI value along with
 the corresponding category"""

# Get user input for weight (kg) and height (cm)
try:
    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))
    
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive values.")

    # Convert height from cm to meters
    height_m = height_cm / 100

except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Calculate BMI
bmi = weight / (height_m ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Display the results
print("\n----- BMI Calculation Result -----")
print(f"Your BMI: {bmi:.2f}")
print(f"Category: {category}")
