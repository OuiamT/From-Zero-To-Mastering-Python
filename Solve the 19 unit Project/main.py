import turtle 
import pandas as pd

gussed = []
missing_countries = []

window = turtle.Screen()
window.bgpic("map.gif")
window.setup(1000, 700)
window.title("Map Game")

data = pd.read_csv("coordinates.csv")
countries = data["country"].to_list()
while len(gussed) < 13:
    answer = window.textinput(f"{len(gussed)} / 13 guessed", "Type a country name:").capitalize()
    if answer in countries:
        gussed.append(answer)
        select = turtle.Turtle()
        select.hideturtle()
        select.penup()
        country_x = data[data["country"] == answer]["x"].item()
        country_y = data[data["country"] == answer]["y"].item()
        select.goto(country_x, country_y)
        select.fillcolor("red")
        select.begin_fill()
        select.circle(10)
        select.end_fill()
        select.write(answer, font=("Arial", 15))

    elif answer == "Exit":
        for country in countries:
            if country not in gussed:
                missing_countries.append(country)
        final_csv = pd.DataFrame(missing_countries).to_csv("notgussed.csv")
        break