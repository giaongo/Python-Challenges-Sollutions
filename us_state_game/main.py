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
all_state_name = data["state"].tolist()
correct_guess = []
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's "
                                                                                            "name?").title()
    if answer_state == "Exit":
        break
    user_guess = UserGuess(answer_state)
    if answer_state in data.values:
        if answer_state not in correct_guess:
            coordinate = user_guess.retrieve_data(data)
            user_guess.write_to_map(coordinate)
            correct_guess.append(answer_state)
        else:
            print("You have already guessed this word before")
    else:
        print("data not found")

remained_states = []
for state in all_state_name:
    if state not in correct_guess:
        remained_states.append(state)

remained_state_dict = {
    "state": remained_states
}

pandas.DataFrame(remained_state_dict).to_csv("remained_states.csv")