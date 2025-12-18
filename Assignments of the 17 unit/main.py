from turtle import Screen
from paddle import Paddle
from ball import Ball

window = Screen()
window.setup(600, 600)
window.bgcolor("black")
window.title("Ping Pong")
paddle1 = Paddle((250, 0))
paddle2 = Paddle((-250, 0)) 
ball = Ball()

window.listen()
window.onkey(paddle1.go_up, "Up")
window.onkey(paddle1.go_down, "Down")

window.onkey(paddle2.go_up, "A")
window.onkey(paddle2.go_down, "Q")

while True:
    ball.goto(ball.xcor()+1, ball.ycor()+1)

window.exitonclick()