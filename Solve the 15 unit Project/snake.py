from turtle import Turtle, Screen

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
        for i in range(len(self.snake)-1):
            self.snake[i].goto(self.snake[i+1].pos())
        self.snake[-1].forward(20)

    def up(self):
        self.snake[-1].setheading(90)

    def down(self):
        self.snake[-1].setheading(270)

    def left(self):
        self.snake[-1].setheading(0)

    def right(self):
        self.snake[-1].setheading(180)