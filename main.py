import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S STATES GAME")
image = "c:\\Users\\Jamshaid Mustafa\\New folder\\ahmed mustafa\\usa game.py\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("c:\\Users\\Jamshaid Mustafa\\New folder\\ahmed mustafa\\usa game.py\\50_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 answered!" ,
                                    prompt="whats another states name?")
    if answer_state is None:
        break
    answer_state = answer_state.title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_Data = pandas.DataFrame(missing_states)
        new_Data.to_csv("c:\\Users\\Jamshaid Mustafa\\New folder\\ahmed mustafa\\usa game.py\\states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)




screen.exitonclick()










