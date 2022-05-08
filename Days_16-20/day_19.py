# Day 19 of 100 Days of Code Challenge
# Turtle races
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [150, 90, 30, -30, -90, -150]
turtles = []

for turtle_index in range(0, 6):
    n_turtle = Turtle(shape='turtle')
    n_turtle.color(colors[turtle_index])
    n_turtle.penup()
    n_turtle.goto(x=-200, y=y_pos[turtle_index])
    turtles.append(n_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            winning = turtle.pencolor()
            race_on = False
            if user_bet == turtle.pencolor():
                print(f"You won the bet! The winning turtle was the {winning} turtle.")
            else:
                print(f"You lost the bet. The winning turtle was the {winning} turtle.")


screen.exitonclick()
