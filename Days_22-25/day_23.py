# Day 23 of the 100 Days of Code Challenge
# Turtle Crossing Game

from turtle import Turtle, Screen
from script23_car_mgmt import CarManager
from script23_player import Player
from script23_score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create player object
player = Player()

screen.listen()
screen.onkeypress(fun=player.move, key='Up')

# create CarManager object
car_manager = CarManager()

# create scoreboard object
score_board = ScoreBoard()

play = True
while play:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.generate_cars()

    if player.ycor() >= 280:
        player.reset_pos()
        car_manager.increase_speed()
        score_board.increase_score()

    for car in car_manager.cars:
        if player.distance(car) < 25:
            play = False
            score_board.game_over()


screen.exitonclick()
