import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")
# Challenge 1- Draw a square
# for i in range(5):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2 - Draw a dashed line
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3 - Draw a different shapes
# pen_color = ["blue", "green", "pink", "black", "brown", "coral", "cyan", "yellow"]
# for i in range(3, 11):
#     turn_angle = round(360 / i)
#     tim.pencolor(random.choice(pen_color))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(turn_angle)

# Challenge 4 - Draw a random walk
direction = [0,90,180,270]
turtle.colormode(255)
tim.pensize(10)
tim.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()