from turtle import Turtle

ALIGNMENT = 'center'
FONT_TYPE = "Courier", 40, "bold"
COLOR = 'white'


class ScoreBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=str(self.score), align=ALIGNMENT, font=FONT_TYPE)

    def increase_score(self):
        self.score += 1
        self.update_score()

