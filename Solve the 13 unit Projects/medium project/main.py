"""
User Management System
----------------------

This script implements a simple user management interface that allows
administrators to add and view users. It demonstrates basic object-oriented
programming concepts, user input validation, and console interface design.

Features:
    1. Add a new user by entering first name, last name, email, and password.
    2. Display all registered users with their details.
    3. Exit the application gracefully.

Classes:
    Management
        Handles user data including name, email, password, and account status.

Functions:
    clear_screen()
        Clears the console screen for better readability.

Workflow:
    1. The program displays a main menu with available actions.
    2. The user selects an option to either add a user, display users, or exit.
    3. Input is validated to prevent invalid or non-numeric entries.
    4. User data is stored in a list and displayed on request.
"""

from management import Management
import time
import os

users = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    clear_screen()
    print(
        """
Welcome to user managment
          
Choose an Action:
1. Add new user
2. Display all users
3. Exit
"""
    )
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
            