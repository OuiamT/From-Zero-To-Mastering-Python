# 📘 Python Notes: Scope & Exception Handling:
## 🔹 Scope: Global and Local Variables:
### Global Variables
- Defined outside of all functions.
- Accessible anywhere in the file.
### Local Variables:
- Defined inside a function.
- Only accessible within that function.
```
x = 2  # global variable
def my_function():
    x = 10  # local variable
    print(x)

my_function()  # 10
print(x)       # 2
```
- You can use the `global` keyword inside a function to modify a global variable.
```
x = 5  # global variable
def change_x():
    global x
    x = 10

change_x()
print(x)  # 10
```

## 🔹 Exception Handling: try, except, else, finally:
### Structure:
```
try:
    # Code that might raise an error
except SomeError:
    # Code that runs if an error occurs
else:
    # Code that runs if no error occurs
finally:
    # Code that always runs
```
