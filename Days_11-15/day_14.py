# Day 14 of 100 Day Code Challenge
# Higher Lower Game
from game_data import data
from higherlower_art import logo
import random
import os

a = ""
b = ""
a_count = 0
b_count = 0
score = 0
start = True


def clear():
    os.system('cls')
    print(logo)


def celebrity(option):
    """formats celebrity data and updates the option score"""
    global a_count
    global b_count
    celeb = random.choice(data)

    # update follower count based on celebrity data
    if option == "A":
        a_count = celeb["follower_count"]
    elif option == "B":
        b_count = celeb["follower_count"]

    # return f-string with celebrity data
    name = celeb["name"]
    desc = celeb["description"]
    cntry = celeb["country"]
    return f"{name}, a {desc}, from {cntry}"


def player_right(player_choice):
    """returns true if player chose correctly"""
    correct = True

    # determine what the player's choice was
    if player_choice == 'A':
        player_choice = a_count
    elif player_choice == 'B':
        player_choice = b_count

    # find the highest value between a and b
    highest = max(a_count, b_count)

    # change correct to false if the player did not pick the highest value
    if highest > player_choice:
        correct = False

    return correct


def game():
    global start
    global a_count
    global b_count
    global a
    global b
    global score

    # assign options a and b
    if start:
        clear()
        a = celebrity("A")
    b = celebrity("B")

    # make sure a and b do not have the same score
    while a_count == b_count:
        b = celebrity("B")

    # display options
    print("Compare A: " + a)
    print("VS.")
    print("Against B: " + b)

    # user input
    choice = input("Who has more followers? Type 'A' or 'B': ")

    # is true if the player was correct, false if not
    answer = player_right(choice)

    if answer:
        score += 1
        clear()
        print(f"You're right! Current score: {score}")
        start = False
        a = b
        a_count = b_count
        game()
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")


game()
