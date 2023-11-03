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
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

timmy = t.Turtle
# 10 x 10
# DOT = 20PX 
def dot(turtle):
    turtle.dot()

dot(timmy)

# 50PX APART

screen = t.Screen()
screen.exitonclick()