from turtle import Turtle, Screen
import random

# 1 
# Needed Output:
# Square drawn with a red turtle, a triangle with a blue turtle and a circle with green turtle.

window = Screen()
turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("red")
# turtle1.forward(100)
# turtle1.left(90)
# turtle1.forward(100)
# turtle1.left(90)
# turtle1.forward(100)
# turtle1.left(90)
# turtle1.forward(100)
# turtle1.left(90)
for _ in range(4):
    turtle1.forward(100)
    turtle1.left(90)

turtle1.color("blue")
for _ in range(3):
    turtle1.forward(150)
    turtle1.right(120)

#! We will deaw a circle without a loop.
turtle1.color("green")
turtle1.circle(100)


# 2
# Square drawn in random color, size of color and shape.
window.reset()
colors = ["red", "blue", "green", "black", "cyan", "DeepPink", "DeepPink4", "coral"]
shapes = ["turtle", "classic", "square", "triangle", "circle"]
size = [1, 4, 8, 10, 7, 5]
def draw_a_square(colors, shapes, size):
    for _ in range(4):
        turtle1.speed("slow")
        turtle1.shape(random.choice(shapes))
        turtle1.color(random.choice(colors))
        turtle1.pensize(random.choice(size))
        turtle1.forward(100)
        turtle1.left(90)

draw_a_square(colors, shapes, size)

window.exitonclick()