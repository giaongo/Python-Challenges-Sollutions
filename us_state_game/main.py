import turtle
from turtle import Screen
import pandas

from user_guess import UserGuess

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_guess = []
score = 0
game_is_on = True
while game_is_on:
    if len(correct_guess) < 50:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
        answer_state = answer_state.title()
        user_guess = UserGuess(answer_state)

        if answer_state in data.values:
            if answer_state not in correct_guess:
                coordinate = user_guess.retrieve_data(data)
                user_guess.write_to_map(coordinate)
                correct_guess.append(answer_state)
                score += 1
            else:
                print("You have already guessed this word before")
        else:
            print("data not found")
    else:
        game_is_on = False

turtle.mainloop()

