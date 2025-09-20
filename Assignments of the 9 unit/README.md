# More about Functions in Python:

## What i learned:

### 🔹 Function with Parameters and Arguments:
A **function** is a block of code that runs only when called, you can pass information to a function using **parameters** and **arguments**.

```
# Function definition with a parameter
def greet(name):
    print("Hello,", name)

# Function call with an argument
greet("Mohamed")   # Output: Hello, Mohamed
```
- **Parameter** → A variable inside the function definition.
- **Argument** → The actual value you pass when calling the function.

### 🔹 Positional Arguments:
**Arguments** are **matched** with **parameters** based on their **position** in the 
function call, but we can change the order of the parameters.
```
def introduce(first_name, last_name, age):
    print("My name is", first_name, last_name)
    print("My age is", age, "years old")

# Positional arguments: not matched in order
introduce(last_name="Adil", age= "30", first_name= "Mahmoud")     # Output: My name is Mahmoud Adil
                                                                  #         My age is 30 years old
```

