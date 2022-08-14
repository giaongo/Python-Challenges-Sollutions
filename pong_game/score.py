from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, position, player_name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.player_name = player_name
        self.post_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.post_score()

    def post_score(self):
        self.write(f"{self.player_name} : {self.score}", False, align="center", font=("Comic Sans MS", 20, "normal"))

    def post_game_over(self):
        self.write("Game over", False, align="center", font=("Arial", 30, "normal"))