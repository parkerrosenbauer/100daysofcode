# Day 20 & 21 of 100 Days of Code Challenge
# Snake Game
from turtle import Screen
from script20_snake import Snake
from script20_food import Food
from script20_score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# perpetual forward movement
move = True
while move:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # losing conditions
    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        move = False
        scoreboard.game_over()

    # collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            move = False
            scoreboard.game_over()

screen.exitonclick()
