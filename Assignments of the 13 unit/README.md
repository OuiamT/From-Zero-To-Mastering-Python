# 🐍 Object-Oriented Programming (OOP):
## 📘 Definition:
**OOP (Object-Oriented Programming)** is a programming style that organizes code into **classes** and **objects**.
It helps make code more **reusable**, **organized**, and **easier to maintain**.
## 🧩 Class and Object:
### Class:
A blueprint or template that defines how objects are created.
```
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
```
### Object:
An instance of a class.
```
my_car = Car("Toyota", "Red")
```
## ⚙️ Methods vs Attributes:
- **Attributes** → Variables that store data inside an object.
- **Methods** → Functions defined inside a class that describe the object’s behavior.
## 🧮 Default Value:
You can assign **default values** to parameters in methods or constructors.
If no value is given, the default is used.
```
class Car:
    def __init__(self, brand="Unknown", color="Black"):
        self.brand = brand
        self.color = color
```
```
my_car1 = Car()               # brand = "Unknown", color = "Black"
my_car2 = Car("BMW", "Blue")  # brand = "BMW", color = "Blue"
```
