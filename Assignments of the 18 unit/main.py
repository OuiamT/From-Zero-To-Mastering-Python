# Open a file for reading and close it after finishing.
my_file = open(r"C:\Users\Python\Project Python\From-Zero-To-Mastering-Python\Assignments of the 18 unit\data.txt")
print(my_file.read())
my_file.close()
print("-" * 30)

# Open a file for reading and close it automatically after finishing
with open(r"C:\Users\Python\Project Python\From-Zero-To-Mastering-Python\Assignments of the 18 unit\data.txt") as my_file:
    print(my_file.read(5))
print("-" * 30)

# Open a file to write a sentence of your choice without reading.
with open(r"C:\Users\Python\Project Python\From-Zero-To-Mastering-Python\Assignments of the 18 unit\data.txt", "w") as my_file:
    my_file.write("Hi there, How is going?")
print("-" * 30)

# Creat a file to write a sentance in your choice with reading.
with open("data.txt", "w+") as file:
    file.write("Hi there, How is going?") 
    file.seek(0)
    print(file.readline())
print("-" * 30)

# Open the data.txt file and append a new sentance.
with open("data.txt", "a") as file:
    file.write("\nI'm very well")
with open("data.txt", "r") as file:
    print(file.read())
print("-" * 30)
