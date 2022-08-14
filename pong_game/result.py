from turtle import Turtle

RED = "#E05D5D"
GREEN = "#59CE8F"


class Result(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(RED)
        self.home()
        self.hideturtle()
        self.clear()

    def post_result(self, winner):
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
        self.goto(0, -40)
        self.color(GREEN)
        if winner is not None:
            self.write(f"{winner} is the winner!!", align="center", font=("Comic Sans MS", 20, "normal"))
        else:
            self.write(f"It is a fair", align="center", font=("Comic Sans MS", 20, "normal"))
