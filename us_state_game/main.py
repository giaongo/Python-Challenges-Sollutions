import turtle
from turtle import Screen
import pandas
from player_guess import PlayerGuess

# Setting up the screen and append image background
screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state_name = data["state"].tolist()
correct_guess = []

# Game starts
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's "
                                                                                            "name?").title()
    if answer_state == "Exit":
        break
    player_guess = PlayerGuess(answer_state)
    if answer_state in data.values:
        if answer_state not in correct_guess:
            coordinate = player_guess.retrieve_data(data)
            player_guess.write_to_map(coordinate)
            correct_guess.append(answer_state)
        else:
            player_guess.notify_player("This state has been guessed before")
    else:
        player_guess.notify_player("No data found")

# Game exits and all remaining states will be written to a csv file
remained_states = []
for state in all_state_name:
    if state not in correct_guess:
        remained_states.append(state)

remained_state_dict = {
    "state": remained_states
}

pandas.DataFrame(remained_state_dict).to_csv("remained_states.csv")