from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.game_level = 1
        self.car_speed = 0.1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-200, y=250)
        self.post_level()

    def increase_level(self):
        self.game_level += 1
        self.car_speed *= 0.7
        self.clear()
        self.post_level()

    def post_level(self):
        self.write(f"Level: {self.game_level}", False, align="center", font=("Comic Sans MS", 20, "normal"))

    def post_game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))