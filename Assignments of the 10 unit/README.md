# 📘 Dictionaries & OS Module:
This document contains simple explanations and examples about **Python dictionaries** and the **OS module**.

## 🗂️ Dictionary in Python:
A **dictionary** is a built-in Python data type uses curly braces **{}**, stores data as **key: value**, requires **unique keys**, and is accessed by keys instead of indexes.

### ✍️ How to Write a Dictionary:
```
student = {
    "name": "Mohamed",   # Key → A unique identifier (like "name").
    "age": 20,         # Value → The data stored for that key (like "20").
    "grade": "A"
}
```

## 🗂️ Nested Dictionary:
A dictionary can contain another dictionary inside it.
### ✍️ How to Write a Nested Dictionary:
```
library = {
    "001": {"title": "Python Basics", "author": "Ali"},
    "002": {"title": "Data Analysis", "author": "Sara"}
}
print(library["001"]["title"])  # Output: Python Basics
```

## 💻 OS Module – “Operating System”
The **OS module** in Python lets you interact with the operating system.

```
import os

# Clear screen (works for Windows and Linux/Mac)
os.system("cls" if os.name == "nt" else "clear")
```
