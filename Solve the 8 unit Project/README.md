# 🎮 Hangman Game:
This is a **Hangman game**. The computer randomly selects a fruit name,and the player must guess
the word letter by letter before running out of lives. Wrong guesses are shown using ASCII 
art of a hangman.

## 🚀 How to Use:
- The computer randomly picks a fruit name.
- You will see underscores **(_)** representing the letters in the word.
- type your guessed letter.
- If the letter is in the word, it will be revealed in the correct position.
- If not, you lose one life and part of the hangman is drawn.
- If you repeat a letter, the game will remind you: "You already guessed that. Try again"
- If you guess all letters before lives run out, **you WIN**.
- If you run out of lives, you see the full hangman drawing and, **you LOSE**.

## 📌 Bonus Knowledge:
### Python Enhancement Proposal:

**PEP (Python Enhancement Proposal)** is a design document that provides information to the Python community. 
It describes new features, improvements, or guidelines for the Python language.
In this project uses three tools to keep the code clean and readable:
- **Black** → Automatically formats your code to follow **PEP 8** conventions.
- **pydocstyle** → Ensures your documentation follows **PEP 257** conventions.
- **pylint** → Analyzes your code for errors, coding standards, and potential bugs.
- And we have **pycodestyle** → Ensures your code follows **PEP 8** conventions.
