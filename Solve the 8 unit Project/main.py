import random


# todo --> رسومات الرجل المخنوق
HANGMANPICS = [ '''
  +---+ 
      |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''']


fruits = ["appel", "avocado", "banana", "orange", "tangerine", "plum", "pear", "watermelon", "pineappel", "strawberry"]

ComputerChoice = random.choice(fruits)
# todo --> تخمين فاكهة عشوائية
# todo --> عدد الخانات متطابق مع حروف الكلمة
# fruit = []
# for letter in ComputerChoice:
#     fruit += "_"    or fruit.append("_")
fruit = ["_"]*len(ComputerChoice) #todo اختصار ثلاثة اسطر fruit["_" for letter in computerchoice]

lives = 6
# todo الحروف سبق تخمينها
gussed_letters = []
print(HANGMANPICS[0])
while ComputerChoice != "".join(fruit) and lives > 0:    #or while "_" in fruit:
    print(" ".join(fruit))
    gussed = input("Please guess a letter:  ").lower().strip()
# todo هل الحرف تم تخمينه من قبل
    if gussed in gussed_letters:
        print(f"You already gussed that. Try agin  \nYou have {lives} more tries")
        continue

    else:
        gussed_letters.append(gussed)

# todo --> تبديل الخانة بالحرف الصحيح
    for position in range(len(ComputerChoice)):
        if gussed == ComputerChoice[position]:
            fruit[position] = gussed

    if gussed not in ComputerChoice :
        lives -= 1
        print(HANGMANPICS[6 - lives])
        print(f" you have {lives} more tries")

    else :
        print(f" you have {lives} more tries") 

if lives == 0:
    print("""\n********
YOU LOSE
********
=========
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""")
else :      
    print("""\n********
YOU WIN
********""")
