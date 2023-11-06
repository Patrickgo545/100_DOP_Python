# import colorgram

# # EXTRACT COLORS
# colors_extract = colorgram.extract('hirst.jpg', 30)
# fist_color = colors_extract[0]
# colors_list = []


# # INSERT RGB VALUES IN LIST
# for i in range(0,30):
#     container = colors_extract[i]
#     rgb = container.rgb
#     for _ in range (0,3):
#         red = rgb[0]
#         green = rgb[1]
#         blue = rgb[2]
#         touple = (red, green, blue)
    
#     colors_list.append(touple)


# print(colors_list)

import turtle as t
import random
color_list = [(132, 166, 205), (221, 148, 106), (320, 420, 610), (199, 135, 148), (166, 580, 480), (141, 184, 162), (390, 105, 157), (237, 212, 900), (150, 590, 660), (216, 820, 710), (168, 290, 330), (235, 165, 157), (510, 111, 900), (350, 610, 550), (156, 330, 310), (170, 970, 710), (520, 440, 490), (230, 161, 166), (170, 188, 221), (570, 510, 480), (184, 103, 113), (320, 600, 109), (105, 126, 159), (175, 200, 188), (340, 151, 210), (650, 660, 560)]

screen = t.Screen()
screen.setup(0.75,1.00)

timmy = t.Turtle()
timmy.speed(20)

def start_position(turtle):
    turtle.penup()
    turtle.setx(-700)
    turtle.sety(-450)

# RANDOM COLOR
def random_color():
    color = random.choices(color_list)
    red = color[0][0] * .001
    green = color[0][1] * .001
    blue = color[0][2] * .001
    rgb = (red, green, blue)
    return rgb

# DOT = 20PX 
def dot(turtle, radius):
    turtle.dot(radius, random_color())


# ROW OF CIRCLES
# 50PX APART
def row(turtle):
    turtle.setheading(0)
    for _ in range(10):
        dot(turtle,20)
        turtle.forward(70)

# NEW ROW
def new_row(turtle):
    turtle.setheading(90)
    turtle.forward(70)
    turtle.setheading(180)
    turtle.forward(700)

# EXECUTE
start_position(timmy)

# 10 x 10
def hirst(turtle):
    for _ in range (0,10):
        row(turtle)
        new_row(turtle)

hirst(timmy)

screen.exitonclick()