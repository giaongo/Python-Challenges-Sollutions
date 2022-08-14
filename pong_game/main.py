from turtle import Screen
from ball import Ball
from liner import Liner
from paddle import Paddle
import time
from result import Result
from score import ScoreBoard

# Setting the main screen and input for players
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#010038")
screen.title("The Pong Game")
screen.tracer(0)
player_left = screen.textinput(title="Player_1's Name", prompt="Name of first player:")
player_right = screen.textinput(title="Player_2's Name", prompt="Name of second player:")

# Creating separator line
for y in range(280, -280, -20):
    Liner(y)

# Initiate 2 paddles, 2 scores, ball and result
paddle_left = Paddle(x_position=-350)
paddle_right = Paddle(x_position=350)
ball = Ball()
score_left = ScoreBoard(position=(-200, 250), player_name=player_left)
score_right = ScoreBoard(position=(200, 250), player_name=player_right)
result = Result()

# Listen on the key event to move the paddles up or down
screen.listen()
screen.onkeypress(key="Up", fun=paddle_right.up)
screen.onkeypress(key="Down", fun=paddle_right.down)
screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key="s", fun=paddle_left.down)

# Loop for game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()
    ball.detect_wall()
    ball.detect_paddle(paddle_right=paddle_right, paddle_left=paddle_left)

    if ball.xcor() > 400 or ball.xcor() < -400:  # if the ball goes out of bound -> score increases for the other player
        if ball.xcor() > 400:
            score_left.increase_score()
        elif ball.xcor() < -400:
            score_right.increase_score()
        ball.restart_ball()

    if score_right.score == 5 or score_left.score == 5:  # If the score reaches 5 -> game ends
        if score_right.score > score_left.score:
            winner = score_right.player_name
        elif score_right.score < score_left.score:
            winner = score_left.player_name
        else:
            winner = None
        result.post_result(winner)
        is_game_on = False

screen.exitonclick()
