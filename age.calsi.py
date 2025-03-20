# Calculate a person's age based on their date of birth.
from datetime import datetime

birth_date = input("Enter your date of birth (YYYY-MM-DD): ").strip()
try:
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
