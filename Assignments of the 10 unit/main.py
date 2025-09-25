# book = {
#     "title": "Red Queen",
#     "author": "Victoria Aveyard",
#     "year": 2015,
#     "pages": 383,
#     "is many": True,
#     "rating": 4.1,
# }

# # 1
# # Needed Output:
# # {'title': 'Red Queen', 'author': 'Victoria Aveyard', 'year': 2015,
# # 'pages': 383, 'is many': True, 'rating': 4.1}
# # Victoria Aveyard

# print(book)
# print(book["author"])
# print("-" * 20)
# print()


# teacher = {}

# # 2
# # Needed Output
# # {'name': 'Mohamed', 'age': 57, 'ID': 2094, 'country': 'Morocco'}
# # {}

# teacher["name"] = "Mohamed"
# teacher["age"] = 57
# teacher["ID"] = 2094
# teacher["country"] = "Morocco"
# print(teacher)
# teacher = {}
# print(teacher)
# print("-" * 20)
# print()


# students = {
#     1: "Ouiam", 
#     2: "Mohamed",
#     3: "Meryam"
# }

# # 3
# # Needed Output:
# # Ouiam
# # the new Dict is: {1: 'Ouiam', 2: 'Ayoub', 3: 'Meryam', 4: 'Ali'}

# print(students[1])
# students[4] = "Ali"
# students[2] = "Ayoub"
# print("The new Dict is: ", students)
# print("-" * 20)
# print()


# # 4
# # Needed Output
# # Student ID:
# # 1
# # Student Name:
# # Ouiam
# # ----------
# # Student ID:
# # 2
# # Student Name:
# # Ayoub
# # ----------
# # Student ID:
# # 3
# # Student Name:
# # Meryam
# # ----------
# # Student ID:
# # 4
# # Student Name:
# # Ali
# # ----------

# for key in students:
#     print("Student ID:")
#     print(key)
#     print("Student Name:")
#     print(students[key])
#     print("-" * 10)
# print("-" * 20)
# print()


# # 5
# # Needed Output:
# # {'name': 'Jack', 'country': 'USA', 'age': 30}

# information = {}
# name = input("What is your name?  ").capitalize()
# information["name"] = name
# country = input("Where are you from?  ")
# information["country"] = country
# age = int(input("How old are you?  "))
# information["age"] = age

# print(information)
# print("-" * 20)
# print()


# 6
# Needed Output


def add_a_contact(contacts):
    ID_contact = input("Enter the contact ID:  ")
    user_name = input("Please type a name:  ").capitalize()
    user_phone = input("Please type a phone number:  ")
    contacts["ID"] = ID_contact
    contacts["name"] = user_name
    contacts["phone number"] = user_phone
    print(f"\n{user_name} was added successfuly ....\n")

def recherche_a_contact(contacts):
    ID_contact = input("Please enter an ID edit:  ")

    if ID_contact == contacts["ID"]:
        new_name = input("Enter a new name:  ").capitalize()
        new_phone = input("Enter a new number:  ")
        contacts["name"] = new_name
        contacts["phone number"] = new_phone
        print("\n Success ...")

    else:
        print(f"This {ID_contact} ID not exist.!!")
    

contacts = {}

while True:
    print("""
    Contact Managment
        
    1- Add a contact
    2- View contact
    3- Edit a contact
    4- Exit
    """)
    choice = int(input("Please choose a number from 1-4:  "))
    if choice == 1:
        add_a_contact(contacts)

    elif choice == 2:
        print(f"\n{contacts}\n")

    elif choice == 3:
        recherche_a_contact(contacts)

    elif choice == 4:
        print("Exiting the program ....")
        break
    
    else:
        print(f"This {choice} number not exist in the contact managment menu ...")