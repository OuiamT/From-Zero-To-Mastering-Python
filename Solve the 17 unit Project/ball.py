from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.y_move = -10
        self.shape_list = ["turtle", "square", "circle", "classic", "triangle"]
        self.color_list = ["red", "green", "blue", "yellow", "purple"]
        self.reset_position()

    def move(self):
        self.goto(self.xcor(), self.ycor()+ self.y_move)

    def reset_position(self):
        random_x = random.randint(-350, 350)
        self.goto(random_x, 250)

        random_shape = random.choice(self.shape_list)
        self.shape(random_shape)

        if random_shape == "turtle" and random.randint(1, 10) == 1:
            self.color("white")
        else:
            self.color(random.choice(self.color_list))

        random_size = random.uniform(0.5, 2)
        self.shapesize(random_size, random_size)

        