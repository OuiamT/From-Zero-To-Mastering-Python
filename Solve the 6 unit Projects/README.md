# iShop Calculator & Password Generator:
A collection of two beginner Python projects.

## 🛒 Project 1: iShop Calculator:
### ▶️ How to Use:
- Input the number of items in your basket.
- Enter names and prices for each item.
- View the full list of basket items.
- See the total cost of your shopping.

## 🔐 Project 2: Password Generator:
### ▶️ How to Use:
The script asks you:
- Total number of characters in the password.
    + Number of letters
    + Number of digits
    + Number of symbols
- It checks that the sum of letters, digits, and symbols matches the total number or not.
- If valid, it creates a password using `import string`:
    + **string.ascii_letters** (A-Z, a-z)
    + **string.digits** (0-9)
    + **string.punctuation** (!@#$%^&*...)
- The password is shuffled to improve randomness and printed to the screen using `random.shuffle()`.
