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

while True:
    try:
        age = int(input("Enter your age please: "))
    except ValueError:
        print("Sorry but your print is not an integer")
    except:
        print("Find an Error")
    else:
        print(f"You born in: {2025 - age}")
        break