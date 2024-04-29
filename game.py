from tkinter import *
import random

# Initialize the game
def start_game():
    global current_player
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
    current_player = random.choice(players)
    status_label.config(text=current_player + "'s Turn")

# Check if there are any empty spaces left on the board
def has_empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                return True
    return False

# Check if the current player has won the game
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="yellow")
        buttons[1][1].config(bg="yellow")
        buttons[2][2].config(bg="yellow")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif not has_empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False

# Handle the next turn of the game
def next_turn(row, column):
    global current_player

    if buttons[row][column]["text"] == "" and not check_winner():

        if current_player == players[0]:
            buttons[row][column]["text"] = current_player
            if check_winner() is True:
                status_label.config(text=current_player + " Wins!")
            elif check_winner() is False:
                current_player = players[1]
                status_label.config(text=current_player + "'s Turn")
            elif check_winner() == "Tie":
                status_label.config(text="It's a Tie!")
        else:
            buttons[row][column]["text"] = current_player

            if check_winner() is True:
                status_label.config(text=current_player + " Wins!")
            elif check_winner() is False:
                current_player = players[0]
                status_label.config(text=current_player + "'s Turn")
            elif check_winner() == "Tie":
                status_label.config(text="It's a Tie!")

# Create the game window
window = Tk()
window.title("Tic Tac Toe Game by Mubashar Ghazi")
window.configure(bg='sky blue')

players = ["X", "O"]
current_player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

status_label = Label(text="Welcome to Tic Tac Toe!", font=("lucida console", 40))
status_label.pack()

reset_button = Button(text="New Game", font=("consolas", 20), command=start_game)
reset_button.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", command=lambda row=row, column=column:
        next_turn(row, column), font=("consolas", 40), width=6, height=2)
        buttons[row][column].grid(row=row, column=column, padx=6, pady=5)

window.mainloop()