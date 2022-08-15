from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.random_color()
        self.random_position()

    def random_color(self):
        rand_r = random.randint(0, 255)
        rand_g = random.randint(0, 255)
        rand_b = random.randint(0, 255)
        self.color(rand_r, rand_g, rand_b)

    def random_position(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-270, 280)
        self.goto(rand_x, rand_y)

    def move_forward(self):
        self.setheading(180)
        if self.xcor() > -300:
            new_x = self.xcor() + 20
            self.setx(new_x)