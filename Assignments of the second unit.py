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
print("-----------------------------------------\n")
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
print("-----------------------------------------\n")


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
# Enter a number: 35609
# -> 5

number = input("Enter a number: ")
number_len = len(number)
print(number_len)
print("-----------------------------------------\n")



# 4
"""
Python Arithmetic Operators:
+	Addition	
-	Subtraction		
*	Multiplication	
/	Division		
%	Modulus	
**	Exponentiation		
'//' Floor division

- Remember the arithmetic operators have an order of priority that you can remember with this sentence:
-> Please Excuse My Dear Aunt Sally
P = Parentheses 
E = Exponent
M = Multiplication
D = Division
A = Addition
S = Subtraction
"""

# Needed Output:
# Please enter two digits: Exemple: 65
# -> 11

number = input("Please Enter two digits:  ")
number_1 = int(number[0])
number_2 = int(number[1])
print(number_1 + number_2)
print("-----------------------------------------\n")



# Needed Output:
# Please type Length:
# answer 1
# Please type width:
# answer 2
# Enter how much for 1 meter?
# answer 3
# The total area is: "Is a multiplication of answer1 and answer2"
# Give the person DH: "Is a multiplication of total area and answer3"

length = float(input("Please type Length:\n"))
width =  float(input("Please type Length:\n"))
pay = float(input("Enter how much for 1 meter?\n"))
result = length * width
result_of_pay = result * pay
# print("The total area is: "+result)  -> Type Error: can only concatenate str to str (not float)
str_area = str(result)
print("The total area is: " + str_area)
print("Give the person: " + str(result_of_pay) + "DH")
print("-----------------------------------------\n")

# Needed Output:
# How old are you: -> Your answer
# You were born in the year: ...

age = int(input("How old are you:  "))
born_in = 2025 - age
print("You were born in the year: " + str(born_in))

