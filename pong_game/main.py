from turtle import Screen
from ball import Ball
from liner import Liner
from paddle import Paddle
import time
from score import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
player_left = screen.textinput(title="Player_1's Name", prompt="Name of first player:")
player_right = screen.textinput(title="Player_2's Name", prompt="Name of second player:")

for y in range(280, -280, -20):
    Liner(y)

paddle_left = Paddle(x_position=-350)
paddle_right = Paddle(x_position=350)
ball = Ball()
score_left = ScoreBoard(position=(-200, 250), player_name=player_left)
score_right = ScoreBoard(position=(200, 250), player_name=player_right)

screen.listen()

screen.onkeypress(key="Up", fun=paddle_right.up)
screen.onkeypress(key="Down", fun=paddle_right.down)
screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key="s", fun=paddle_left.down)

is_game_on = True
direction = "ahead"
while is_game_on:
    screen.update()
    time.sleep(0.03)
    ball.move_ball()
    ball.detect_wall()
    ball.detect_paddle(paddle_right=paddle_right, paddle_left=paddle_left)
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            score_left.increase_score()
        elif ball.xcor() < -400:
            score_right.increase_score()
        ball.restart_ball()

screen.exitonclick()
