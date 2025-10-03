# 1
# Needed Output:
# Enter your name Please:  
# Hi {name}, How are you? 
#! With use function.

def greet(name):
    return f"Hi {name}, How are you? "

message = input("Enter your name Please:  ").lower()
print(greet(message))
print("-" * 20)
print()

# 2
# Needed Output:
# ! With use Function choose 2 number and return their reproduction.
# "Too high" if result >= 20, if is not print "Good".

def multiplication(num1, num2):
    return num1 * num2

reproduction = multiplication(5, 9)
if reproduction >= 20:
    print("Too high")
else:
    print("Good")
print("-" * 20)
print()

# 3
# Needed Output:
# Enter your spending budget
# Enter the item you want to buy
# How many {item}s do you want to buy?
# Enter the price per {item}
# Waring: Your purchase exceeds you daily dubget! if rest < 0 if is not Purchase successful!! Enjoy your new item.

import os

def clear_scrin():
    os.system( "cls" if os.name == "nt" else "clear")

def result(budget, item, price):
    return budget - (item * price)
    
while True:
    clear_scrin()
    budget = int(input("Enter your spending budget:  "))
    item = input("Enter the item you want to buy:  ").lower()
    many_items = int(input(f"How many {item}s do you want to buy?  "))
    price = int(input(f"Enter the price per {item}:  "))

    sum = result(budget, many_items, price)
    if sum < 0:
        print("Waring: Your purchase exceeds you daily dubget!")
    else:
        print("Purchase successful!! Enjoy your new item.")

    if input("Do you want to continue? y-n:  ").lower() != "y":
        break
print("-" * 20)
print()