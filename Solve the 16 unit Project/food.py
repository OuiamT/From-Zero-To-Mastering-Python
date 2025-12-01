from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.where_food()

    def where_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.penup()
        self.goto(random_x, random_y)