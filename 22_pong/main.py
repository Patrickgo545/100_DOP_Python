from turtle import Screen
import time
import paddle
import ball
from scoreboard import Scoreboard

# SET UP SCREEN
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# CREATE PADDLES
r_paddle = paddle.Paddle(x_cor=350,y_cor=0)
l_paddle = paddle.Paddle(x_cor=-350, y_cor=0)

# PADDLE - SCREEN LISTEN
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# BALL
pong = ball.Ball()

# SCOREBOARD
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong.move()
    scoreboard.update_scoreboard()

    # COLLISION WITH WALL
    if pong.ycor() == 290 or pong.ycor() == -290:
        pong.bounce_y()

    # COLLISION WITH PADDLES
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320:
        pong.bounce_x()

    if pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    # R PLAYER SCORES
    if pong.xcor() > 400:
        pong.reset_ball()
        scoreboard.l_point()

    # L PLAYER SCORES
    if pong.xcor() < -400:
        pong.reset_ball()
        scoreboard.r_point()
    

screen.exitonclick()