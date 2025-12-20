from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

window = Screen()
window.setup(600, 600)
window.bgcolor("black")
window.title("Ping Pong")
window.tracer(0)
paddle1 = Paddle((250, 0))
paddle2 = Paddle((-250, 0)) 
ball = Ball()
score_board = Score()

window.listen()
window.onkey(paddle1.go_up, "Up")
window.onkey(paddle1.go_down, "Down")

window.onkey(paddle2.go_up, "A")
window.onkey(paddle2.go_down, "Q")

default_sleep = 0.1
while True:
    window.update()
    time.sleep(0.05)
    ball.goto(ball.xcor()+ ball.x_move, ball.ycor() + ball.y_move)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1

    if (ball.xcor() >= 230 and ball.distance(paddle1) <= 50) or (ball.xcor() <= -230 and ball.distance(paddle2) <= 50):
        ball.x_move *= -1
        default_sleep *= 0.9

    if ball.xcor() > 300:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1
        score_board.l_point()

    if ball.xcor() < -300:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1
        score_board.r_point()



window.exitonclick()