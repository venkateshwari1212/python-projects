"""Write a program to book movie tickets by selecting movie,
 time, and number of seats. Prints the tickets with price"""

# Recent Telugu movie releases and their ticket prices
movies = {
    "1": {"name": "Pelli Kani Prasad", "price": 120},
    "2": {"name": "Tuk Tuk", "price": 150},
    "3": {"name": "Shanmuka", "price": 130},
    "4": {"name": "Court – State vs a Nobody", "price": 140}
}

# Showtimes
showtimes = {
    "1": "10:00 AM",
    "2": "1:00 PM",
    "3": "4:00 PM",
    "4": "7:00 PM",
    "5": "10:00 PM"
}

# Display movie options
print("\nAvailable Telugu Movies:")
for key, movie in movies.items():
    print(f"{key}. {movie['name']} - ₹{movie['price']} per ticket")

# User selects a movie
movie_choice = input("\nSelect a movie (1-4): ")
if movie_choice not in movies:
    print("Invalid movie selection!")
    exit()

# Display available showtimes
print("\nAvailable Showtimes:")
for key, time in showtimes.items():
    print(f"{key}. {time}")

# User selects a showtime
showtime_choice = input("\nSelect a showtime (1-5): ")
if showtime_choice not in showtimes:
    print("Invalid showtime selection!")
    exit()

# User inputs the number of tickets
try:
    num_tickets = int(input("\nEnter the number of tickets: "))
    if num_tickets <= 0:
        raise ValueError
except ValueError:
    print("Invalid number of tickets!")
    exit()

# Calculate total price
ticket_price = movies[movie_choice]["price"]
total_price = num_tickets * ticket_price

# Print the ticket details
print("\n----- Your Movie Ticket -----")
print(f"Movie: {movies[movie_choice]['name']}")
print(f"Showtime: {showtimes[showtime_choice]}")
print(f"Tickets: {num_tickets}")
print(f"Total Price: ₹{total_price}")
print("Enjoy your movie!")

