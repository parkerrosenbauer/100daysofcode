# Day 22 of 100 Days of Code Challenge
# Pong Game
from turtle import Screen, Turtle
from script22_paddle import Paddle
from script22_pingpong import Ball
from script22_score import ScoreBoard
import time

# Set up the screen
screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

# Create the paddle objects
left_p = Paddle(-475, 0)
right_p = Paddle(475, 0)

screen.listen()
screen.onkeypress(fun=left_p.up, key='w')
screen.onkeypress(fun=left_p.down, key='s')
screen.onkeypress(fun=right_p.up, key='Up')
screen.onkeypress(fun=right_p.down, key='Down')

# Create the pingpong ball
pingpong = Ball()

# Create the scoreboard
left_score = ScoreBoard(-50, 270)
right_score = ScoreBoard(50, 270)

# Insert the dividing line
divide_line = Turtle()
divide_line.hideturtle()
divide_line.pencolor('white')
divide_line.pensize(width=5)
divide_line.penup()
divide_line.setheading(90)

for i in range(-370, 350, 40):
    divide_line.goto(0, i)
    divide_line.pendown()
    divide_line.forward(20)
    divide_line.penup()

play = True
while play:
    time.sleep(.05)
    screen.update()
    pingpong.move()

    # ball collides with paddle
    if pingpong.distance(left_p) < 35:
        pingpong.paddle_collide(315, 405)
    elif pingpong.distance(right_p) < 35:
        pingpong.paddle_collide(135, 225)

    # ball collides with wall
    if pingpong.ycor() > 325:
        pingpong.wall_collide()
    elif pingpong.ycor() < -325:
        pingpong.wall_collide()

    # ball goes off-screen
    if pingpong.xcor() > 490:
        left_score.increase_score()
        left_p.reset_position()
        right_p.reset_position()
        pingpong.new_round()
    elif pingpong.xcor() < -490:
        right_score.increase_score()
        pingpong.new_round()
        left_p.reset_position()
        right_p.reset_position()

screen.exitonclick()
