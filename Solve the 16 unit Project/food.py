"""
Represents the food object in the Snake game.

The food is a small circular turtle that appears at a random position
on the screen. When the snake eats the food, it is moved to a new
random location.

Inheritance
-----------
This class inherits from the Turtle class and uses turtle methods
for shape, color, and movement.

Methods
-------
*where_food()*
    Moves the food to a random position within the game boundaries.
"""

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
