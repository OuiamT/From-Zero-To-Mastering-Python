from turtle import Turtle, Screen
import random
import time

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
time.sleep(2)


# 2
# Needed Output:
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
time.sleep(2)
window.reset()

# 3
# Needed Output:
# Lines drawn with random angles.

window.setup(600, 600)
window.bgcolor("black")
turtle1 = Turtle("turtle")
turtle1.color("blue")
turtle2 = Turtle("square")
turtle2.color("red")

angles = [0, 90, 180, 270]
distances = [20,30,40,50,60,70,90,100]

def walking(turtle):
    for _ in range(random.choice([10, 20, 5, 15])):
        turtle.forward(random.choice(distances))
        turtle.right(random.choice(angles))

walking(turtle1)
walking(turtle2)

time.sleep(2)
window.reset()

# 4
# Needed Output:
# Homework:

window.bgcolor("black")
window.setup(width=800, height=600)

turtle1 = Turtle("turtle")
turtle1.color("white")
turtle1.speed("fastest")

places = [(-250, -150), (0,0), (250, 150)]

def place(places):
        turtle1.penup()
        turtle1.goto(places)
        turtle1.pendown()

def draw_a_circle():
    place(places[0])
    for _ in range(20):
            turtle1.circle(50)
            turtle1.left(360 / 20)

def draw_a_square():
    place(places[1])
    for _ in range(15):
            for _ in range(4):
                  turtle1.forward(50)
                  turtle1.left(90)
            turtle1.left(360 / 15)

def draw_a_triangle():
    place(places[2])
    for _ in range(10):
            for _ in range(3):
                  turtle1.forward(50)
                  turtle1.left(120)
            turtle1.left(360 / 10)

draw_a_circle()
draw_a_square()
draw_a_triangle()


window.exitonclick()