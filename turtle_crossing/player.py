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
        if new_y >= 290:
            self.return_to_origin()

    def return_to_origin(self):
        self.goto(x=0, y=-280)
