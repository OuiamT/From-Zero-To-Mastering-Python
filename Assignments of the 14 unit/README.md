# 🐢 Python Turtle Module:
**The Turtle** module in Python is a beginner-friendly graphics library in **OOP** that allows you to create drawings, animations, and interactive programs using simple commands.
## 🔹 Main Classes:
It works with two main classes:
1. `Turtle` Class:
Used to create and control a “turtle” — the pen that moves and draws on the screen.
2. `Screen` Class:
Represents the drawing window.
You use it to control window settings such as size, background color, input dialogs, etc.
## 🖥️ Screen Class:
- `Screen().exitonclick()`:
Closes the window when you click on it. Useful for ending programs.
- `screen.setup(width, height)`:
Sets the window size.
- `screen.bgcolor(color_name)`:
Changes the background color.
- `screen.reset()` vs `screen.clear()`:
  - **reset()** → Clears the screen and resets the turtle (position, color, speed, etc).
  - **clear()** → Clears the drawings only but keeps settings the same.
- `window.textinput(title, prompt)`:
Opens a dialog box to take text input from the user.

## 🐢 Turtle Class:
- `turtle.shape()`:
Changes the appearance of the turtle.
Common shapes:
**"turtle", "classic", "square", "triangle", "circle", "arrow"**
- `turtle.color(name)`:
Sets the turtle’s color.
You can find a large list of colors online: search “Python turtle colors list”.
### Movement:
- `turtle.forward(steps` → Move forward (in pixels).
- `turtle.right(angle)` → Turn right.
- `turtle.left(angle)` → Turn left.
- `turtle.goto(x, y)` → Move to a specific coordinate.
### Drawing Tools:
- `turtle.circle(radius)` → Draw a circle.
- `turtle.penup()` → Lift pen (no drawing).
- `turtle.pendown()` → Lower pen (draw).
- `turtle.pensize(n) ` → Set the pen thickness.
### Speed Control:
- `turtle.speed(value)`
Possible values: **"fastest", "fast", "normal", "slow", "slowest"**
### Writing Text on Screen
- `turtle.write(text, font=("Arial", size, "normal"), align=("center", "left" or "right")`
Draw text at the turtle’s current position.
