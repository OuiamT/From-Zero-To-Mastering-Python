# 🧠 Learning 'Random' and Data Structure (List):
This folder contains notes and practice for understanding some fundamental Python.

## ✔ What i learned:
+ How to use two random methods: **random.randint()** and **random.random()**.
  - `random.randint(start, end)`: gives you a random whole number between the two numbers you choose, including both.
  - `random.random()`: gives you a random decimal number between 0.0 and 0.9999. If you want to give you a random decimal above this last one, just multiply it by the number you want.
  ```
  Example:
  random_decimal = random.random() * 5
  print(random_decimal)
  > Output: All number between 0.0 and 4.9999
  ```
+ **String Method: .capitalize()**: Made the first letter uppercase.
+ How to use **List**: It is a type of ***Data Structure***, and we learned how to use list methods: **append()**, **extend()** and **remove()**.
  ```
  💠 append() ---> Added a single item to the end of a list.
  💠 extend() --->  added all items from another list to the end of your list.
  💠 remove() ---> Deleted an item
  ```

## 📌 Bonus Knowledge:
### 🧩 Difference Between a Function and a Method:
+ A **function** is a block of code you can call by name, like **print()** or **len()**.
+ A **method** is like a function, but it's called on an object (like a **string** or **list**).
```
Example:
print("Hello")          -> is a function
my_name.capitalize()    -> is a method
```
### 💻 Helpful VSCode Extension:
+ 🎨 **Better Comments**:  helps you write more meaningful and colorful comments by using special symbols. 
