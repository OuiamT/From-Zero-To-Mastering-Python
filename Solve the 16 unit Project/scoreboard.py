"""
Manages the score display for the Snake game.

This class is responsible for showing the current score at the top
of the screen, updating it when the snake eats food, and displaying
a game-over message when the player loses.

Inheritance
-----------
Inherits from the Turtle class to use turtle graphics for text display.

Methods
-------
*update_scoreboard()*
    Displays the current score on the screen.

*increase_score()*
    Increases the score by one and refreshes the display.

*lose()*
    Ends the game visually by changing the background color and
    showing the final score message.
"""

from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def lose(self):
        self.screen.bgcolor("darkred")
        self.goto(0, 0)
        self.write(
            f"Game Over\nFinal Score is: {self.score}",
            align="center",
            font=("Arial", 24, "normal"),
        )
