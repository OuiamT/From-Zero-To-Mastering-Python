from management import Management
import time
import os

users = []

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")


while True:
    clear_screen()
    print("""
Welcome to user managment
          
Choose an Action:
1. Add new user
2. Display all users
3. Exit
""")
    while True:
        try:
            choice = int(input("Enter your choice:  "))
            time.sleep(2)
            break
        except ValueError:
            print("Try again because your choice not a number between 1 and 9")
            continue
    
    clear_screen()
    match choice:
        case 1:
            f_name = input("Enter first name:  ").capitalize()
            l_name = input("Enter last name:  ").capitalize()
            email = input("Enter email:  ")
            password = input("Enter password:  ")
            users.append(Management(f_name, l_name, email, password))
            time.sleep(2)
            print("\nUser added successfully!\n")
            time.sleep(3)

        case 2:
            clear_screen()
            print("Displaying all users ....")
            time.sleep(3)
            for user in users:
                Management.display_inf(user)
            time.sleep(5)
        
        case 3:
            print("Exiting ....")
            time.sleep(3)
            break

        case _:
            print(f"The {choice} not valide ...")
            time.sleep(3)