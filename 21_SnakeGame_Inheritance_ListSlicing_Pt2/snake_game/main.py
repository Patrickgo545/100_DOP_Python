from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# scoreboard.refresh_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(.1)
    screen.update()
    
    snake.move_snake()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.refresh_score()
        scoreboard.display_score()
        snake.extend()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False

    # DETECT COLLISION WITH TAIL 
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            
    # IF SNAKE HEAD COLLIDES WITH SNAKE SEGMENT - GAME OVER


scoreboard.game_over()
        






















screen.exitonclick()