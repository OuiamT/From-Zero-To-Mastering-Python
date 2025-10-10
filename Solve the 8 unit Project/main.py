"""Hangman game.

This script runs a text-based Hangman game where the computer chooses a random
fruit, and the player must guess letters until the word is completed or all
lives are lost. The game displays ASCII art to represent the hangman’s state
after each wrong guess.

Attributes:
    HANGMANPICS (list[str]): ASCII art for the hangman stages.
    fruits (list[str]): List of possible fruits to guess.
    computer_choice (str): Randomly selected fruit word.
    fruit (list[str]): Current state of the guessed word with underscores.
    LIVES (int): Number of remaining incorrect guesses allowed.
    gussed_letters (list[str]): Letters already guessed by the player.
"""

import random
from hangman_art import HANGMANPICS
from hangman_words import fruits


computer_choice = random.choice(fruits)
# todo --> تخمين فاكهة عشوائية
# todo --> عدد الخانات متطابق مع حروف الكلمة
# fruit = []
# for letter in ComputerChoice:
#     fruit += "_"    or fruit.append("_")
fruit = ["_"] * len(computer_choice)  
# todo اختصار ثلاثة اسطر
# fruit["_" for letter in computerchoice]

LIVES = 6
# todo الحروف سبق تخمينها
gussed_letters = []
print(HANGMANPICS[0])
while computer_choice != "".join(fruit) and LIVES > 0:  # or while "_" in fruit:
    print(" ".join(fruit))
    gussed = input("Please guess a letter:  ").lower().strip()
    print()
# todo هل الحرف تم تخمينه من قبل
    if gussed in gussed_letters:
        print(f"You already gussed that. Try agin  \nYou have {LIVES} more tries")
        continue

    else:
        gussed_letters.append(gussed)

# todo --> تبديل الخانة بالحرف الصحيح
    for position in range(len(computer_choice)):
        if gussed == computer_choice[position]:
            fruit[position] = gussed

    if gussed not in computer_choice:
        LIVES -= 1
        print(HANGMANPICS[6 - LIVES])
        print(f" you have {LIVES} more tries")

    else:
        print(f" you have {LIVES} more tries")

if LIVES == 0:
    print(
        """\n********
YOU LOSE
********
=========
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
    )
else:
    print(
        """\n********
YOU WIN
********"""
    )
