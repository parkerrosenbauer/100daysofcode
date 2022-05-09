from turtle import Turtle
ALIGNMENT = "center"
FONT_TYPE = "Courier", 18, "bold"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT_TYPE)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER. Final Score: {self.score}", align=ALIGNMENT, font=FONT_TYPE)

    def increase_score(self):
        self.score += 1
        self.update_board()
