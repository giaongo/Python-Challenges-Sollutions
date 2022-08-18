from turtle import Turtle
import time


class PlayerGuess(Turtle):

    def __init__(self, answer_state):
        super().__init__()
        self.answer_state = answer_state
        self.penup()
        self.hideturtle()
        self.color("black")

    def retrieve_data(self, data_frame):
        found_answer_series = data_frame[data_frame.state == self.answer_state]
        x_coordinate = int(found_answer_series.x)
        y_coordinate = int(found_answer_series.y)
        return x_coordinate, y_coordinate

    def write_to_map(self, coordinate):
        self.clear()
        self.goto(coordinate)
        self.write(f"{self.answer_state}", align="center", font=("Arial", 6, "bold"))

    def notify_player(self, notify_text):
        self.goto(x=0, y=-90)
        self.color("red")
        self.write(f"{notify_text}", align="center", font=("Arial", 15, "normal"))
        time.sleep(1)
        self.clear()
