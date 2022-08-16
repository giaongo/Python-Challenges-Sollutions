from turtle import Turtle, Screen

FONT = ("Courier", 18, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")


def read_high_score():
    with open("data.txt") as file:
        return int(file.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.colormode(255)
        self.high_score = read_high_score()
        self.goto(0, 260)
        self.penup()
        self.color(252, 190, 3)
        self.score = 0
        self.hideturtle()
        self.post_score()

    def update_score(self):
        self.score += 1
        self.post_score()

    def post_score(self):
        self.clear()
        self.write(f"Total score: {self.score} -- High Score: {self.high_score}", False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_high_score()
        self.score = 0
        self.post_score()

    def write_high_score(self):
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")
