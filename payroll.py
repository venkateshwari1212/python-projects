"""
Create a Python program that calculates an employee's
salary after accounting for deductions like tax and adding
bonuses. The program should allow the user to input the
employee's base salary, tax percentage, and any bonuses.
It should then calculate the amount deducted for taxes,
add the bonus to the salary, and display the final salary
after deductions and bonuses. The tax can be calculated
as a percentage of the base salary, and the final salary will
be the sum of the base salary minus tax plus any bonus. 
"""

# Get user input for salary details
base_salary = float(input("Enter the employee's base salary: "))
tax_percentage = float(input("Enter the tax percentage: "))
bonus = float(input("Enter any bonus amount: "))

# Calculate tax deduction
tax_amount = (tax_percentage / 100) * base_salary

# Calculate final salary
final_salary = base_salary - tax_amount + bonus

# Display results
print("\n--- Salary Calculation ---")
print(f"Base Salary: ${base_salary:.2f}")
print(f"Tax Deducted ({tax_percentage}%): ${tax_amount:.2f}")
print(f"Bonus Added: ${bonus:.2f}")
print(f"Final Salary: ${final_salary:.2f}")
