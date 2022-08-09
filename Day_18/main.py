from turtle import Turtle, Screen
import random
turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
# Challenge 1- Draw a square
# for i in range(5):
#     turtle.forward(100)
#     turtle.right(90)

# Challenge 2 - Draw a dashed line
# for i in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Challenge 3 - Draw a different shapes
pen_color = ["blue", "green", "pink", "black", "brown", "coral", "cyan", "yellow"]
for i in range(3, 11):
    turn_angle = round(360 / i)
    turtle.pencolor(random.choice(pen_color))
    for j in range(i):
        turtle.forward(100)
        turtle.right(turn_angle)





screen = Screen()
screen.exitonclick()