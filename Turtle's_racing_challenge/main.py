from turtle import Turtle, Screen
import random
from result import Result

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Welcome To Turtle Racing")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

turtle_players = []
colors = ["red", "black", "pink", "brown", "blue", "violet"]
betting_result = Result()
x_coordinate = -280
y_coordinate = 210
for color in colors:
    player = Turtle(shape="turtle")
    player.color(color)
    player.penup()
    player.goto(x_coordinate, y_coordinate)
    y_coordinate -= 70
    turtle_players.append(player)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for player in turtle_players:
        if round(player.xcor()) >= 280:
            winner = player.pencolor()
            if winner == user_bet:
                result = "won"
            else:
                result = "lost"
            betting_result.print_result(result, winner)
            is_race_on = False
        random_distance = random.randint(0, 10)
        player.forward(random_distance)

screen.exitonclick()