# 🐍 Snake Game:
A simple **Snake game** built using Python’s built-in turtle graphics module. The project consists of two files:
- **main file** → sets up the game window and controls the gameplay loop
- **snake.py** → contains the Snake class that builds and moves the snake

## 🎮 How the Game Works:
1. The program creates a 600×600 window with a black background.
2. The snake is built from four red square segments.
3. The game runs in a continuous loop where:
  - The snake moves forward each frame.
  - The screen updates smoothly (**window.update()**).
  - A short delay controls the snake's speed (**time.sleep(0.1)**).
4. The player uses the keyboard to change the direction of the snake.
5. The window stays open until the user clicks to close it.

## 🎯 Controls:
| Key   | Action     |
| ----- | ---------- |
| **e** | Move Up    |
| **d** | Move Down  |
| **f** | Move Left  |
| **s** | Move Right |
