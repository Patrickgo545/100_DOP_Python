from turtle import Turtle
import random

SPEEDS = []
X_START_POSITION = 280
COLORS = ["red", "orange", "green", "blue", "purple", "brown", "black"]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.seth(180)
        self.car_list = []
        self.car_count = len(self.car_list)
        self.hideturtle()
        self.difficulty = 5


    def spawn_cars(self):
        chance = [1,0]
        weights = [0.1, 0.9]
        spawn = random.choices(chance, weights=weights)[0]

        if spawn == 1:
            y_pos_rand = random.randint(-260,280)
            car = CarManager()
            car.color(random.choices(COLORS)[0])
            car.speed(self.difficulty)
            car.goto(x=X_START_POSITION, y=y_pos_rand)
            car.showturtle()
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            x_pos = car.xcor()
            new_pos = x_pos - self.difficulty
            car.goto(new_pos, car.ycor())
        
            # REMOVE CARS FROM LIST AFTER IT CLEARS LEFT SCREEN
            if new_pos < -350:
                self.car_list.remove(car)

    
            


        
# CREATE LIST TO HOLD Y VALUES FOR Y_COR OF SPAWNED CARS
# CREATE A CHANCE TO SPAWN
# ELIMINATE CAR WHEN IT REACHES LEFT SIDE OF SCREEN

