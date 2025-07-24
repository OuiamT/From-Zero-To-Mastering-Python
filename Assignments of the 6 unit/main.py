# 1
# Needed Output:
# Red
# Black
# Pink
# ! Without Loop:
colors = ["Red", "Black", "Pink"]
print(colors[0])
print(colors[1])
print(colors[2])
print("-" * 20)

# ! With Loop:
colors = ["Red", "Black", "Pink"]
for color in colors:
    print(color)
print("-" * 20)

# 2
# Needed Output:
# O
# U
# I
# A
# M
name = "ouiam"
for char in name:
    print(char.upper())
print("-" * 20)

# 3
# Needed Output
# Bananas
# Grapes
# Apples is my favorite fruit.
# Watermelon
fruits = ["Bananas", "Grapes", "Apples", "Watermelon"]
for fruit in fruits:
    if fruit.lower() == "apples":
        print(f"{fruit} is my favorite fruit.") 
    else:
        print(fruit)
print("-" * 20)

# 4
# Needed Output
# 2
# 4
# 6
# 8
# 10
# Finished the loop successfully.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)
        print()
print("Finished the loop successfully.")
print("-" * 20)


# 5
# Needed Output
# Enter the name of attendees separated by comma and espace:
# name
# Is this person attending? (yes or no)
# if yes: Attendance confirmed! 
# if no: Attendance not confirmed!

attendees = input("Enter the name of attendees separated by comma and espace:  ").split(", ")
for person in attendees:
    print(person)
    print()
    confirme = input("Is this person attending? (yes or no):  ").lower()
    if confirme == "yes" :
        print("Attendance confirmed!")
    else:
        print("Attendance not confirmed!")
    print("---------")
print("-" * 20)


# 6
# Needed Output
# Enter your taskes for today separated by comma and espace:
# A task
# Did you finish <task> alredy? (Yes/No):
# if yes: Nice job
# if no: Try not to put it off!
# After finish all tasks
# Do you want to see your today's progress? (Yes/No):
# if yes: ***** Done Tasks *****: <tasks>     ***** Ongoing Tasks *****: <tasks>
# if no: Enter Press to exist....

done_tasks = []
ongoing_tasks = []


tasks = input("Enter your taskes for today separated by comma and espace:  ").split(", ")
for task in tasks:
    print(f"\n{task}\n")
    respons = input(f"Did you finish {task} alredy? (Yes/No):  ").upper()
    if respons == "YES":
        print("Nice job")
        done_tasks.append(task)
    else:
        print("Try not to put it off!")
        ongoing_tasks.append(task)
    print("------")
response = input("Do you want to see your today's progress? (Yes/No):  ").upper()
if respons == "YES":
    print(f"""
          
    ***** Done Tasks *****
{done_tasks}

    ***** Ongoing Tasks *****
{ongoing_tasks}
""")
else:
    input("Enter Press to exist....")
print("-" * 20)


# 7
# Needed Output
# 0
# 1
# 2
# 3
# 4
for x in range(5):
    print(x)
print("-" * 20)


# 8
# Needed Output
# 5
# 7
# 9
for x in range(5, 10, 2):
    print(x)
print("-" * 20)

# 9
print("*** Welcome to the Multipliation table ***")
number = int(input("Enter a number: "))
for X in range(1, 11):
    result = X * number
    print(f"{number} x {X} = {result}")
print("-" * 20)


# 10
"""Shorthand Operations"""
# Example:
x = 5
x = x + 2
print(x)
# Is same
x = 5
x += 2
print(x)

# Example for the String
message = "Hello"
message += " ,World!"
print(message)

# 11
# Needed Output
# Let's add each number to the next
# --> <total>
# The total number is: <total>

total = 0
print("Let's add each number to the next:")
for number in range(1, 5):
    total += number
    print(f"--> {total}")
    print(f"The total number is: {total}\n")
print("-" * 20)

# 12
# Input:
# meryam sabah, ali farah, salma salah 
# Needed Output
# Enter the first and the last name of your friends separated by a comma and espace:
# ["meryam", "sabah"]
# ["ali", "farah"]
# ["salma", "salah"]
# Abbreviated names:
# M. S.
# A. F.
# S. S.

names = input(
        "Enter the first and the last name of your friends separated by a comma and espace:  "
        ).title().split(", ")
for f_l_name in names:
    separator = f_l_name.split()
    print(separator)
    
print("Abbreviated names:")
for abbrv in names:
    separator = abbrv.split()
    f_name = separator[0][0]
    l_name = separator[1][0]
    print(f"{f_name}. {l_name}.")


# 13
# Input: Python is easy
# Needed Output
# Enter a sentance:
# Reversed sentance: easy is Python

reversed_sentance = []
sentance = input("Enter a sentance:  ").split()
lenght = len(sentance)

for word in range(1, lenght + 1):
    l_word = sentance[-word]
    reversed_sentance.append(l_word)

# ! Or can you writ it with use slicing:
# for word in sentance[::-1]:
#     reversed_sentance.append(word)    

right_sentance = " ".join(reversed_sentance)
print(f"Reversed sentance: {right_sentance}")


# 14
# Input: "Wait up!" Shouted> the main in= (green) clothes!
# Needed Output
# Please type a sentance:
# 
# ----- Here is the same sentance without punctuation -----
# Wait up Shouted the main in green clothes

import string

same_sentance = []
sentance = input("Please type a sentance: \n")
punctuations = string.punctuation

for world in sentance:
    if world not in punctuations:
        same_sentance.append(world)

print("\n----- Here is the same sentance without punctuation -----\n")
right_sentance = "".join(same_sentance)
print(right_sentance)