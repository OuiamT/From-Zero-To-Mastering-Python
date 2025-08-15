# 1
# Needed Output

# We have "apple" like a random fruit
# Please guess a letter: a
# Right
# Wrong
# Wrong
# Wrong
# Wrong

import random

fruits = ("apple", "banana", "pear", "tangerine", "plum", "grapce", "watermelon")
random_fruit = random.choice(fruits)
choice_a_char = input("Please guess a letter:  ").lower()
print()
for character in random_fruit:
    if character == choice_a_char:
        print("Right")
    else:
        print("Wrong")


# 2
# Needed Output

# We have 'apple' like a random fruit 
# ['_', '_', '_', '_', '_']
# Please guess a letter:  e
# ['_', '_', '_', '_', 'e']

import random

hight_fruit = []

fruits = ("apple", "banana", "pear", "tangerine", "plum", "grapce", "watermelon")
random_fruit = random.choice(fruits)
print()

for _ in random_fruit:
    hight_fruit.append("_")  #Or hight_fruit += "_"
print(hight_fruit)

choice_a_char = input("Please guess a letter:  ").lower()

if choice_a_char in random_fruit:
    for index in range(len(random_fruit)):
        if choice_a_char == random_fruit[index]:
            hight_fruit[index] = choice_a_char
    print(hight_fruit)
    
else:
    print("Try again ...")


# 3
# Needed Output

# We have "apple" like a random fruit
# ['_', '_', '_', '_', '_']     
# Please guess a letter:  a     
# ['a', '_', '_', '_', '_']
# Please guess a letter:  p
# ['a', 'p', 'p', '_', '_']
# Please guess a letter:  l
# ['a', 'p', 'p', 'l', '_']
# Please guess a letter:  z
# Try again ...
# ['a', 'p', 'p', 'l', '_']
# Please guess a letter:  e
# The random fruit is: apple
#   YOU WIN       


import random

hight_fruit = []

fruits = ("apple", "banana", "pear", "tangerine", "plum", "grapce", "watermelon")
random_fruit = random.choice(fruits)
print()

for _ in random_fruit:
    hight_fruit.append("_")  #Or hight_fruit += "_"

while random_fruit != "".join(hight_fruit):
    print("\n",hight_fruit)
    choice_a_char = input("Please guess a letter:  ").lower()

    if choice_a_char in random_fruit:
        for index in range(len(random_fruit)):
            if choice_a_char == random_fruit[index]:
                hight_fruit[index] = choice_a_char
    else:
        print("Try again ...")

print("\nThe random fruit is: ", "".join(hight_fruit))
print("""
**************
  YOU WIN
**************
""")