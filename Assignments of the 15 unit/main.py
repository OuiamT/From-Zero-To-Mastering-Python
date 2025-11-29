from turtle import Turtle, Screen
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")

position = [(-40, 0), (-20, 0), (0, 0)]
snake = []
# window.tracer(0)
for x in range(len(position)):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(position[x])
    snake.append(turtle)

#* The snake move:
# while True:
#     for turtle in snake:
#         turtle.forward(0.1)
#         window.update()

#* The snake move without tracer:
while True:
    for i in range(len(snake)-1):
        snake[i].goto(snake[i+1].pos())
    snake[-1].forward(20)

window.exitonclick()