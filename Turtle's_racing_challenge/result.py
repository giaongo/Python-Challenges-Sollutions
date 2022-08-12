from turtle import Turtle


class Result(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("orange")
        self.clear()

    def print_result(self, result, winner):
        self.write(f"You have {result} the bet. {winner} turtle is the winner", align="center", font=("Arial", 15, "bold"))
