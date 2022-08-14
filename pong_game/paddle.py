from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x_position, 0)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 80
            self.sety(new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 80
            self.sety(new_y)
