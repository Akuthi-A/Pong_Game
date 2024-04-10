from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# create left_paddle
left_paddle = Paddle((350, 0))
right_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision w left_paddle
    if (ball.distance(left_paddle) < 50 and ball.xcor() > 320) or (ball.distance(right_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # swing and a miss (right left_paddle)
    if ball.xcor() > 380:
        ball.reset_ball_pos()
        scoreboard.left_point()

    # left left_paddle
    if ball.xcor() < -380:
        ball.reset_ball_pos()
        scoreboard.right_point()

screen.exitonclick()
