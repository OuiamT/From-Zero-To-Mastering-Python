print("""▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀▒
▒▒█▒▒███████▄██████▒▒▒
▒▒▒▒▒██████████████▒▒▒
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒
""")

print("\n\nWelcome to my island!")

door = input("There are two doors in front of you. 🚪 a Red door and 🚪 a Blue door   \nWhich door do you want to open?\n").lower()
if door == "blue" :
    print("Oopss! you chose the crocodiel door🐊🐊🐊.    \nGame over!!!")
elif door == "red" :
    print("Great!! now you entered a room.     \nYou found three boxes: 🎁 White, 🎁Black, 🎁Green.")
    box = input("Which box do you want to open?\n").lower()
    if box == "white" :
        print("Oopss! you opened a box filled with snakes🐍🐍🐍")
    elif box == "black" :
        print("Oopss! you opened a box filled with spider 🕷 🕸 🕷 🕸")
    elif box == "green" :
        print("Congratulation!! You found the treasure 💰💲💰💲")
    else :
        print("Ivalide choice 😕😓😕😓")
else :
    print("Ivalide choice 😕😓😕😓")