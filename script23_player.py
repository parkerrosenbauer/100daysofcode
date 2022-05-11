from turtle import Turtle
STARTING_POS = 0, -280
MOVE_DIST = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def reset_pos(self):
        self.hideturtle()
        self.goto(STARTING_POS)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DIST)
