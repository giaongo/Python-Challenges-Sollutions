from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_body = []
x_coordinate = 0
for i in range(3):
    snake = Turtle(shape="square")
    print(snake.shapesize())
    snake.color("white")
    snake.setx(x_coordinate)
    x_coordinate -= 20
    snake_body.append(snake)



















screen.exitonclick()