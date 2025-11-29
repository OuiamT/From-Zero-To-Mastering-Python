from turtle import Turtle, Screen
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
position = ((-40, 0), (-20, 0), (0, 0))
snake = []
window.tracer(0)
for x in range(3):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(position[x])
    snake.append(turtle)

while True:
    for x in snake:
        x.forward(0.1)
    window.update()


window.exitonclick()