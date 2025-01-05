from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

df = pandas.read_csv("data/french_words.csv")
df_dict = df.to_dict(orient="records")
current_card = {}


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df_dict)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def remove_word():
    df_dict.remove(current_card)
    review_df = pandas.DataFrame(df_dict)
    review_df.to_csv("words_to_learn.csv", index=False)
    new_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=1, row=1)

new_word()

window.mainloop()
