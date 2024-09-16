from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=790, height=600)
screen.title("PONG GAME")
screen.tracer(0)
time.sleep(0.1)


r_paddle = Paddle((375, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detection with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection with both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect when paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.l_point()


screen.exitonclick()
