"""
Turtle Game
----------------

This program creates a simple turtle racing game using the Python turtle module.
Three turtles (red, blue, and green) start on the left side of the screen and move
forward by a random amount until one of them crosses the finish line.

The user is prompted to bet on which turtle color will win the race. After the race
ends, the program displays a message indicating whether the user guessed correctly.
The screen background turns green when the user wins and red when the user loses.

Main Components
---------------
- User Input:
    The player enters a color: "red", "blue", or "green" to guess which turtle will win.

- Turtle Setup:
    Three turtles are created, positioned vertically, and assigned the colors red,
    blue, and green.

- Race Logic:
    The turtles move forward by small random steps until one crosses the finish line.
    The winner is determined based on its x-coordinate.

- Result Display:
    The function `who_is_winner()` displays either "You win!" or "You lose!" at the
    center of the screen and changes the background color accordingly.

Functions
---------
- who_is_winner(winner):
    Displays the race result message and sets the background color depending on
    whether the player's chosen turtle won.

- race_turtle():
    Runs the turtle race by moving each turtle randomly until a winner is detected.
    Calls `who_is_winner()` with the outcome.

This program runs in a loop, allowing the user to play multiple times until they
close the window.
"""
from turtle import Turtle, Screen
import random

window = Screen()

START_AXE_X = -250
start_axe_y = (0, 100, -100)
colors = ("red", "blue", "green")
turtles = []


def who_is_winner(winner):
    """
    Display the result of the turtle race and change the screen background
    depending on whether the player guessed correctly.

    Parameters
    ----------
    winner : bool
        A boolean value indicating whether the player's chosen turtle won.
        - True : The player guessed correctly.
        - False: The player guessed wrong.
    """
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 0)
    result_turtle.pendown()
    if winner == my_choice:
        window.bgcolor("dark green")
        result_turtle.color("black")
        result_turtle.write("You win!", align="center", font=("Arial", 30, "normal"))
    else:
        window.bgcolor("red")
        result_turtle.color("black")
        result_turtle.write("You lose!", align="center", font=("Arial", 30, "normal"))


def race_turtle():
    """
    tart the turtle race and determine the winning turtle.

    This function moves each turtle forward by a random small amount on each
    iteration until one turtle crosses the finish line (x > 275). When a turtle 
    wins, the function calls `who_is_winner()` to display the result.
    """
    move_turtle = True
    while move_turtle:
        for turtle in turtles:
            if turtle.xcor() > 275:
                move_turtle = False
                winner_turtle = turtle.pencolor()
                who_is_winner(winner_turtle == my_choice)

            else:
                turtle.forward(random.randint(1, 4))


while True:
    window.setup(600, 500)
    window.bgcolor("AliceBlue")
    window.title("OctuCode Turtle Race")
    my_choice = (
        window.textinput(
            "Make your bet", "Guess the winner:\nType a color:Red, Blue or Green"
        )
        .lower()
        .strip()
    )
    match my_choice:
        case "red" | "blue" | "green":
            for x in range(3):
                new_turtle = Turtle("turtle")
                new_turtle.color(colors[x])
                new_turtle.penup()
                new_turtle.goto(START_AXE_X, start_axe_y[x])
                turtles.append(new_turtle)

            race_turtle()
        case _:
            continue

    window.exitonclick()
