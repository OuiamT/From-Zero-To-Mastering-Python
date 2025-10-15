from twenty_one_art import logo
import os
import time
import random

BLACK_JACK = 21

def clear_scrine():
    os.system ("cls" if os.name == "nt" else "clear")


def another_cards_for_me(cards, my_cards, computer_cards):
    while input("Get another card? y/n:\t").lower() == "y":
        if sum(my_cards) < 17:
            my_cards.append(cards[len(my_cards) + len(computer_cards)])
            print(f"Your cards are {my_cards}, current score is {sum(my_cards)}")
            print(f"Computer's first card is {computer_cards[0]}")
            print("\n\n")
        else:
            print(f"Sorry your score is grater than 17")
            break

def final_cards(cards, my_cards, computer_cards):
    while sum(computer_cards) < 17:
        computer_cards.append(cards[len(my_cards) + len(computer_cards)])
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
    
def card_A():
    pass


while True:
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]
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
    