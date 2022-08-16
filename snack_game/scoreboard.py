from turtle import Turtle, Screen

FONT = ("Courier", 18, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.colormode(255)
        self.high_score = 0
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
        self.write(f"Total score : {self.score} High Score: {self.high_score}", False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.post_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER!!!!!", align="center", font=GAME_OVER_FONT)
