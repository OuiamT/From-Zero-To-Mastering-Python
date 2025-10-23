# 1
# Needed Output:
# user name is : [used local variable]
# user name is : [used global variable]

name = "Ibrahim"
def info():
    name = "Adel"
    print(f"User name inside info is: {name}")

info()
print(f"User name is: {name}")
print("-" * 20)
print()

# 2
# Needed Output:
# [name: local variable] [contry: global variable]

user_contry = "Morocco"
def information():
    user_name = "Mohamed"
    print(user_name,  user_contry)

information()
print("-" * 20)
print()


# 3
# Needed Output:
# Enter your number
# All of messages are Errors or Exceptions (number egal 0, number not a one character or not a number).

num = input("Enter your number:  ")
if num == '0':
    raise ValueError("Number Must Be Larger Than 0")

elif len(num) != 1:
    raise IndexError( "Only One Character Allowed")

elif not num.isdigit():
    raise Exception("Only Numbers Allowed")

print(f"The number is: {num}")
print("-" * 20)
print()

# 4


while True:
    try:
        char = input("Add Letter From A to Z:  ")
        if not char.isalpha():
            print("The Letter Not In A - Z")
        elif len(char) != 1:
            print("You Must Write One Character Only")
        else:
            print(f"You typed {char}")
            break
    except:
        print("Exist an Ettor")
