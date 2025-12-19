from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

window = Screen()
window.setup(600, 600)
window.bgcolor("black")
window.title("Ping Pong")
window.tracer(0)
paddle1 = Paddle((250, 0))
paddle2 = Paddle((-250, 0)) 
ball = Ball()

window.listen()
window.onkey(paddle1.go_up, "Up")
window.onkey(paddle1.go_down, "Down")

window.onkey(paddle2.go_up, "A")
window.onkey(paddle2.go_down, "Q")

while True:
    window.update()
    time.sleep(0.1)
    ball.goto(ball.xcor()+ ball.x_move, ball.ycor() + ball.y_move)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1

    if (ball.xcor() >= 230 and ball.distance(paddle1) <= 50) or (ball.xcor() <= -230 and ball.distance(paddle2) <= 50):
        ball.x_move *= -1

window.exitonclick()