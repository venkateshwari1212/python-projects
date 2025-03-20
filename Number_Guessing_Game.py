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

number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Too Low! Try again.")
        elif user_guess > number_to_guess:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {number_to_guess}")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
