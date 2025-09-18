# function with parameters and arguments
# def fct(parameter):
#   print(parameter)

# fct(argument)
# positional arguments
# ??!! the difference between methode and function
# the methode index() (the difference between this and find())

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
print("-" * 20)
print()

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
print("-" * 20)
print()


# 3

# Input
# "Hello"

# Needed Output:
# "Jgnnq" 
# example: H --> I --> J
#          e --> f --> g
#          l --> m --> n


import string

new_sentance = []
alphabet = string.ascii_letters

word = input("Enter a sentance: ").strip()
for character in word:
    old_index = alphabet.index(character)
    new_index = old_index + 2
    new_sentance.append(alphabet[new_index])

print("".join(new_sentance))
print("-" * 20)
print()


# 4
# Input:
# 'zoo'

# Needed Output:
# 'bqq'
# Solving the 'index out of range' problem for the last alphabets.


import string

new_sentance = []
alphabet = string.ascii_lowercase

word = input("Enter a sentance: ").strip().lower()
for character in word:
    old_index = alphabet.index(character)
    new_index = (old_index + 2) % 26
    new_sentance.append(alphabet[new_index])

print("".join(new_sentance))
print("-" * 20)
print()


# 5
# Input:
# 'the king is sleeping!!?

# Needed Output:
# ''

import string

encrypted_sentance = ""

alphabet = string.ascii_lowercase
punctuation = string.punctuation
sentance = input("Enter your sentance:\n").strip().lower()
number = int(input("Enter the number for encrpting:\t"))

for character in sentance:
    if character == " ":
        encrypted_sentance += " "

    elif character in punctuation:
        encrypted_sentance += character

    else:
        old_index = alphabet.index(character)
        new_index = (old_index + number) % 26
        encrypted_sentance += alphabet[new_index]

print(f"The new sentance after encrpting is:\n{encrypted_sentance}")