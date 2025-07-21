# for loop

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
# if yes: ***** Done Tasks *****: <tasks>
# if no: ***** Ongoing Tasks *****: <tasks>

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
else :
    input("Enter Press to exist....")
