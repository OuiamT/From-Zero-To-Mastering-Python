import random

# ? Save Ascii in Variables 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("Welcome to the Rock, Paper, Scissors game :")
plan = input("Press 'Enter' to continue or type 'Help' for the rules :\t").lower()

if plan == "help" :
    print("""\n        ***********RULES**********
    1)You choose and the computer choose
    2)Rock smashes Scissors --> Rock win
    3)Scissors cut Paper --> Scissors win
    4)Paper covers Rock --> Paper win""")

# ? Display user choice in Ascii

    my_choice = input("\nEnter you choice 'Rock, Paper, Scissors' :\n").lower()
    if my_choice == "rock":
        print("\nYou chose \n",rock)
    elif my_choice == "paper" :
        print("\nYou chose \n",paper)
    elif my_choice == "scissors" :
        print("\nYou chose \n",scissors)
    else :
    # todo: anathor methode
    # todo: if my choice 'not in' ["rock"...]--> ivalide choice : لن احتاج الى استعمال متغير
        print("Ivalide choice!! Please run the program again and choose Rock, Paper or Scissors.")  

# ? Computer choice   
    computer_choice = random.choice(["rock", "paper", "scissors"]) 
    if computer_choice == "rock":
        print("\ncomputer chose \n",rock)
    elif computer_choice == "paper" :
        print("\ncomputer chose \n",paper)
    else : 
        print("\ncompter chose \n",scissors)

    # ? المقارنة
    if my_choice == computer_choice :
        print("It is a tie")
    elif (my_choice == "paper" and computer_choice == "rock" ) or\
         (my_choice == "rock" and computer_choice == "scissors") or \
         (my_choice == "scissors" and computer_choice == "paper") :
        print("Congratulation!! You win! ")
    else:
        print("Sorry!! You lose! ")

    

elif plan  == "":
    my_choice = input("\nEnter you choice 'Rock, Paper, Scissors' :\n").lower()

# ? Display user choice in Ascii
    if my_choice == "rock":
        print("\nYou chose \n",rock)
    elif my_choice == "paper" :
        print("\nYou chose \n",paper)
    elif my_choice == "scissors" :
        print("\nYou chose \n",scissors)
    else :
        print("Ivalide choice!! Please run the proraù again and choose Rock, Paper or Scissors.")    

#  ? Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if computer_choice == "rock":
        print("\ncomputer chose \n",rock)
    elif computer_choice == "paper" :
        print("\ncomputer chose \n",paper)
    else : 
        print("\ncompter chose \n",scissors)


    # ?  المقارنة
    if my_choice == computer_choice :
        print("It is a tie")
    elif (my_choice == "paper" and computer_choice == "rock" ) or\
         (my_choice == "rock" and computer_choice == "scissors") or \
         (my_choice == "scissors" and computer_choice == "paper") :
        print("Congratulation!! You win!")
    else:
        print("Sorry!! You lose!")
else :
    print("Ivalide choice!! Please run the program again and choose 'Help' or press 'Enter' to continue..")