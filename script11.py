# Day 11 of 100 Days of Code Challenge
# Blackjack
from blackjack_art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    """clears the console"""
    os.system('cls')


def summing(hand):
    """to calculate if the ace should represent 1 or 11"""
    while sum(hand) > 21:
        if 11 not in hand:
            return sum(hand)
        else:
            x = hand.index(11)
            hand[x] = 1
    return sum(hand)


def choose_cards_user():
    """randomly generates cards for the user"""
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    return[card1, card2]


def choose_cards_dealer():
    """randomly generates cards for the dealer"""
    card1 = cards[random.randint(0, len(cards)-1)]
    card2 = cards[random.randint(0, len(cards)-1)]
    hand = [card1, card2]
    while summing(hand) < 16:
        card3 = cards[random.randint(0, len(cards)-1)]
        hand.append(card3)
    return hand


clear()
play = input(
    "Would you like to play Blackjack? Type 'y' for yes, 'n' for no: ").lower()

while play == 'y':
    clear()
    print(logo)

    # display players cards
    player_hand = choose_cards_user()
    player_score = summing(player_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")

    # generate and display computer's first card
    computer_hand = choose_cards_dealer()
    computer_score = summing(computer_hand)
    print(f"Computer's first card: {computer_hand[0]}")

    # ask player for an extra card
    extra = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while extra == 'y':
        # add a card to player hand
        player_hand.append(random.choice(cards))
        player_score = summing(player_hand)

        # evaluate sum of player hand
        if player_score <= 21:
            print(f"Your cards: {player_hand}, current score: {player_score}")
            extra = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
        else:
            extra = 'n'

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(
        f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if player_score > 21:
        print("Bust. You lose.")
    elif computer_score > 21:
        print("The computer busted, you win!")
    elif computer_score > player_score:
        print("The computer has bested you. You lose.")
    elif computer_score == player_score:
        print("Draw.")
    else:
        print("You win!")

    play = input(
        "Would you like to play Blackjack? Type 'y' for yes, 'n' for no: ").lower()
