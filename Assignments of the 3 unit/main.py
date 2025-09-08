# 1
# Exemple:
age = 23 
print(f"My name is Ouiam, I am {age} years old.")
print("------------------------------------------------\n")


# 2
# Needed Output:
# Welcome to my Application:
# How old are you? 
# 'Your answer'
# if your age bigger than 12, So you can to use it, but if not you can't use the Application

print("Welcome to my Application:" )
age = int(input("How old are you?  \n"))
if age < 12 :
    print("Sorry, you can't use the Application...")
else:
    print("Good, you can to use the app")
print("------------------------------------------------\n")


# 3
# White a simple project, that take a number, and print if this number is positive or negative or zero.

number = float(input("Enter a number:  "))
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"0 is null")
else:
    print(f"{number} is negative")
print("------------------------------------------------\n")


# 4
# Write a simple project, to check if a PassWord is correct or not.

PassWord = "abc123"
your_PassWord = input("Enter your PassWord:  ")
if your_PassWord == PassWord:
    print("Hello")
else:
    print("Sorry")
print("------------------------------------------------\n")
    

# 5
""" 
Write a block code to ask about age and driver's license, if over than 18 years old or 
equal and have a driving license, he can to drive
"""

age = int(input("How old are you:  \n"))
license = input("Do you have a driver's lisence: (yes or no):  ").lower()

if license == "yes" or license == "no":
    if age >= 18 and license == "yes":
        print("You can to drive")
    # elif age < 18 or license == "no":
    else:
        print("Sorry, you can't to drive")
else :
    print(f"Sorry, you entery of '{license}' is not understood")  

print("------------------------------------------------\n")


# 6
# A project about Nested if statements:

is_morocco = input("Are you Moroccan? (yes or no): \n").upper()
if is_morocco == "YES":
    print("Good, that is the first step...")
    age = int(input("Please enter your age:  \n"))
    if age >= 18:
        print("You can have an ID")
    else:
        print("Sorry, you have to be 18 or older    \nPlease try again when you are 18")
else:
    print("Sorry, an Morocco ID is give only to Moroccans")

print("------------------------------------------------\n")
