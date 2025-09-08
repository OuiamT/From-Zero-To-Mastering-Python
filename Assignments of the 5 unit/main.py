# 1
# Needed Output:
# Welcome to 'whose wallet'?
# You will give me a list of names, and I will pick a person to pay.
# If you are ready, enter the names separated by comma and espace:
# Please ask <'name'>, to take his wallet out. Dinner is on him


import random

print("Welcome to 'whose wallet'? \n" 
"You will give me a list of names, and I will pick a person to pay.")
names = input("If you are ready, enter the names separated by comma and espace: \n")
split_names = names.split(", ")
length = len(split_names) - 1
computer_choice = random.randint(0, length)
print(f"Please ask '{split_names[computer_choice]}', to take his wallet out. Dinner is on him")

print("-" * 40, "\n")

# Onather solution 

import random
print("Welcome to 'whose wallet'? \n" 
"You will give me a list of names, and I will pick a person to pay.")
names = input("If you are ready, enter the names separated by comma and espace: \n").split(", ")
print(f"Please ask '{random.choice(names)}', to take his wallet out. Dinner is on him")

print("-" * 40, "\n")


# 2
# Input: [["Apples", "Bananas"], ["Milk", "Water", "Coffe"]]
# Needed Output:
# ["Apples", "Bananas"]
# Apples
# Bananas Milk
# [["Apples", "Bananas"], ["Milk", "Water", "Coffe"], ["Cake", "Candy"]]

basket = [["Apples", "Bananas"], ["Milk", "Water", "Coffee"]]
print(basket[0])
print(basket[0][0])
print(basket[0][1], basket[1][0])
basket.append(["Cake", "Candy"])
print(basket)

print("-" * 40, "\n")


# 3
# Input: [["Watermelons", "Grapes"], ["Tea", "Coffee"]]
# Needed Output:
# Press 'Enter' to change the content....
# Here is the updated basket....
# [['Oranges', 'Watermelons', 'Grapes', 'Kiwi'], ['Water', 'Tea', 'Milk'], [1, 6.21, True]]


basket = [["Watermelons", "Grapes"], ["Tea", "Coffee"]]
print(basket)
input("Press 'Enter' to change the content....")
basket[0].insert(0, "Oranges")
basket[0].append("Kiwi")
basket[1].insert(0, "Water")
basket[1].remove("Coffee")
basket[1].insert(2, "Milk")
basket.append([1, 6.21, True])
print("Here is the updated basket....\n")
print(basket)

print("-" * 40, "\n")