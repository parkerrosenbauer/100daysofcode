# Day 4 of 100 Days of Code Challenge
# Rock Paper Scissors
import random

# graphics
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Player Choice
player_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))


if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
else:
    print(scissors)

# Computer Choice
computer_choice = random.randint(0, 2)

print("Computer chose: ")
if computer_choice == 0:
    print(rock)
    if player_choice == 1:
        print("You win!")
    elif player_choice == 2:
        print("You lose.")
    else:
        print("It's a draw.")
elif computer_choice == 1:
    print(paper)
    if player_choice == 2:
        print("You win!")
    elif player_choice == 0:
        print("You lose.")
    else:
        print("It's a draw.")
else:
    print(scissors)
    if player_choice == 0:
        print("You win!")
    elif player_choice == 1:
        print("You lose.")
    else:
        print("It's a draw.")
