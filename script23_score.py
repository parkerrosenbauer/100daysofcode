from turtle import Turtle

FONT_TYPE = "Courier", 18, "bold"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-285, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT_TYPE)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER. Final Score: {self.score}", align='center', font=FONT_TYPE)
