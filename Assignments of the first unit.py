# This is a comment
""" Multiple Line Comment """ 

# 1: 
# Python use 'Interpreter': Each line of code is read, then interpreted and executed by the computer.

#  2
print("Hello") 
print('Hello')
#  It's same result
print("---------------------")


# 3
# Needed Output:
"""
I love python

print(I love python)
"""
print("I love Python")
print()
print("print(I love Python)")
print("----------------------")


# 4
# "\n" --> means a new line
# Needed Output:
"""
I love python
Python is very easy
"""
print("I love python   \nPython is very easy")
print("-------------------------")


# 5
# Debugging <=> Bug:
# print("Hello" + " "Python")
#  print("Hello " + "Python")
# print(Hello" + " Python")
# print("Hello" + " " "Python"
# prin("Hello" + " "Python")

# The solution is:
print("Hello" +  " Python")
print("Hello " + "Python")
print("Hello" + " Python")
print("Hello" + " " +"Python")
print("Hello " + "Python")
print("-------------------------")


# 6
# input <=> يدخل البيانات
# variable <=> مكان في ذاكرة الكمبيوتر يتم فيها تخزين قيمة
# Needed Output:
# Enter your name:
# -> Ouiam
# Hello, Ouiam
name = input("Enter your name:\n")
print("Hello, "+name)
