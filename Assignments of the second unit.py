# 1
""" The function 'type()' specify the Data Type. """

# Needed Output:
# str
# int
# float
# bool
# complex

print(type("Hello, World!")) 
print(type(50)) 
print(type(3.14)) 
print(type(True))   #or print(type(False))
print(type(7 + 2j)) 
# Avec 7 est la partie réel et 2 est la partie imaginaire

# 2
""" To get the length of a string, use the 'len()' function. Remember an integer don't have the 'len()' function."""

word = "Hello, World!"

# Needed Output:
# 13
# e
# !

""" Get the character at position 1 (remember that the first character has the position 0)."""

print(len(word))
print(word[1])   #1 and -1 are indexes
print(word[-1])

# 3
"""
Python Casting: 

- int() → Converts to a whole number.
Example: int("4") → 4
         int(5.78) → 5

- float() → Converts to a decimal number.
Example: float("5") → 5.0
         float(12) → 12.0

- str() → Converts anything to text.
Example: str(5) → "5"
         str(8.12) → "8.12"
"""

# Needed Output:
# Enter a number: 356  
# -> 3

number = input("Enter a number: ")
number_len = len(number)
print(number_len)