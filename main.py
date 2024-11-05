import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os
from tkinter import font
from PIL import ImageFont


# Custom font
custom_font_path = "pkgb.ttf"
custom_font = ImageFont.truetype(custom_font_path, size=16) 

# COLORS
c0 = "#F4E6F5"  # Pink gameboy...I guess?
c1 = "#F4E6F5"
c2 = "#444466"  # Black
c3 = "#feffff"  # White


file_path = "pokemon_data.json"
with open(file_path, "r") as file:
    pokemon_data = json.load(file)


def pokedex():

    global pokemon_data, dex_name, dex_type, dex_id, image_pokemon
    pokemon_name = random.choice(list(pokemon_data.keys()))
    pokemon_info = pokemon_data[pokemon_name]["info"]

    dex_name.config(text=pokemon_info[0].split(": ")[1])
    dex_type.config(text=pokemon_info[1].split(": ")[1])
    dex_id.config(text=pokemon_info[2].split(": ")[1])

    image_path = os.path.join("", pokemon_info[3])
    img = Image.open(image_path)
    img = img.resize((200, 200))
    photo_image = ImageTk.PhotoImage(img)
    image_pokemon.config(image=photo_image)
    image_pokemon.image = photo_image 



# Main
red_dex = Tk()
red_dex.title("Pokémon red / Pokedex")
red_dex.geometry('500x300')
pokefont = font.Font(red_dex, family=custom_font.getname()[0], size=16)
img = PhotoImage(file='icon.png')
red_dex.iconphoto(False, img)


red_dex.resizable(0, 0)
# Background Color
red_dex.configure(bg=c1)
ttk.Separator(red_dex, orient=HORIZONTAL).grid(row=0, column=1, ipadx=500)


# screen split
dex_frame = Frame(red_dex, width=500, height=250, relief="flat", bg=c0)
dex_frame.grid(row=1, column=0)


# 

# name
dex_name = Label(dex_frame, text="Bulbasaur", relief=FLAT,
                 anchor=CENTER, font=pokefont, bg=c2, fg=c3)
dex_name.place(x=250, y=50)

# type

dex_type = Label(red_dex, text="Grass/Poison", relief=FLAT, anchor=CENTER,
                 font=pokefont, bg=c2, fg=c3)
dex_type.place(x=250, y=95)

# ID

dex_id = Label(red_dex, text="001", relief=FLAT, anchor=CENTER,
               font=pokefont, bg=c2, fg=c3)
dex_id.place(x=250, y=130)


# Poke IMG

dex_img = Image.open("img/0001.png")
dex_img = dex_img.resize((200, 200))
dex_img = ImageTk.PhotoImage(dex_img)

image_pokemon = Label(red_dex, image=dex_img, relief="flat")
image_pokemon.place(x=30, y=50)


# Random Button

dex_button = Button(red_dex, text="RANDOM",font=pokefont,bg=c2, fg=c1, command=pokedex)
dex_button.place(x=290, y=200)


#right button
right_button = Button(red_dex, text=">",font=pokefont,bg=c2, fg=c1)
right_button.place(x=446, y=200)

#Left button
left_button = Button(red_dex, text="<",font=pokefont,bg=c2, fg=c1)
left_button.place(x=250, y=200)


# Loop
red_dex.mainloop()
