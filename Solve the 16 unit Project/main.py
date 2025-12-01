from turtle import Screen
from snakeeat import Snake
from food import Food
import time

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Project")
window.tracer(0)
snake1 = Snake()
food = Food()


while True:
    snake1.snake_move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake1.up, "Up")
    window.onkey(snake1.down, "Down")
    window.onkey(snake1.left, "Right")
    window.onkey(snake1.right, "Left")
    if snake1.head.distance(food) < 10:
        print("Good Job!!")
        food.where_food()
        snake1.tall_of_snake()


window.exitonclick()