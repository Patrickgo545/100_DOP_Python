import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
# CREATE TURTLE OBJECT TO WRITE STATE
class StateText(turtle.Turtle):
    def __init__(self, player_input):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.state_data = data[data.state == player_input]
        self.state = player_input

    def write_text(self):
        x_cor = self.state_data.x.item()
        y_cor = self.state_data.y.item()
        self.goto(x=x_cor, y=y_cor)
        self.write(f"{self.state}", align="center", font=("Aerial", 12, "normal"))

# CREATE DATA DICTIONARY
data = pd.read_csv("./50_states.csv")
data_list = data["state"].to_list()
data_dict = {}

# STATE = FALSE IF PLAYER HASN'T GUESSED IT
for state in data_list:
    data_dict[state] = False


# GAME LOGIC
game_on = True

while game_on:
    # NUM OF STATES GUESSED
    states_guessed = []
    for state in data_dict:
        if data_dict[state] != False:
            states_guessed.append(state)

    # PROMPT USER
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").title()
    
    # BREAK LOOP ON EXIT
    if answer_state == "Exit":
        break

    # IF USER GUESSES CORRECT
    for state in data_list:
        if answer_state == state:
            input = StateText(player_input=answer_state)
            input.write_text()
            data_dict[state] = input

# CREATE CSV FOR MISSED STATES
for state in states_guessed:
    data_list.remove(state)

feedback_dataframe = pd.DataFrame(data_list)
feedback_dataframe.to_csv("Results.csv", index=False)

turtle.mainloop()