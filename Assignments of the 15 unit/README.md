# 🐍 Snake Project:
This document explains the key concepts used in your Snake Game built with **Python’s turtle module**.
It covers how the snake moves, how event listeners work, and what functions like `tracer()` or `setheading()` do.

## 📏 Turtle Square Size:
In the **turtle** module, the default shape **"square"** has a size of **20×20 pixels**.
What is a pixel?
**A pixel** is the smallest dot your screen can display. Every shape on the turtle screen is made of pixels.
- **One square = 20 pixels wide × 20 pixels tall**

## Attributes:
### 1. window.tracer(0):
This turns off automatic drawing.
- The screen stops updating after every turtle movement.
- The game becomes smoother because you control the exact moment when the frame updates.
### 2. window.update().
### 3. window.listen():
Activates the window so it can **listen for keyboard input**. Without calling **.listen()**, key presses won’t be detected.
### 4. window.onkey(function, key):
Binds a keyboard key to a function.
```
Example:
window.onkey(snake.up, "w")
```
Means -> When the player presses w, call snake.up()
### 5. snake.setheading(angle):
Changes the turtle’s **direction instantly**.
Directions:
- 0 → right
- 90 → up
- 180 → left
- 270 → down
