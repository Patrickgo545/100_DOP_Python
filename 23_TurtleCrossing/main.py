import time
from turtle import Screen
import player_manager
from car_manager import CarManager
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = player_manager.Player()
car_manager = CarManager()
score = scoreboard.Scoreboard()

# SCREEN LISTEN
screen.listen()
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.spawn_cars()
    car_manager.move_cars()
    score.update()

    # CHECK COLLISION WITH CAR
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    screen.update()


    # PLAYER CROSSES STREET
    if player.ycor() > 280:
        score.new_level()
        player.reset_turtle()
        car_manager.difficulty += 2

screen.exitonclick()