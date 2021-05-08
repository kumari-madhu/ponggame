from turtle import Turtle, Screen
from paddlecreation import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-game")
screen.tracer(0)
paddle = Turtle()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
# if right misses
    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_point()
# if left misses
    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()





screen.exitonclick()
