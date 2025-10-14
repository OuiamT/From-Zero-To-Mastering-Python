from twenty_one_art import logo
import os
import time

def clear_scrine():
    os.system ("cls" if os.name == "nt" else "clear")

while True:
    my_choice = input("Choose 'Twenty one' game to start....\t").lower()
    clear_scrine()
    time.sleep(4)
    if my_choice == "21" or my_choice == "twenty one":
        print("Starting game ....")
        time.sleep(4)
        print(logo)

    else:
        print("Try againe ....")
        time.sleep(4)
    