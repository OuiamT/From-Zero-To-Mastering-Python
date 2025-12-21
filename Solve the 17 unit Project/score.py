from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self, point):
        self.score += point
        self.update_score_board()

    def reset_score(self):
        self.score = 0
        self.update_score_board

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))