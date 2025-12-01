from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.position = [(-40, 0), (-20, 0), (0, 0)]
        self.snake_body()
        self.head = self.snake[-1]

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
        self.head.forward(20)

    def tall_of_snake(self):
        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(self.snake[0].pos())
        self.snake.insert(0, new_segment)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(0)

    def right(self):
        self.head.setheading(180)