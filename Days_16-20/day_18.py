# Day 18 of 100 Days of Code Challenge
# Turtle GUI Art
from turtle import Turtle, Screen
import random

lil_guy = Turtle()
lil_guy.penup()
lil_guy.speed(0)
lil_guy.hideturtle()


def random_color():
    """generates 3 random floats between 0 and 1"""
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def paint_dots(row_num):
    lil_guy.setposition(-400, -350)
    for i in range(row_num):
        lil_guy.setx(-400)
        lil_guy.sety(-350 + i * 50)
        for x in range(10):
            lil_guy.dot(20, random_color())
            lil_guy.forward(50)


paint_dots(10)

screen = Screen()
screen.exitonclick()
