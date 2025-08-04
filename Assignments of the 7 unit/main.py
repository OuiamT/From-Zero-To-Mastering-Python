# why used _ in for loop
# difference between for and while 

# 1
# Needed Output:
# Hello and Welcome to my function!

def my_function():
    print("** Hello and Welcome to my function! **")

my_function()
print("-" * 20)
print()


# 2
# Needed Output:
# Welcome to the program
# Press "Enter" to exit ...
# Thanks for using the program. See you soon!

def welcome():
    print("Welcome to the program")

def bye():
    print("Thanks for using the program. See you soon!")

welcome()
input("Press \"Enter\" to exit ...")
bye()
print("-" * 20)
print()


"""
*** Reeborg's keeyboard ***
move() --> has moved forward
turn_left() --> turn left
"""

# 3
# Needed Output:

"""
We want him to take two steps forward and come back:


move()
move()
turn_left()
turn_left()
move()
move()
"""

# 4
# Needed Output

"""
We want to give us his face (turn right):


turn_left()
turn_left()
turn_left()
"""

# 5
# Needed Output
"""
We want to draw a square:


def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
move()
turn_right()
move()
move()
turn_right()
move()
move()
turn_right()
move()
move()
turn_left()
"""

# 6
# Needed Output
"""
Solution of Hurdle1:


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    turn_right()
    turn_left()
    
    
for _ in range(6):
    jump()
"""

# 7
# Needed Output
# example correct password = 1a2b3c
# Enter your password:
# The code entry password will be repeated until it is correct.

correct_password = "1a2b3c"
entered_password = input("Enter your password:\t")
while entered_password != correct_password:
    print("Invalide password. Try again...")
    entered_password = input("Enter your password again:\t")

print("Correct password")


# 8
# Needed Output
# Guess a number between 1 and 10:  
# It will not stop until you enter the correct number.

import random
computer_choice = random.randint(1, 10)
choice = int(input("Guess a number between 1 and 10:  "))
if choice > 10 or choice < 1:
    print("Try again and choice a number between 1 and 10")
else:
    while computer_choice != choice:
        if choice < computer_choice:
            choice = int(input("Too low! Guess again:  "))
        else:
            choice = int(input("Too high! Guess again:  "))
    print("Congratulation! You guess the number!")