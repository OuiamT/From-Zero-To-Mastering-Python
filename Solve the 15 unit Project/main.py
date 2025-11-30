from turtle import Turtle, Screen
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