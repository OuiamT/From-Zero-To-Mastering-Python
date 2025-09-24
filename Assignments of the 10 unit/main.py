book = {
    "title": "Red Queen",
    "author": "Victoria Aveyard",
    "year": 2015,
    "pages": 383,
    "is many": True,
    "rating": 4.1,
}

# 1
# Needed Output:
# {'title': 'Red Queen', 'author': 'Victoria Aveyard', 'year': 2015,
# 'pages': 383, 'is many': True, 'rating': 4.1}
# Victoria Aveyard

print(book)
print(book["author"])
print("-" * 20)
print()


teacher = {}

# 2
# Needed Output
# {'name': 'Mohamed', 'age': 57, 'ID': 2094, 'country': 'Morocco'}
# {}

teacher["name"] = "Mohamed"
teacher["age"] = 57
teacher["ID"] = 2094
teacher["country"] = "Morocco"
print(teacher)
teacher = {}
print(teacher)
print("-" * 20)
print()


students = {
    1: "Ouiam", 
    2: "Mohamed",
    3: "Meryam"
}

# 3
# Needed Output:
# Ouiam
# the new Dict is: {1: 'Ouiam', 2: 'Ayoub', 3: 'Meryam', 4: 'Ali'}

print(students[1])
students[4] = "Ali"
students[2] = "Ayoub"
print("The new Dict is: ", students)
print("-" * 20)
print()


# 4
# Needed Output
# Student ID:
# 1
# Student Name:
# Ouiam
# ----------
# Student ID:
# 2
# Student Name:
# Ayoub
# ----------
# Student ID:
# 3
# Student Name:
# Meryam
# ----------
# Student ID:
# 4
# Student Name:
# Ali
# ----------

for key in students:
    print("Student ID:")
    print(key)
    print("Student Name:")
    print(students[key])
    print("-" * 10)
print("-" * 20)
print()