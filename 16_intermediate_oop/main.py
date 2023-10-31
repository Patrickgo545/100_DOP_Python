
# from turtle import Turtle , Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")

# for i in range(4):
#     timmy.left(90)
#     timmy.forward(100)

# timmy.left(90)
# timmy.forward(50)
# timmy.right(90)
# timmy.forward(25)
# timmy.right(90)
# timmy.forward(50)

# for i in range(4):
#     timmy.left(90)
#     timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name" , ["Pikachu" , "Squirtle" , "Charmander"])
table.add_column("Type" , ["Electric" , "Water" , "Fire"])

table.align = "l"

print(table.align)

print(table)