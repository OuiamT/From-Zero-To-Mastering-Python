# function with parameters and arguments
# def fct(parameter):
#   print(parameter)

# fct(argument)

# 1

# Input:
# multiply(7)

# Needed output:
# 7 x 1 = 7
# 7 x 2 = 14 
# 7 x 3 = 21 
# 7 x 4 = 28 
# 7 x 5 = 35 
# 7 x 6 = 42 
# 7 x 7 = 49 
# 7 x 8 = 56 
# 7 x 9 = 63 
# 7 x 10 = 70

def multiplay(number):
    for x in range(1, 11):
        result = number * x
        print(f"{number} x {x} = {result}")

multiplay(7)