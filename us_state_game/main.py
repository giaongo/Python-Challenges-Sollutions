import turtle
from turtle import Screen
import pandas

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
