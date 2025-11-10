"""
Gym Membership Management System
=================================

This script provides a simple command-line interface (CLI) for managing gym memberships.
Users can create new members, display all existing members, and search for specific
members by first name, membership ID, or membership status.

Modules Used:
-------------
- os : For clearing the console screen across operating systems.
- time : For adding small delays to improve the user experience.
- membership : Custom module that defines the *Member* class.

Functionalities:
---------------------
1. **Search Members**:
   Allows searching for members by:
     - First name
     - Membership ID
     - Membership status

2. **Clear Screen**:
   Clears the console window depending on the operating system.

3. **Input Validation**:
   - is_digit: Ensures the membership ID contains only digits.
   - is_alpha: Ensures name fields contain only alphabetic characters.

4. **Create Member**:
   Prompts the user for first name, last name, membership ID, and membership status.
   Validates inputs (alphabetic for names, digits for IDs) before creating a *Member* instance.

Program:
-------------
- Displays a main menu with four options:
  1. Add new member
  2. Display all members
  3. Search for a member
  4. Exit
- Loops until the user chooses to exit.

Error Handling:
---------------
- Input validation ensures correct data types for each field.
- Handles unexpected user inputs gracefully with retry prompts.

Notes:
------
- The script depends on the *Member* class from *membership.py*, which must define:
    - Member.display_members()
    - Member.status_etap()
- This script is intended for small-scale, console-based management and does not
  persist data to disk (data is lost when the program exits).
"""

from membership import Member
import os
import time


all_members = []


# ! The biginnir of search function
def search_by(all_members):
    """
    Search for gym members by first name, membership ID, or status.

    This function provides an interactive console menu that lets users
    filter and view members stored in the *all_members* list. After selecting
    a search criterion, it prompts the user for the corresponding input,
    validates it, finds all matching members, and displays them using
    *Member.display_members()*.

    Parameters
    ----------
    all_members : list
        A list containing `Member` objects to be searched through.

    Behavior
    --------
    - Displays a menu with the following options:
        1. Search by first name
        2. Search by membership ID
        3. Search by membership status
        4. Exit the search menu
    - Collects user input for the chosen search field.
    - Validates inputs:
        - Ensures names contain only alphabetic characters.
        - Ensures IDs contain only numeric digits.
    - Displays all matching members using the *Member.display_members()* method.
    - Returns control to the main menu after displaying results.

    Exceptions
    ----------
    - Handles invalid numeric inputs (e.g., non-integer menu choices).
    - Handles invalid text or ID inputs gracefully with re-prompts.

    Notes
    -----
    - The search is case-insensitive due to *.capitalize().strip()* normalization.
    - Temporary search results are cleared after each search iteration.
    - The function runs in a loop until the user chooses to exit.
    """
    found_members = []
    while True:
        clear_scrine()
        print(
            """
    Search by:
            
    1. First Name
    2. ID membership
    3. Status
    4. Exit
            
    """
        )
        try:
            choice = int(input("Enter your choice:  "))
            time.sleep(3)
            match choice:
                case 1:
                    f_name = input("Enter the first name:  ").capitalize().strip()
                    if not f_name.isalpha():
                        f_name = is_alpha(f_name)
                    for member in all_members:
                        if f_name == member.f_name:
                            found_members.append(member)

                case 2:
                    member_id = input("Enter the ID membership:  ").capitalize().strip()
                    if not member_id.isdigit():
                        member_id = is_digit(member_id)
                    for member in all_members:
                        if member_id == member.member_id:
                            found_members.append(member)

                case 3:
                    member_status = (
                        input("Enter the status of the person:  ").capitalize().strip()
                    )
                    for member in all_members:
                        if member_status == member.member_status:
                            found_members.append(member)

                case 4:
                    print("You will come back to principal page ...")
                    time.sleep(3)
                    break

                case _:
                    print("\nInput a number between 1 and 4!!")
                    time.sleep(3)

            clear_scrine()
            for x in found_members:
                Member.display_members(x)
            found_members.clear()
            input("Enter any key to return ...")

        except:
            print("Ivalid choice... Choice 1 or 2 or 3")
            time.sleep(5)


# ! The end of search function


def clear_scrine():
    os.system("cls" if os.name == "nt" else "clear")


def is_digit(member_id):
    while not member_id.isdigit():
        member_id = input("Enter the ID membership from digits (0 to 9):  ").strip()
        return member_id


def is_alpha(name):
    while not name.isalpha():
        name = input("Enter the name only from alphabitic:\t").capitalize().strip()
        return name


def creat_member():
    f_name = input("Enter first name:\t").capitalize().strip()
    if not f_name.isalpha():
        f_name = is_alpha(f_name)

    l_name = input("Enter last name:\t").capitalize().strip()
    if not l_name.isalpha():
        l_name = is_alpha(l_name)

    member_id = input("Enter membership ID:\t").strip()
    if not member_id.isdigit():
        member_id = is_digit(member_id)

    member_status = (
        input("Enter membership status, Or click enter:\t").capitalize().strip()
    )
    return Member(f_name, l_name, member_id, member_status)


while True:
    clear_scrine()
    print(
        """
Welcome to Gym Membership Managment
          

Choose an Action:
          
1. Add new member
2. Display all members
3. Search for a member
4. Exit
"""
    )
    try:
        choice = int(input("\nEnter your choice:\t"))
        time.sleep(3)
        clear_scrine()
        match choice:
            case 1:
                all_members.append(creat_member())
                time.sleep(3)
                print("\nMember added successfully!")
                time.sleep(3)

            case 2:
                if all_members:
                    print("Displaying all members ....")
                    for member in all_members:
                        Member.status_etap(member)
                        Member.display_members(member)
                        input("Enter any key to return a principal page ...")
                else:
                    print("Sorry this file is Empty...")
                    time.sleep(3)

            case 3:
                if all_members:
                    search_by(all_members)
                else:
                    print("Sorry the file is Empty... So you desn't can search")
                    time.sleep(3)
            case 4:
                print("The Programme Exit ....")
                time.sleep(3)
                print("Good Bye !!!")
                break
            case _:
                print("Invalid choice... Choice a number between 1 and 4")
                time.sleep(5)
    except:
        time.sleep(3)
        print("Please Input a number between 1 and 4")
        time.sleep(3)
        print("Try again ....")
        time.sleep(3)
