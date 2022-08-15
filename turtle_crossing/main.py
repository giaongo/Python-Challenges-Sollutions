from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)







screen.exitonclick()