from turtle import Turtle


class Liner(Turtle):

    def __init__(self, y_coordinate):
        super().__init__()
        self.draw_liner(y_coordinate)

    def draw_liner(self, y_coordinate):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.4, stretch_len=0.1)
        self.sety(y_coordinate)
