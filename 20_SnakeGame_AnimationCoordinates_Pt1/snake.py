from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.x_start_position = [0, -20, -40]
        self.spawn_snake()
        self.head = self.segment[0]


    def spawn_snake(self):
        for pixel_index in range (0,3):

            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.goto(x=self.x_start_position[pixel_index],y=0)
            self.segment.append(block)

    def move_snake(self):
        for block_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[block_num - 1].xcor()
            new_y = self.segment[block_num - 1].ycor()
            self.segment[block_num].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)        