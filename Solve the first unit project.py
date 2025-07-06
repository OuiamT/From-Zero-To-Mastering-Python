

# Needed Output:
"""
Welcome to the YouTube channel Name Generator:
What is your name?
-> answer1
What is your channel about?
-> answer2
You could name your channel: (answer2 with answer1)
"""

print("Welcome to the YouTube channel Name Generator:")
name = input("What is your name?\n")
channel_about = input("What is your channel about?\n")
print("You could name your channel: ("+channel_about+ " with "+ name+")")