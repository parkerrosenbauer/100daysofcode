from turtle import Turtle

STRETCH_WID = 3
STRETCH_LEN = 1
SHAPE = 'square'
COLOR = 'white'
UP = 90
DOWN = 270
MOVE_SPEED = 30


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=STRETCH_LEN, stretch_len=STRETCH_WID)
        self.penup()
        self.setheading(90)
        self.color(COLOR)
        self.starting_x = x
        self.starting_y = y
        self.goto(self.starting_x, self.starting_y)

    def up(self):
        self.forward(MOVE_SPEED)

    def down(self):
        self.backward(MOVE_SPEED)

    def reset_position(self):
        self.goto(self.starting_x, self.starting_y)
