from turtle import Turtle, Screen
import turtle as t
import random

# GET MODULE TO DRAW A SQUARE
def draw_square(turtle, pixels):
    for i in range(4):
        turtle.forward(pixels)
        turtle.right(90)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape()
timmy_the_turtle.color("green")

# draw_square(timmy_the_turtle,100)


# INDENTED LINE 

# for _ in range (15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


# RANDOM COLOR
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r,g,b)
    return color


# SHAPES
def shapes(turtle, qty_shapes):
    sides = 3

    for shapes in range(qty_shapes):
        turtle.pencolor(random_color())
        vector_angle = 360 / sides

        for line in range(sides):
            turtle.forward(100)
            turtle.right(vector_angle)

        sides += 1 

# shapes(timmy_the_turtle, 10)


# RANDOM WALK
def random_walk(turtle, strokes):
    turtle.pensize(10)
    turtle.speed(10)

    angle = [0, 90, 180, 270]

    for _ in range(strokes):
        turtle.pencolor(random_color())
        turtle.setheading(random.choice(angle))
        turtle.forward(50)

# random_walk(timmy_the_turtle,100)


# SPIROGRAPH
def spirograph(turtle, qty_circles):
    turtle.speed(20)

    full_circle = 360
    s_angle = full_circle / qty_circles

    for _ in range(qty_circles):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.right(s_angle)

spirograph(timmy_the_turtle,75)


screen = Screen()
screen.exitonclick()