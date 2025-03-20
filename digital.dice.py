"""
 Create a Python program that simulates rolling a digital dice.
 The program should allow the user to roll the dice, and based
 on the outcome, track the number of wins and losses. 
For example:
 A win is recorded if the dice roll matches a pre-determined
 "winning number" (for example, 6).
 1.
 A loss is recorded if the dice roll is any other number. 2.
 The program should continue asking the user if they want to
 roll again, and it should keep track of the total wins and losses.
 After the user decides to stop, the program should display the
 final score, showing the number of wins and losses. 
"""

import random

# Predefined winning number
winning_number = 6

# Initialize win/loss counters
wins = 0
losses = 0

# Game loop
while True:
    input("Press Enter to roll the dice...")  # Wait for user input to roll
    roll = random.randint(1, 6)  # Roll the dice

    print(f"\nYou rolled: {roll}")

    if roll == winning_number:
        print("Congratulations! You win!")
        wins += 1
    else:
        print("Sorry, you lose!")
        losses += 1

    # Ask if the user wants to play again
    play_again = input("\nDo you want to roll again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

# Display final score
print("\n----- Final Score -----")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print("Thanks for playing!")

