from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.home()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.03

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce("wall")

    def detect_paddle(self, paddle_right, paddle_left):
        if (self.distance(paddle_right) < 50 and 320 < self.xcor() < 350) or \
                (self.distance(paddle_left) < 50 and -350 < self.xcor() < -320):
            self.bounce("paddle")

    def bounce(self, surface):
        if surface == "wall":
            self.y_move *= -1
        elif surface == "paddle":
            self.x_move *= -1

    def restart_ball(self):
        rand_num_1 = [-1, 1]
        self.home()
        self.ball_speed *= 0.9
        self.x_move *= -1
        self.y_move *= random.choice(rand_num_1)
