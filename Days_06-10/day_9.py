# Day 9 of 100 Days of Code Challenge
# Silent Auction
import os
from auction_art import logo

bid_dict = {}
more_bidders = "y"

# clears terminal after each bidder


def clear():
    os.system('cls')


clear()
print(logo)
print("Welcome to the secret auction program.")

# runs program as long as there are more bidders
while more_bidders == "y":
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    bid_dict[name] = bid
    more_bidders = input(
        "Are there more bidders? Type 'y' for yes, 'n' for no. ")
    clear()

# find highest bidder
high_amt = max(bid_dict.values())
high_bidder = max(bid_dict, key=bid_dict.get)

print(f"The highest bidder was {high_bidder} with a bid of ${high_amt}!")
