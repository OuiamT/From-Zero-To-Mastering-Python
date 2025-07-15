#  المكتبتان المتوفرتان
library = []
wishlist = []

# ? introduction :
print("----- Welcome to your library -----\n")

# ? the information about your books :
book_name = input("Enter the name of a book you own:  ").capitalize()
if book_name :
    library.append(book_name)
    book_name = input("Enter the name of another book you own (or press 'Enter' to skip):  ").capitalize()
    if book_name :
        library.append(book_name)
        print(f"\nYour library is : {library}\n")
    else :
        print(f"\nYour library is : {library}\n")

# ? the information about your wishlist books :
    book_name = input("Enter the name of a book you wish to have in the future:  ").capitalize()
    if book_name :
        wishlist.append(book_name)
        book_name = input("Enter the name of another book you wish to have in the future (or press 'Enter' to skip):  ").capitalize()
        if book_name :
            wishlist.append(book_name)
            print("\nYour wishlist is :", wishlist,"\n")
        else :
            print("\nYour wishlist is :", wishlist,"\n")

# ? About acqutred book :
        acqutred_book = input("Enter the name of a book from you wishlist that you've acqutred (or press 'Enter' to skip):  ").capitalize()
        if acqutred_book in wishlist :
            wishlist.remove(acqutred_book)
            library.append(acqutred_book)
            print(f"\nUpdated library : {library}         \nUpdated wishlist : {wishlist}\n")
        else :
            print(f"\nUpdated library : {library}         \nUpdated wishlist : {wishlist}\n")


# ? About donate book :
        donated_book = input("Enter the name of a book rom you library you wish to donate (or press 'Enter' to skip):  ").capitalize()
        if donated_book in library :
            library.remove(donated_book)
            print(f"Final library after donation : {library}")
        else :
            print(f"Final library after donation : {library}")
    else :
        print("Please!! Follow the directions")
else :
    print("Please!! Follow the directions")
