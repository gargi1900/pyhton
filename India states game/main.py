import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "India-state.gif"
screen.setup(500, 500)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()

guessed_states = []
guessed_wrong_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 29 States Correct",
                                    prompt="Guess state's name? or want to exit").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to learn")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
