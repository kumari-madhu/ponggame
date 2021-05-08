from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("courier", 20, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 20, "normal"))

    def l_point(self):
        self.lscore += 1
        self.score_update()

    def r_point(self):
        self.rscore += 1
        self.score_update()
