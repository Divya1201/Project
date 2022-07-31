import tkinter as tk
import random

window = tk.Tk()
window.geometry("600x400")
window.config(bg="purple")
window.title("NUMBER GUESSING")

window.resizable(width=False, height=False)

# taking variables
TARGET = random.randint(1, 100)
RETRIES = 0
SCORE = 0


# Create a new game
def update_result(text):
    result.configure(text=text)


def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES, SCORE
    TARGET = random.randint(0, 100)
    RETRIES = 0
    SCORE = 0
    update_result(text="Guess a number between\n 1 and 100")


# Continue the ongoing game or end it
def play_game():
    global RETRIES, SCORE

    choice = int(number_form.get())

    if choice != TARGET:
        RETRIES += 1
        SCORE -= 1

        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number is less than {}".format(choice)
        else:
            hint = "The required number is greater than {}".format(choice)

        for i in range(int(TARGET / 2) + 1, 1, -1):
            n = i
            if TARGET % i == 0:
                hint1 = "The number to be guessed is divisible by: {}".format(i)
                break
            n -= 1
        if n == 1:
            hint1 = "The number to be guessed is a prime number"
        result += "\n\nHINT :\n" + hint + "\n" + hint1

    else:
        SCORE += 1
        hint = "Your score is : {}".format(SCORE)
        result = "You guessed the correct number after {} retries".format(RETRIES) + "\n" + hint
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"

    update_result(result)


# Heading of our game
title = tk.Label(window, text="Guessing Game", font=("Arial", 24), fg="black", bg="blue")


result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12), fg="White",
                  bg="#065569", justify=tk.LEFT)


play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",
                        command=new_game)


guess_button = tk.Button(window, text="Guess", font=("Arial", 13), state='disabled', fg="#13d675", bg="Black",
                         command=play_game)


exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="White", bg="#b82741", command=exit)


guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_number)

# Place the labels

title.place(x=170, y=50)
result.place(x=180, y=210)

# Place the buttons
exit_button.place(x=300, y=320)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

# Place the entry field
number_form.place(x=180, y=150)

# Start the window
window.mainloop()
