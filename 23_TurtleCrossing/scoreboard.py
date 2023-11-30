from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def update(self):
        self.clear()
        self.goto(x=-245, y=270)
        self.write(f"level: {self.level}", align="center", font=("Aerial", 16, "normal"))

    def new_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Aerial", 24, "normal"))
