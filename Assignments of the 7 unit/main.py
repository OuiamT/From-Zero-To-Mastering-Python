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
