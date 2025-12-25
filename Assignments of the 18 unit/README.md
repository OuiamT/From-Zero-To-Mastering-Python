# 📂 File Handling in Python:
This document explains the basics of **handling files in Python**, including opening files, reading and writing modes, file pointers, and file paths.
## 📌 Opening Files:
To work with files in Python, we use the built-in open() function.
```
file = open("example.txt")
```
After opening a file, you can read or write data depending on the mode used.
## 📖 Reading Files:
```
file.read()
file.read(nbr)
file.readline()
file.readlines()
```
- **file.read()** → reads the entire file
- **file.read(nbr)** → reads a specific number of characters
