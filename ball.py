from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
# created two attributes inorder to create the bounce function
        self.x_pos = 10
        self.y_pos = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_pos *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_pos *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
