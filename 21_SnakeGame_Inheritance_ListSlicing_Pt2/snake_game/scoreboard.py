from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.speed("fastest")
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)
        
    def refresh_score(self):
        self.clear()
        self.score += 1

    def display_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 14, "normal"))
