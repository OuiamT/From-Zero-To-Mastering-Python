"""
Manages the score display for the Falling Shapes Game.

This class is responsible for showing the current score at the top
of the screen, updating the score when the player catches shapes,
resetting the score for special cases, and displaying a game-over
message when the game ends.

Responsibilities
----------------
- Display the current score.
- Update the score based on shape type.
- Reset the score when required.
- Show a game-over message.

Methods
-------
update_score_board()
    Refreshes the score display on the screen.

increase_score(point)
    Adds the given number of points to the current score.

reset_score()
    Resets the score back to zero.

game_over()
    Displays the game-over message.
"""

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
