# 📂 File Handling in Python:
This document explains the basics of **handling files in Python**, including opening files, reading and writing modes, file pointers, and file paths.
## 📌 Opening Files:
To work with files in Python, we use the built-in open() function.
```
file = open("example.txt")
file.close()
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
- **file.readline()** → reads the first line
- **file.readlines()** → convert str to list 
## 🧭 File Modes:
| Mode | Meaning                          |
| ---- | -------------------------------- |
| `r`  | Read (default)                   |
| `w`  | Write (overwrites file)          |
| `a`  | Append (adds content at the end) |
| `x`  | Create a new file                |
| `w+` | Write and read                   |
| `r+` | Read then write                  |
| `a+` | Append and read                  |
