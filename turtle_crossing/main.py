from turtle import Screen
import time
from Player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.move_forward)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)






screen.exitonclick()