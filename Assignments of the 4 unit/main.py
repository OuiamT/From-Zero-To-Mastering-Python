# 1
import random

my_choice = input("Enter a 4-digit PIN code:\t")
computer_choice = random.randint(1000, 9999)

if len(my_choice) == 4:
    if int(my_choice) == computer_choice:
        print(f"\nPIN code matched. Both chose '{computer_choice}'")
    else:
        print("\nSorry, PIN code did not match.")     
        print(f"The computer generated this PIN: {computer_choice}")
else:
    print("\nPlease enter 4-digits")

print("-" * 30)


# 2
# Needed Output:
# You will choose between two methodes, then you will guess 'Tails' or 'Heads' and check if you are match with computer's guess or not.

import random

# ? introduction :
print("""Welcome to the Coin Guessing Game!
Choose a methode to toss the coin:
1- Using random.randint()
2- Using random.random()""")

choice = int(input("Enter your choice (1 or 2):  "))
my_guess = input("Enter your guess (tails or heads):  ").capitalize()
if my_guess == "Heads" or my_guess == "Tails":

    if choice == 1:
        computer_guess = random.randint(0, 1)
        if computer_guess == 0:
            computer_result = "Tails"
        else :
            computer_result = "Heads"

        #! checking:
        if my_guess == computer_result:
            print(f"Good! you win  \nThe computer's coin toss result was: {computer_result}")
        else :
            print(f"Sorry! you lost  \nThe computer's coin toss result was: {computer_result}")

    elif choice == 2:
        computer_guess = random.random()
        if computer_guess >= 0.5:
            computer_result = "Tails"
        else:
            computer_result = "Heads"

        #! checking:
        if my_guess == computer_result :
            print(f"Good! you win  \nThe compter's coin toss result was: {computer_result}")
        else :
            print(f"Sorry! you lost  \nThe computer's coin toss result was: {computer_result}")

    else:
        print("Ivalide choice! Please select either 1 or 2") 
else:
    print("Ivalide choice! Choose between 'Tails' or 'Heads'")

print("-" * 30)


# 3
# We have a list of colors
# Input -> ["Red", "Green", "Black", "Blue"]
# We will modify it ti become like this:
# Needed Output:
# -> ['Red', 'Green', 'Blue', 'Yellow', 'Pink']

colors = ["Red", "Green", "Black", "Blue"]
colors.append("Yellow")
colors.append("Pink")
colors.remove("Black")
print(colors)
print(f"The first color on our list is '{colors[0]}', and the last color on our list is '{colors[-1]}'")

print("-" * 30)