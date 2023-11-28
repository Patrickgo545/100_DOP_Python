from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10

    def move(self):
        # y_pos = self.ycor()
        # if y_pos == 300:
        #     self.moving_up = False
        # elif y_pos == -300:
        #     self.moving_up = True

        # if self.moving_up == True:
        #     new_y = self.ycor() + 10
        # else:
        #     new_y = self.ycor() - 10
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.move()
        self.bounce_x()

