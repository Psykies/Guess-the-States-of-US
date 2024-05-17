# importing panda to work with the csv file where name of the sate and co-ordinate are stored and turtle
import turtle
import pandas

# setting up the screen with turtle and using map of usa as background
screen = turtle.Screen()
screen.title("Guess the States of US")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# storing the data from csv file where name of the state and co-ordinates are stored
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# making an empty list to store the right answer of the states
guessed_state = []

# looping to ask all the name of the state ,exit to exit
while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Guess  the remaining  state ").title()

    # creating a instance to exit the loop and print all the state that was missed
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        print(f"You have guessed {guessed_state} states correctly")
        if len(missing_states) == 0:
            print("/n Congratulations you have named every state correctly")
        else:
            print(f"you are still missing on ")
            print(missing_states)
        break

    # To write the name of the state in the map if guessed correctly using turtle
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        guessed_state.append(answer)


screen.exitonclick()
