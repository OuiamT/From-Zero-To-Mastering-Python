"""
Library Management System
-------------------------

This is a friendly Python program that simulates a simple library system.
It allows users to:

1. Add books to the catalog with ISBN, title, and author.
2. Check out a book if available.
3. Check in a previously borrowed book.
4. View the list of all books in the catalog.
5. Exit the program.

The catalog is stored in a dictionary where:
- The key is the ISBN (string of digits).
- The value is another dictionary containing:
    - "title": Title of the book
    - "author": Author of the book
    - "Available": Boolean (True if available, False if checked out)
"""

import os

catalog = {}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def add_books(catalog):
    """
    Add new books to the catalog.

    Prompts the user to enter an ISBN (numbers only), title, and author.
    Each book is stored in the catalog dictionary with its availability set to True.
    The user can continue adding multiple books until they choose to stop.

    Args:
        catalog (dict): The library catalog where books are stored.
    """
    while True:
        ISBN_book = input("Enter ISBN:  ")
        if not ISBN_book.isdigit():
            continue

        title_book = input("Enter title:  ").capitalize()
        author_of_book = input("Enter author:  ").title()
        catalog[ISBN_book] = {
            "title": title_book,
            "author": author_of_book,
            "Available": True,
        }
        print(
            f"\nBook '{title_book}' by {author_of_book} added to the catalog with ISBN {ISBN_book}\n"
        )

        if input("Do you want to add another book? (y-n):  ").lower() != "y":
            break

        else:
            clear_screen()
            continue


def check_out_book(catalog):
    """
    Check out a book from the catalog.

    Prompts the user to enter an ISBN. If the ISBN exists and the book is available,
    it marks the book as checked out (Available = False).
    If the book is already checked out or the ISBN is not found,
    it displays an appropriate message.

    Args:
        catalog (dict): The library catalog where books are stored.
    """
    while True:
        ISBN_ckeck_out = input("Enter ISBN to check out:  ")
        if not ISBN_ckeck_out.isdigit():
            continue

        if ISBN_ckeck_out in catalog:
            if catalog[ISBN_ckeck_out]["Available"] == True:
                print(
                    f"\nBook '{catalog[ISBN_ckeck_out]["title"]}' chacked out successfully.\n"
                )
                catalog[ISBN_ckeck_out]["Available"] = False
            else:
                print("\nSorry, The book is currently checked out ...\n")

        else:
            print(f"\nSorry this {ISBN_ckeck_out} ISBN not found ...\n")

        if input("Do you want to check out another book? (y-n):  ").lower() != "y":
            break

        else:
            clear_screen()
            continue


def check_in_book(catalog):
    """
    Check in a book to the catalog.

    Prompts the user to enter an ISBN. If the ISBN exists and the book is
    currently checked out, it marks the book as available again (Available = True).
    If the book is already checked in or the ISBN is not found,
    it shows an appropriate message.

    Args:
        catalog (dict): The library catalog where books are stored.
    """
    while True:
        ISBN_ckeck_in = input("Enter ISBN to check in:  ")
        if not ISBN_ckeck_in.isdigit():
            continue

        if ISBN_ckeck_in in catalog:
            if catalog[ISBN_ckeck_in]["Available"] == False:
                print(
                    f"\nBook '{catalog[ISBN_ckeck_in]["title"]}' chacked in successfully.\n"
                )
                catalog[ISBN_ckeck_in]["Available"] = True
            else:
                print("\nSorry, The book is currently checked in. It's not ours...\n")

        else:
            print(f"\nSorry this {ISBN_ckeck_in} ISBN not found in the catalog ...\n")

        if input("Do you want to check out another book? (y-n):  ").lower() != "y":
            break

        else:
            clear_screen()
            continue


def list_of_books(catalog):
    print("Library Catalog:\n   -------  ")
    for key in catalog:
        print(
            f"""
ISBN: {key}
Title: {catalog[key]["title"]}
Author: {catalog[key]["author"]}
Available: {catalog[key]["Available"]}
-----------
"""
        )


while True:
    print(
        """
Menu:
------
1. Add Book
2. Check Out Book
3. Check In Book
4. List Books
5. Exit
"""
    )

    choice = int(input("Enter your choice (1 - 5): "))
    clear_screen()
    if choice == 1:
        add_books(catalog)

    elif choice == 2:
        if not catalog:
            print("Sory this catalog is empty ...")
        else:
            check_out_book(catalog)

    elif choice == 3:
        if not catalog:
            print("Sory this catalog is empty ...")
        else:
            check_in_book(catalog)

    elif choice == 4:
        if not catalog:
            print("Sory this catalog is empty ...")
        else:
            list_of_books(catalog)
            input("Press any key to go back to the menu ...")

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print(f"This {choice} number choice not found in the menu ... Try again")
