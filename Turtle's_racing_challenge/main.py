from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Welcome To Turtle Racing")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

turtle_players = []
colors = ["red", "black", "pink", "brown", "blue", "violet"]

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
                print(f"You have won the bet. {winner} turtle is winner")
            else:
                print(f"You have lost the bet. {winner} turtle is winner")
            is_race_on = False
        random_distance = random.randint(0, 10)
        player.forward(random_distance)

screen.exitonclick()