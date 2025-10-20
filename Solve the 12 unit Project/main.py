"""
Blackjack Console Game
-----------------------------------

This script implements a simple console-based version of the classic Blackjack (also known as Twenty-One)
card game.

The player competes against the computer (dealer) to reach a card total as close to 21 as possible
without exceeding it.
Face cards (J, Q, K) are represented as 10, and Aces (A) can count as 11 or 1 depending on the player's hand.

Modules:
    - os: Used to clear the console screen between rounds.
    - time: Used to create brief pauses for a smoother game experience.
    - random: Used to shuffle the deck of cards.
    - twenty_one_art: Provides a visual ASCII logo for the game.

Constants:
    - BLACK_JACK (int): Target score for winning (21).
    - MAX_OF_TAKE_CARDS (int): Maximum threshold for taking additional cards (17).

Game Steps:
    1. The game shuffles a standard deck represented as numeric values.
    2. Both player and computer are dealt two initial cards.
    3. The player decides whether to draw more cards.
    4. The computer draws automatically according to dealer rules.
    5. The result is displayed, and the player is prompted for another round or not.
"""

from twenty_one_art import logo
import os
import time
import random

BLACK_JACK = 21
MAX_OF_TAKE_CARDS = 17


def clear_scrine():
    os.system("cls" if os.name == "nt" else "clear")


def another_cards_for_me(cards, my_cards, computer_cards):
    while input("Get another card? y/n:\t").lower() == "y":
        if sum(my_cards) < MAX_OF_TAKE_CARDS:
            my_cards.append(cards[len(my_cards) + len(computer_cards)])
            card_A(my_cards)
            print(f"Your cards are {my_cards}, current score is {sum(my_cards)}")
            print(f"Computer's first card is {computer_cards[0]}")
            print("\n\n")
        else:
            print(f"Sorry your score is grater than 17")
            break


def final_cards(cards, my_cards, computer_cards):
    while sum(computer_cards) < MAX_OF_TAKE_CARDS:
        computer_cards.append(cards[len(my_cards) + len(computer_cards)])
        card_A(computer_cards)
    print(f"Your final hand: {my_cards}, with score {sum(my_cards)}")
    print(f"Computer's final hand: {computer_cards}, with score {sum(computer_cards)}")


def result(my_cards, computer_cards):
    if sum(my_cards) == BLACK_JACK or sum(computer_cards) == BLACK_JACK:
        return "*** BLACK JACK ***"
    elif sum(my_cards) > BLACK_JACK and sum(computer_cards) > BLACK_JACK:
        return "None of you want!!🙄😕 Because both have exceeded the permitted total"
    elif sum(my_cards) == sum(computer_cards):
        return "It's tie 😎✨"
    elif sum(my_cards) < BLACK_JACK and sum(computer_cards) < BLACK_JACK:
        if sum(my_cards) > sum(computer_cards):
            return "Congratulation!!!🎇🥳 You WIN...."
        else:
            return "Sorry! 😐😓 You LOSE....\nTry a second round"
    elif sum(my_cards) < BLACK_JACK and sum(computer_cards) > BLACK_JACK:
        return "Computer went over 21, 🎇🥳 You WIN...."
    elif sum(my_cards) > BLACK_JACK and sum(computer_cards) < BLACK_JACK:
        return "You went over 21, 😐😓 You LOSE....\nTry a second round"


def card_A(value):
    if 11 in value:
        if sum(value) > BLACK_JACK:
            value.remove(11)
            value.append(1)


while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    my_cards = [cards[0], cards[1]]
    computer_cards = [cards[2], cards[3]]
    my_choice = input("Press 'Twenty one' game to start....\t").lower()
    clear_scrine()
    time.sleep(4)
    if my_choice == "21" or my_choice == "twenty one":
        print("Starting game ....")
        time.sleep(4)
        print(logo)
        print()
        print(f"Your cards are {my_cards}, current score is {sum(my_cards)}")
        print(f"Computer's first card is {computer_cards[0]}")
        another_cards_for_me(cards, my_cards, computer_cards)
        final_cards(cards, my_cards, computer_cards)
        print()
        print(result(my_cards, computer_cards))
        if input("Do you want to play another round?..y/n:\t").lower() != "y":
            break

    else:
        print("Try againe ....")
        time.sleep(4)
