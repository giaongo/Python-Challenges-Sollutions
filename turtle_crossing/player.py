from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)

    def move_forward(self):
        new_y = self.ycor() + 10
        self.sety(new_y)

    def return_to_origin(self):
        self.goto(x=0, y=-280)
