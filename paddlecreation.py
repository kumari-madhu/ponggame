from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.goto(position)

    def move_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
