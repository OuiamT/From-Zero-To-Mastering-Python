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

def the_rest(budget, item, price):
    return budget - (item * price)
    
while True:
    clear_scrin()
    budget = float(input("Enter your spending budget:  "))
    item = input("Enter the item you want to buy:  ").lower()
    many_items = int(input(f"How many {item}s do you want to buy?  "))
    price = float(input(f"Enter the price per {item}:  "))

    if the_rest(budget, many_items, price) < 0:
        print("Waring: Your purchase exceeds you daily dubget!")
    else:
        print("Purchase successful!! Enjoy your new item.")
    # print("Waring: Your purchase exceeds you daily dubget!") if result(budget, many_items, price) < 0 else print("Purchase successful!! Enjoy your new item.")

    if input("Do you want to continue? y-n:  ").lower() != "y":
        break
print("-" * 20)
print()


# 4
#! Shorten these codes
# def greet_person(name):
#     greeting_message = f"Hello, {name}! How are you?"
#     return greeting_message

# user_name = input("Enter your name:  ")
# result = greet_person(user_name)
# print(result)

def greet_person(name):
    return f"Hello, {name}! How are you?" 

print(greet_person(input("Enter your name:  ")))
print("-" * 20)
print()


# 5
# Needed Output:
# Welcome {name} to the restaurant!
# Order taken successfuuly.
# Thank you {name}, for choosing our restaurant!
    

def take_order(name):
    print(f"\nWelcome {name} to the restaurant!")
    print("Order taken successfuuly.")
    thank_customer(name)

def thank_customer(name):
    print(f"Thank you {name}, for choosing our restaurant!")

take_order(input("What is your name:\t").lower())
print("-" * 20)
print()

# 6
# Needed Output:
# Enter your base salary: example 3000
# How much bonus did you get?: example 250
# Final salary after 15% tax is: $4500.0

def calculate_tax(base_salary):
    return base_salary * 0.15

def final_salary(base_salary, bonus):
    total_salary = base_salary + bonus 
    return total_salary - calculate_tax(base_salary)

base_salary = float(input("Enter your base salary:  "))
bonus = float(input("How much bonus did you get?  "))
print(f"\nFinal salary after 15% tax is:\n${final_salary(base_salary, bonus)}")
print("-" * 20)
print()


# 7
# Needed Output:
# Enter a user name
# Enter your email
# Checking email name ....
# Check if email is valid or not


def check_result(name, email):
    if "@" in email and "." in email:
        print(f"User '{name}' with email '{email}' successfully added.")
    else:
        print("Invalid email format. Registration failed.")

import time

user_name = input("Enter a user name:  ")
email = input("Enter your email:  ")
time.sleep(2)
print("Checking email name ....")
time.sleep(2)
print("Validation email adress ....")
time.sleep(3)
check_result(user_name, email)
print("-" * 20)
print()