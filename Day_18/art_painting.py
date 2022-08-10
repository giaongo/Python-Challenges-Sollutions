import turtle
import colorgram
from turtle import Turtle, Screen
import random

# color_extracts = []
# colors = colorgram.extract('image.jpg', 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_extracts.append(new_color)
# print(color_extracts)

color_list = [(238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106),
              (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24),
              (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
              (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85),
              (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179),
              (122, 169, 190), (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
y_coordinate = 0
for i in range(0, 10):
    x_coordinate = 0
    tim.setx(x_coordinate)
    for j in range(0, 10):
        tim.pendown()
        tim.pencolor(random.choice(color_list))
        tim.begin_fill()
        tim.dot(20)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
    y_coordinate += 50
    tim.sety(y_coordinate)


screen = Screen()
screen.exitonclick()