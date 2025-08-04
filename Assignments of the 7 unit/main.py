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
at_goal() --> reached the goal
front_is_clear() --> you have no barrier in front of you
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
computer_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10:  "))
if guess > 10 or guess < 1:
    print("Try again and choice a number between 1 and 10")
else:
    while computer_guess != guess:
        if guess < computer_guess:
            guess = int(input("Too low! Guess again:  "))
        else:
            guess = int(input("Too high! Guess again:  "))
    print("Congratulation! You guess the number!")

# 9
# Needed Output
"""
Solution of Hurdle2:

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

while not at_goal():
    jump()
"""