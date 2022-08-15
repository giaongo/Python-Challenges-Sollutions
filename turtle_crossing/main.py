from turtle import Screen
import time

from cars_list import CarsList
from player import Player

# Screen setting up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.colormode(255)

player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.move_forward)

is_game_on = True
cars = CarsList()
number_of_loop = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)

    if number_of_loop % 3 == 0:
        cars.create_car()

    for car in cars.cars_list:
        if player.distance(car) < 18:
            is_game_on = False
        car.move_forward()
        if car.xcor() < -300:
            car.clear()

    number_of_loop += 1

screen.exitonclick()
