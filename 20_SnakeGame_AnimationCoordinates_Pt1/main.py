from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
sal = Snake()

screen.listen()
screen.onkey(sal.up, "Up")
screen.onkey(sal.down, "Down")
screen.onkey(sal.left, "Left")
screen.onkey(sal.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(.1)
    screen.update()
    
    sal.move_snake()




















screen.exitonclick()