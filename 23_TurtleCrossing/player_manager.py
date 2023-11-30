from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(x=0, y=-280)
        self.speed("fastest")
        self.setheading(90)
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()

    def move_forward(self):
        self.setheading(90)
        self.y_pos += 10
        self.goto(self.x_pos, self.y_pos)

    def move_down(self):
        self.setheading(270)
        self.y_pos -= 10
        self.goto(self.x_pos, self.y_pos)

    def move_right(self):
        self.setheading(0)
        self.x_pos += 10
        self.goto(self.x_pos, self.y_pos)

    def move_left(self):
        self.setheading(180)
        self.x_pos -= 10
        self.goto(self.x_pos, self.y_pos)


    def reset_turtle(self):
        self.x_pos = 0
        self.y_pos = -280
        self.goto(self.x_pos, self.y_pos)
        