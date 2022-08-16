from turtle import Screen
import time

from cars_list import CarsList
from level import Level
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
game_level = Level()

number_of_loop = 0
while is_game_on:
    screen.update()
    time.sleep(game_level.car_speed)

    if player.ycor() >= 290:
        game_level.increase_level()
        player.return_to_origin()

    if number_of_loop % 6 == 0:
        cars.create_car()

    # Loop for car moving on the screen
    index = 0
    while index < len(cars.cars_list):
        car = cars.cars_list[index]

        if player.distance(car) < 17:
            game_level.post_game_over()
            is_game_on = False
        car.move_forward()

        if car.xcor() < -300:
            car.hideturtle()
            cars.remove_car(car)
            index -= 1
        else:
            index += 1

    number_of_loop += 1

screen.exitonclick()
