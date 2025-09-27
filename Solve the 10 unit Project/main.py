import os

catalog = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_books(catalog):
    while True:
        ISBN_book = input("Enter ISBN:  ")
        title_book = input("Enter title:  ").capitalize()
        author_of_book = input("Enter author:  ").title()
        catalog[ISBN_book] = {"title": title_book, "author": author_of_book, "Available": True}
        print(f"Book '{title_book}' by {author_of_book} added to the catalog with ISBN {ISBN_book}")

        if input("Do you want to add another book? (y-n):  ").lower() != "y":
            break

        else:
            clear_screen()
            continue

def check_out_book(catalog):
    while True:
        ISBN_ckeck_out = input("Enter ISBN to check out:  ")
        if ISBN_ckeck_out in catalog:
            if catalog[ISBN_ckeck_out]["Available"] == True:
                print(f"Book '{catalog[ISBN_ckeck_out]["title"]}' chacked out successfully.")
                catalog[ISBN_ckeck_out]["Available"] = False
            else:
                print("Sorry, The book is currently checked out ...")

        else:
            print(f"Sorry this {ISBN_ckeck_out} ISBN not found ...")

        if input("Do you want to check out another book? (y-n):  ").lower() != "y":
            break

        else:
            clear_screen()
            continue
    
def check_in_book(catalog):
    while True:
        ISBN_ckeck_in = input("Enter ISBN to check in:  ")
        if ISBN_ckeck_in in catalog:
            if catalog[ISBN_ckeck_in]["Available"] == False:
                print(f"Book '{catalog[ISBN_ckeck_in]["title"]}' chacked in successfully.")
                catalog[ISBN_ckeck_in]["Available"] = True
            else:
                print("Sorry, The book is currently checked in. It's not ours...")

        else:
            print(f"Sorry this {ISBN_ckeck_in} ISBN not found in the catalog ...")

        if input("Do you want to check out another book? (y-n):  ").lower() != "y":
            break

        else:
            clear_screen()
            continue


def list_of_books(catalog):
    print("Library Catalog:\n")
    for key in catalog:
        print(f"""
ISBN: {key}
Title: {catalog[key]["title"]}
Author: {catalog[key]["author"]}
Available: {catalog[key]["Available"]}
-----------
""")

while True:
    print("""
Menu:
------
1. Add Book
2. Check Out Book
3. Check In Book
4. List Books
5. Exit
""")
    
    choice = int(input("Enter your choice (1 - 5): "))
    clear_screen()
    if choice == 1:
        add_books(catalog)

    elif choice == 2:
        check_out_book(catalog)

    elif choice == 3:
        check_in_book(catalog)

    elif choice == 4:
        list_of_books(catalog)
        input("Press any key to go back to the menu ...")

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print(f"This {choice} number choice not found in the menu ... Try again")
