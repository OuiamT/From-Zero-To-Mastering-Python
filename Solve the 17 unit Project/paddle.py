"""
Represents the player-controlled paddle in the Falling Shapes Game.

The paddle moves horizontally at the bottom of the screen and is used
to catch falling shapes. Movement is restricted to prevent the paddle
from leaving the visible game area.

Methods
-------
go_left()
    Moves the paddle to the left while staying within bounds.

go_right()
    Moves the paddle to the right while staying within bounds.
"""

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(1, 5)

    def go_left(self):
        new_x = self.xcor() - 30
        if new_x > -350:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 30
        if new_x < 350:
            self.goto(new_x, self.ycor())
