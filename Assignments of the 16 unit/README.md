# 📘 Simple Guide in OOP:
This document completes what we started with concepts in **object-oriented programming (OOP)** in Python using simple language and small examples.
## 🧬 Inheritance:
**Inheritance** allows a class to inherit attributes and methods from another class, creating a parent-child relationship.
```
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass
```
- **Dog** inherits from **Animal** and can use **speak()**.
## 🚀 Super():
**super()** is used inside a child class to call methods from the parent class.
```
class Animal:
    def __init__(self):
        print("Animal created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
# Output: Animal created
          Dog created
```
## 🔁 Overriding:
**Overriding** allows a child class to provide its own implementation of a methode that already exists in the parent class.
```
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
```
- When calling **Dog().speak()**, Python uses the child’s method, not the parent’s.
## 🧭 MRO (Method Resolution Order):
**MRO** defines the order in which Python looks for a method when multiple classes are involved.
# 💻 Basics Command Line Interface (CLI) :
| Purpose              | Windows Command    | macOS / Linux Command | 
| -------------------- | ------------------ | --------------------- |
| Show files & folders | `dir`              | `ls`                  | 
| Change directory     | `cd folder_name`   | `cd folder_name`      | 
| Go back one level    | `cd ..`            | `cd ..`               | 
| Clear screen         | `cls`              | `clear`               | 
| Check Python version | `python --version` | `python3 --version`   | 
| Run project | `python main.py` | `python3 main.py`|
