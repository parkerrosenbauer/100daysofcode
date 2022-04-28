# Day 3 of 100 Days of Code Challenge
# Choose your own adventure game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Intro
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Choice One
choice_one = input(
    "You come across a fork in the road. Would you like to go left or right?\n")
choice_one = choice_one.lower()

if choice_one != "left":
    print("You fell into a hole. You died.")
    quit()
else:
    print("You make your way towards a lake.")

# Choice Two
choice_two = input(
    "Type 'swim' if you'd like to swim across, type 'wait' if you'd like to wait for a boat.\n")
choice_two = choice_two.lower()

if choice_two != "wait":
    print("You were attacked by trout. You died.")
    quit()
else:
    print("You wait for a boat and made it successfully across the lake.")

# Choice Three
choice_three = input(
    "You come across a house with three doors. You see a red, yellow, and blue one. Type the color of door you wish to enter.\n")
choice_three = choice_three.lower()

if choice_three == "yellow":
    print("You found a pile of treasure, you win!")
elif choice_three == "blue":
    print("You were attacked by beasts. You died.")
elif choice_three == "red":
    print("The room was filled with fire. You died.")
else:
    print("You have left the simulation. You died.")
