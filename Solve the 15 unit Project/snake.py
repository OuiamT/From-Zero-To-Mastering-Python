"""
A class representing the snake used in the Snake game.

The snake is composed of multiple square turtle segments stored in a list.
The last segment in the list represents the snake's head. The snake starts 
with four segments positioned horizontally.

Attributes
----------
snake : list[Turtle]
    A list containing the turtle segments that make up the snake's body.
position : list[tuple[int, int]]
    Initial (x, y) coordinates for each starting segment of the snake.

Methods
-------
snake_body()
    Creates the initial snake body using the predefined starting positions.

snake_move()
    Moves the snake forward by shifting each segment to the position of the 
    segment in front of it. The head moves forward by 20 units.

up()
    Changes the snake head's direction to upward (90 degrees).

down()
    Changes the snake head's direction to downward (270 degrees).

left()
    Changes the snake head's direction to left (0 degrees).

right()
    Changes the snake head's direction to right (180 degrees).
"""

from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.position = [(-40, 0), (-20, 0), (0, 0), (20, 0)]
        self.snake_body()

    def snake_body(self):
        for x in range(len(self.position)):
            turtle = Turtle("square")
            turtle.color("red")
            turtle.penup()
            turtle.goto(self.position[x])
            self.snake.append(turtle)

    def snake_move(self):
        for i in range(len(self.snake) - 1):
            self.snake[i].goto(self.snake[i + 1].pos())
        self.snake[-1].forward(20)

    def up(self):
        self.snake[-1].setheading(90)

    def down(self):
        self.snake[-1].setheading(270)

    def left(self):
        self.snake[-1].setheading(0)

    def right(self):
        self.snake[-1].setheading(180)
