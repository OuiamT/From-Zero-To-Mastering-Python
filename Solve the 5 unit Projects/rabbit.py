field = [["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"]]

print("Welcome to place the rabbit...\n")
print(f"{field[0]}   \n{field[1]}   \n{field[2]}")
print("\nWhere should the 🐇 to go?")

choice = input("Please choose a row and a colum:  ")
row = int (choice[0]) 
colum = int (choice[1]) 
field[row - 1][colum - 1] = "🐇"

print("\nSuccess ....    \n")
print(f"{field[0]}   \n{field[1]}   \n{field[2]}")
