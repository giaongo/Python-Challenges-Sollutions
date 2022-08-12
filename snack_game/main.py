from turtle import Screen
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # this method is to turn off the turtle animation

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision with snake and food
    if snake.head.distance(food) < 20:
        score.update_score()
        snake.extend()
        food.move_random()

    # Detect collision with the wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 \
            or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()

    # Detect collision with its own tail
    if snake.collide_with_tail():
        game_is_on = False
        score.game_over()

screen.exitonclick()
