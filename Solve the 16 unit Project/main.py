from turtle import Screen
from snakeeat import Snake
from food import Food
from scoreboard import ScoreBoard
import time

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Project")
window.tracer(0)
snake1 = Snake()
food = Food()
score = ScoreBoard()


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
        food.where_food()
        snake1.tall_of_snake()
        score.increase_score()
    if snake1.head.xcor() > 270 or snake1.head.xcor() < -270 or snake1.head.ycor() > 270 or snake1.head.ycor() < -270:
        score.lose()
        break

    for segmant in snake1.snake[: -1]:
        if snake1.head.distance(segmant) < 10:
            score.lose()
            break


window.exitonclick()