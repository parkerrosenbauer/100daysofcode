from turtle import Turtle
import random

SHAPE = 'circle'
COLOR = 'white'
START_ANGLES = (135, 225)
MOVE_DIST = 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.new_round()

    def move(self):
        self.forward(MOVE_DIST)

    def paddle_collide(self, a1, a2):
        opposite_way = random.randint(a1, a2)
        self.setheading(opposite_way)

    def wall_collide(self):
        opposite_way = abs(self.heading() - 360)
        self.setheading(opposite_way)

    def new_round(self):
        self.goto(0, 0)
        self.setheading(random.randint(START_ANGLES[0], START_ANGLES[1]))
