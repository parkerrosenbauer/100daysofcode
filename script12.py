# Day 12 of 100 Days of Code Challenge
# Number Guessing Game
import random


def evaluate_guess(guess):
    """looks to see if the guess is greater, equal to, or lower than the number"""
    global runs_left
    if guess > number:
        print("Too high.\nGuess again.")
        runs_left -= 1
    elif guess < number:
        print("Too low.\nGuess again.")
        runs_left -= 1
    else:
        runs_left = 0


# starting message
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# generate random number
number = random.randint(1, 100)

# set amount of guesses based on chosen difficulty level
if difficulty == 'easy':
    runs_left = 10
elif difficulty == 'hard':
    runs_left = 5
else:
    print("You did not enter a valid level of difficulty.")

# run the game until the number is guessed or guesses run out
while runs_left > 0:
    print(f"You have {runs_left} attempts remaining to guess the number.")
    attempt = int(input("Make a guess: "))
    evaluate_guess(attempt)

# final statement of win/loss
if attempt == number:
    print(f"You got it! The number was {number}.")
else:
    print("You ran out of guesses. You lose.")
