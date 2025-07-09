"""
F-Strings:
'F-strings' are a new and easy way to put variables inside a string. 
To use them, just write the letter f before your string, 
and put the variable inside curly brackets {}.
"""

# Exemple:
age = 23
print(f"My name is Ouiam, I am {age} years old.")
print("------------------------------------------------\n")


"""
If Condition:
**************
We use this code block:

if condition:
    If the condition is true, the code will run.
elif condition:
    It check another condition if the first is not true.
else:
    It runs when none of the above conditions are true.
"""

"""
Indentation:
************
Python uses indentation to define blocks of code (it is best to leave 4 spaces). If you don't indent
correctly, Python will give you an error.
"""

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



# Needed Output:
# if this number is positive or negative or zero

number = float(input("Enter a number:  "))
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"0 is null")
else:
    print(f"{number} is negative")
print("------------------------------------------------\n")
