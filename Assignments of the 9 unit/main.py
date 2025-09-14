# function with parameters and arguments
# def fct(parameter):
#   print(parameter)

# fct(argument)
# positional arguments

# 1

# Input:
# multiply(7)

# Needed output:
# 7 x 1 = 7
# 7 x 2 = 14 
# 7 x 3 = 21 
# 7 x 4 = 28 
# 7 x 5 = 35 
# 7 x 6 = 42 
# 7 x 7 = 49 
# 7 x 8 = 56 
# 7 x 9 = 63 
# 7 x 10 = 70

def multiplay(number):
    for a in range(1, 11):
        print(f"{number} x {a} = {number * a}")

multiplay(7)

# 2
# Needed Output:
# Hi, your name is: Mohamed")
# print(f"Your age is: 22 years old")
# print(f"You live in: Morocco


def welcome(name, age, natinality):
    print(f"Hi, your name is: {name}")
    print(f"Your age is: {age} years old")
    print(f"You live in: {natinality}")

welcome(age=22, natinality="Morocco", name="Mohamed")