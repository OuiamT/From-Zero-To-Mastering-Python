from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard
import time

window = Screen()
window.setup(800, 600)
window.bgcolor("black")
window.title("Falling Shapes Game")
window.tracer(0)

player = Paddle((0, -250))
shapes = Ball()
score = ScoreBoard()

window.listen()
window.onkey(player.go_left, "Left")
window.onkey(player.go_right, "Right")

shape_speed = 0.1

while True:
    window.update()
    time.sleep(shape_speed)
    shapes.move()

    if shapes.distance(player) < 50 and shapes.ycor() < -230:
        shape_type = shapes.shape()
        shape_color = shapes.color()[0]

        if shape_type == "turtle" :
            if shape_color == "white":
                score.game_over()
                break
            else:
                point = 5
                score.increase_score(point)
        elif shape_type == "square":
            point = 2
            score.increase_score(point)
        elif shape_type == "circle":
            point = 1
            score.increase_score(point)
        elif shape_type == "triangle":
            score.reset_score()

        shapes.reset_position()
        shape_speed *= 0.9

    if shapes.ycor() < -300:
        shapes.reset_position()

window.exitonclick()
