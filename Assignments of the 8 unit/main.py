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