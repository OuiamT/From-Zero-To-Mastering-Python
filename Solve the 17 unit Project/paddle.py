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