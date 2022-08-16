from turtle import Turtle

FONT = ("Comic Sans MS", 18, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.game_level = 1
        self.car_speed = 0.1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-150, y=250)
        self.post_level()

    def increase_level(self):
        self.game_level += 1
        self.car_speed *= 0.7
        self.clear()
        self.post_level()

    def post_level(self):
        if self.game_level == 1:
            explain_level = "Beginner"
        elif self.game_level == 2:
            explain_level = "Intermediate"
        else:
            explain_level = "Hard"
        self.write(f"Level: {self.game_level}--{explain_level}", False, align="center", font=FONT)

    def post_game_over(self):
        self.home()
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
