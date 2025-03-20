# Validate if a given string is a valid email address.
#  Extract the username and domain from an email address

import re

# Function to validate email and extract username & domain
def validate_email(email):
    # Regular expression pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        username, domain = email.split("@")
        print("Valid email address!")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address!")

# Get user input
email = input("Enter your email address: ")
validate_email(email)
