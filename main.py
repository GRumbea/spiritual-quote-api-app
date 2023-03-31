import tkinter.font

import requests
from tkinter import *

response = requests.get(url="https://buddha-api.com/api/random")
response.raise_for_status()
quote = response.json()["text"]
author = response.json()["byName"]


def get_quote():
    global response
    response = requests.get(url="https://buddha-api.com/api/random")
    response.raise_for_status()
    new_quote = response.json()["text"]
    new_author = response.json()["byName"]
    canvas.itemconfig(quote_text, text=new_quote)
    canvas.itemconfig(author_name, text=f"-{new_author}")



window = Tk()
window.title("Spiritual Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=420)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(column=0, row=0)
quote_text = canvas.create_text(150, 150, text=quote, width=250, font=("Calisto MT", 18, "italic"))
author_name = canvas.create_text(150, 300, text=f"-{author}", width=250, font=("Calisto MT", 18, "italic"))

lotus_img = PhotoImage(file="lotus_img.png")
lotus_btn = Button(image=lotus_img, highlightthickness=0, height=100, width=100, command=get_quote)
lotus_btn.grid(column=0, row=1)
print(tkinter.font.families())



window.mainloop()


