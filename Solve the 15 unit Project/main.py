"""
Snake Game
----------

This script initializes and runs a simple Snake game using Python's turtle module.
The snake itself is implemented in a separate class (`Snake`) imported from the
`snake` module. The game window is set up with a black background, fixed size, and
manual screen updates to create smooth animation.

Controls
--------
The user controls the snake's direction using the following keyboard keys `miniscule`:
- **e** → Move Up
- **d** → Move Down
- **f** → Move Left
- **s** → Move Right

These controls are bound inside the loop using `window.onkey()` and `window.listen()`.
"""

from turtle import Screen
from snake import Snake
import time

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Project")
window.tracer(0)
snake1 = Snake()

while True:
    snake1.snake_move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake1.up, "e")
    window.onkey(snake1.down, "d")
    window.onkey(snake1.left, "f")
    window.onkey(snake1.right, "s")


window.exitonclick()
